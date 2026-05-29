
"""
Interactive Word Search Game Module

This module provides functionality to generate and play an interactive word search game.
Players can find hidden words in a grid and receive hints through clues.

Features:
    - Dynamically generates word search grids with hidden words
    - Supports both predefined and random word selections
    - Provides clues to help players find words
    - Interactive gameplay with user input and feedback

Author: Santosh
Version: 1.0
"""

import random
import string


def build_word_search(words, size=10):
    """
    Build a word search grid with hidden words.
    
    Args:
        words (list): List of words to hide in the grid.
        size (int, optional): Dimension of the square grid. Defaults to 10.
    
    Returns:
        list: A 2D grid (list of lists) with words placed and remaining cells filled with random letters.
    
    Raises:
        ValueError: If a word cannot be placed in the grid.
    """
    grid = [['' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0)]
    for word in words:
        placed = False
        random.shuffle(directions)
        for dr, dc in directions:
            max_row = size - len(word) + 1 if dr != 0 else size
            max_col = size - len(word) + 1 if dc != 0 else size
            start_positions = [(r, c) for r in range(max_row) for c in range(max_col)]
            random.shuffle(start_positions)
            for r, c in start_positions:
                if all(grid[r + i * dr][c + i * dc] in ('', char) for i, char in enumerate(word)):
                    for i, char in enumerate(word):
                        grid[r + i * dr][c + i * dc] = char
                    placed = True
                    break
            if placed:
                break
        if not placed:
            raise ValueError(f"Could not place the word: {word}")
    for r in range(size):
        for c in range(size):
            if grid[r][c] == '':
                grid[r][c] = random.choice(string.ascii_uppercase)
    return grid

def print_grid(grid):
    for row in grid:
        print(' '.join(row))
    print()

def play_word_search():
    def generate_random_words_and_clues(count=5, min_len=3, max_len=8):
        predefined_clues = {
            'PYTHON': 'Famous AI-powered programming language.',
            'JAVA': 'Most popular programming language for enterprise applications.',
            'JAVASCRIPT': 'Language of the web browser.',
            'ALGORITHM': 'Step-by-step procedure to solve a problem.',
            'DATABASE': 'Organized collection of data.',
            'NETWORK': 'Connected computers communicating together.',
            'SECURITY': 'Protecting systems from attacks.',
            'COMPILER': 'Translates code to machine language.',
            'VARIABLE': 'Container for storing data values.',
            'FUNCTION': 'Reusable block of code.'
        }
        clues = {}
        available_words = list(predefined_clues.keys())
        random.shuffle(available_words)
        for i in range(min(count, len(available_words))):
            word = available_words[i]
            clues[word] = predefined_clues[word]
        return clues

    use_random = input("Generate random words & clues? (y/N): ").strip().lower() == 'y'
    if use_random:
        try:
            count = int(input("How many words (default 5): ").strip() or 5)
        except ValueError:
            count = 5
        clues = generate_random_words_and_clues(count)
    else:
        clues = {
            'PYTHON': 'Famous AI-powered programming language.',
            'CODE': 'What programmers write.',
            'SEARCH': 'What you do in this puzzle.',
            'GAME': 'A fun activity with rules.',
            'FUN': 'Enjoyment or pleasure.'
        }
    words = list(clues.keys())
    grid = build_word_search(words)
    found = set()
    remaining_clues = dict(clues)
    print("Welcome to the interactive word search game!")
    print("Find all words hidden in the grid.")
    print("Clues:")
    for clue in remaining_clues.values():
        print(f" - {clue}")
    print()
    while len(found) < len(words):
        print_grid(grid)
        remaining_count = len(words) - len(found)
        print(f"Words remaining: {remaining_count}")
        guess = input("Enter a word you found (or 'quit'): ").strip().upper()
        if guess == 'QUIT':
            print("Thanks for playing.")
            return
        if guess in words:
            if guess in found:
                print("You already found that word.")
            else:
                found.add(guess)
                print(f"Great! You found {guess}.")
                if guess in remaining_clues:
                    del remaining_clues[guess]
                print("Remaining clues:")
                for clue in remaining_clues.values():
                    print(f" - {clue}")
        else:
            print("Not in the list. Try again.")
        print()
    print("Congratulations! You found all the words.")

if __name__ == "__main__":
    play_word_search()
