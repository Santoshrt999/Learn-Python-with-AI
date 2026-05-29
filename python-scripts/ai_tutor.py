"""
AI Learning Tutor — Learn Python concepts interactively with Claude.

How it works:
  1. You type a Python concept (e.g. "list comprehensions", "decorators")
  2. Claude explains it with a short code example
  3. Claude asks you 2 quiz questions to test your understanding
  4. You answer → Claude grades you and explains what was right or wrong

Usage:
  python ai_tutor.py
"""

import anthropic
from claude_client import get_client, MODEL, extract_text

# Instructs Claude to act as a tutor: explain, quiz, then grade
SYSTEM_PROMPT = """You are a friendly Python tutor for someone learning Python for the first time.

When given a concept to teach:
1. Give a clear, simple explanation (3-5 sentences max)
2. Show one short code example with comments
3. Ask exactly 2 quiz questions to test understanding

When given an answer to grade:
- Tell the user what they got right and what needs correction
- Give the correct answer if they were wrong
- Keep feedback encouraging and concise
"""


def explain_and_quiz(client: anthropic.Anthropic, concept: str) -> str:
    """Ask Claude to explain a concept and generate 2 quiz questions."""
    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": f"Teach me about: {concept}"}
        ]
    )
    return extract_text(response)


def grade_answer(client: anthropic.Anthropic, concept: str, quiz: str, user_answer: str) -> str:
    """Pass the original quiz + user's answer back to Claude for grading.

    Conversation history is replayed so Claude has full context when grading.
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user",      "content": f"Teach me about: {concept}"},
            {"role": "assistant", "content": quiz},
            {"role": "user",      "content": user_answer}
        ]
    )
    return extract_text(response)


def run():
    client = get_client()

    print("\n" + "=" * 50)
    print("   Python AI Tutor — powered by Claude")
    print("=" * 50)
    print("Type any Python concept to learn it.")
    print("Examples: 'list slicing', 'dictionaries', 'for loops', 'functions'")
    print("Type 'quit' to exit.\n")

    while True:
        concept = input("What do you want to learn? → ").strip()

        if concept.lower() in ("quit", "exit", "q"):
            print("\nHappy coding!")
            break

        if not concept:
            continue

        print("\nClaude is thinking...\n")
        quiz = explain_and_quiz(client, concept)
        print(quiz)

        answer = input("\nYour answer → ").strip()

        if answer.lower() in ("quit", "exit", "q"):
            break

        if answer:
            print("\nGrading your answer...\n")
            feedback = grade_answer(client, concept, quiz, answer)
            print(feedback)

        print("\n" + "─" * 50 + "\n")


if __name__ == "__main__":
    run()
