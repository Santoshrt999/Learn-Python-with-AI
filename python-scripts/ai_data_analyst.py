"""
AI Data Analyst — Ask plain English questions about your data using Claude.

How it works:
  1. Loads the Honda used car dataset by default (from data_analysis.py)
  2. You ask questions in plain English
  3. Claude reads the data and answers with specific numbers/insights
  4. Follow-up questions remember previous context (conversation history)

Usage:
  python ai_data_analyst.py                  # uses built-in Honda dataset
  python ai_data_analyst.py path/to/file.csv # use your own CSV file
"""

import sys
import anthropic
import pandas as pd
from claude_client import get_client, MODEL, extract_text
from data_analysis import load_data  # reuses the Honda DataFrame loader


# Instructs Claude to answer data questions concisely with real numbers
SYSTEM_PROMPT = """You are a data analyst assistant.
You will receive a dataset in JSON format and answer questions about it.
- Use specific numbers and values from the data in your answers
- Keep answers concise: 2-4 sentences unless a longer answer is clearly needed
- If a question can't be answered from the data, say so clearly
"""


def dataframe_to_json(df: pd.DataFrame) -> str:
    """Serialize the DataFrame to a JSON string so Claude can read it."""
    return df.to_json(orient="records", indent=2)


def load_csv(filepath: str) -> pd.DataFrame:
    """Load an external CSV file into a DataFrame."""
    return pd.read_csv(filepath)


def ask_claude(client: anthropic.Anthropic, data_json: str, question: str, history: list[anthropic.types.MessageParam]) -> str:
    """Send the data + conversation history + new question to Claude.

    On the first question, data is embedded in the message.
    On follow-ups, only the new question is added — history carries the context.
    """
    if not history:
        # First turn: include the full dataset as context
        messages = [
            {"role": "user", "content": f"Here is my dataset:\n\n{data_json}\n\nQuestion: {question}"}
        ]
    else:
        # Follow-up turns: history already has the data, just add the new question
        messages = history + [{"role": "user", "content": question}]

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages
    )
    return extract_text(response)


def run():
    client = get_client()

    # Load data from CLI arg (CSV) or default Honda dataset
    if len(sys.argv) > 1:
        csv_path = sys.argv[1]
        df = load_csv(csv_path)
        source = csv_path
    else:
        df = load_data()
        source = "Honda used car listings (built-in)"

    data_json = dataframe_to_json(df)

    print("\n" + "=" * 50)
    print("   AI Data Analyst — powered by Claude")
    print("=" * 50)
    print(f"Dataset : {source}")
    print(f"Rows    : {len(df)}  |  Columns: {list(df.columns)}")
    print("\nAsk questions in plain English. Follow-ups remember context.")
    print("Examples: 'which car is cheapest?', 'average km driven?', 'best value car?'")
    print("Type 'quit' to exit.\n")

    history: list[anthropic.types.MessageParam] = []

    while True:
        question = input("Your question → ").strip()

        if question.lower() in ("quit", "exit", "q"):
            print("\nGoodbye!")
            break

        if not question:
            continue

        print("\nAnalyzing...\n")
        answer = ask_claude(client, data_json, question, history)
        print(f"Claude: {answer}")

        # Append to history so follow-up questions have full context
        if not history:
            history.append({
                "role": "user",
                "content": f"Here is my dataset:\n\n{data_json}\n\nQuestion: {question}"
            })
        else:
            history.append({"role": "user", "content": question})

        history.append({"role": "assistant", "content": answer})

        print()


if __name__ == "__main__":
    run()
