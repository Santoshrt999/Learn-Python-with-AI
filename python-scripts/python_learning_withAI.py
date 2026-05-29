"""
Python Learning Reference — Core Language Concepts
Each section is wrapped in a function so you can run them individually
or all at once via the entry point at the bottom.
"""

import os
import csv
import json
from math import ceil, floor
from statistics import mean, median, mode
from random import sample
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown

console = Console()


# =============================================================================
# 1. VARIABLES & DATA TYPES
# =============================================================================

def demo_variables():
    name = "Santosh"
    age = 30
    pi = 3.14
    is_active = True    # bool: True/False — not true/false like Java

    x, y, z = 1, 2, 3  # multiple assignment — no Java equivalent

    console.print(f"[bold]1. Variables & Types[/bold]")
    console.print(f"   str={type(name).__name__}, int={type(age).__name__}, "
                  f"float={type(pi).__name__}, bool={type(is_active).__name__}")
    console.print(f"   len('{name}') = {len(name)}")
    console.print(f"   x={x}, y={y}, z={z}")


# =============================================================================
# 2. F-STRINGS & STRING METHODS
# =============================================================================

def demo_strings():
    name = "shreyanvi"
    age = 0.4

    console.print(f"\n[bold]2. F-Strings & String Methods[/bold]")
    # f-string (Python 3.6+) — Java: "Hello " + name + ", age: " + age
    console.print(f"   Hello {name.capitalize()}, age: {age}")
    console.print(f"   upper: {name.upper()} | lower: {name.lower()}")
    console.print(f"   expression inside {{}}: next year = {age + 1}")


# =============================================================================
# 3. ARITHMETIC & UNIT CONVERSIONS
# =============================================================================

def demo_arithmetic():
    console.print(f"\n[bold]3. Arithmetic Operators[/bold]")
    console.print(f"   2 * 10  = {2 * 10}")
    console.print(f"   20 // 3 = {20 // 3}  (integer division)")
    console.print(f"   2 ** 10 = {2 ** 10}  (exponentiation)")
    console.print(f"   20 % 3  = {20 % 3}   (modulo / remainder)")


def demo_unit_conversions():
    console.print(f"\n[bold]4. Unit Conversions[/bold]")
    console.print(f"   6 ft        → {6 * 0.3048:.2f} m")
    console.print(f"   10 km       → {10 / 1.609:.2f} miles")
    console.print(f"   82°F        → {(82 - 32) * 5/9:.1f}°C")
    console.print(f"   30°C        → {(30 * 9/5) + 32:.1f}°F")
    console.print(f"   145 lbs     → {145 * 0.453592:.2f} kg")
    console.print(f"   8 fl oz     → {8 * 29.5735:.1f} ml")


# =============================================================================
# 5. LISTS
# =============================================================================

def demo_lists():
    friends = ["Tommy", "Isabel", "Daniel", "Sophie"]

    console.print(f"\n[bold]5. Lists[/bold]")
    console.print(f"   {friends}")
    console.print(f"   first: {friends[0]} | last: {friends[-1]} | count: {len(friends)}")
    console.print(f"   slice [1:3]: {friends[1:3]}")

    for i, friend in enumerate(friends):
        console.print(f"   [{i}] Hello {friend}!")

    # List comprehension — compact alternative to a for-loop with append
    nums = [1, 2, 3]
    multiplied = [n * 5 for n in nums]
    console.print(f"   {nums} × 5 = {multiplied}")
    console.print(f"   unpacked: {' | '.join(str(n) for n in multiplied)}")


# =============================================================================
# 6. DICTIONARIES
# =============================================================================

def demo_dicts():
    person = {
        "name": "Santosh",
        "age": 30,
        "city": "New York",
        "tasks": ["eating", "task2", "task3"],
        "subArea": {"village": "nyc-b1"}
    }
    person["area"] = "bronx"    # add key after creation

    console.print(f"\n[bold]6. Dictionaries[/bold]")
    console.print(f"   {person['name']}, {person['age']}y, {person['city']} ({person['area']})")
    console.print(f"   missing key fallback: {person.get('location', 'Unknown')}")
    console.print(f"   keys:   {list(person.keys())}")
    console.print(f"   nested: subArea.village = {person['subArea']['village']}")

    for key, val in person.items():
        console.print(f"   {key}: {val}")


# =============================================================================
# 7. NESTED DATA & FILTERING
# =============================================================================

def demo_nested_data():
    fruit_catalog = {
        "Citrus": [
            {"name": "Orange", "description": "Juicy, rich in vitamin C."},
            {"name": "Lemon",  "description": "Tart, commonly used to flavor dishes."}
        ],
        "Berries": [
            {"name": "Strawberry", "description": "Sweet red fruit, great for desserts."},
            {"name": "Blueberry",  "description": "Small blue fruit, packed with antioxidants."}
        ],
        "Tropical": [
            {"name": "Mango",     "description": "Sweet and juicy, unique tropical flavor."},
            {"name": "Pineapple", "description": "Tangy-sweet, great fresh or in dishes."}
        ]
    }

    # Build markdown string and render with Rich
    md_text = "# Fruit Catalog\n\n"
    for category, fruits in fruit_catalog.items():
        md_text += f"## {category}\n"
        for fruit in fruits:
            md_text += f"- **{fruit['name']}**: {fruit['description']}\n"

    console.print(f"\n[bold]7. Nested Data & Rich Markdown[/bold]")
    console.print(Markdown(md_text))

    # List comprehension to filter — cleaner than building reminder_list with append
    employees = [
        {"name": "Alice",   "task_completed": True},
        {"name": "Bob",     "task_completed": False},
        {"name": "Charlie", "task_completed": True},
        {"name": "Diana",   "task_completed": False}
    ]
    pending = [e["name"] for e in employees if not e["task_completed"]]
    console.print(f"   Send reminder to: {pending}")


# =============================================================================
# 8. FUNCTIONS
# =============================================================================

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9

def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32

def demo_functions():
    console.print(f"\n[bold]8. Functions[/bold]")
    console.print(f"   100°F = {fahrenheit_to_celsius(100):.1f}°C")
    for c in [0, 100, 13]:
        console.print(f"   {c:>3}°C = {celsius_to_fahrenheit(c):.0f}°F")


# =============================================================================
# 9. MATH & STATISTICS
# =============================================================================

def demo_statistics():
    console.print(f"\n[bold]9. Math & Statistics[/bold]")

    console.print(f"   floor(5.7)={floor(5.7)}  floor(5.9)={floor(5.9)}")
    console.print(f"   ceil(5.2)={ceil(5.2)}   ceil(5.5)={ceil(5.5)}")

    heights = [160, 172, 155, 180, 165, 170, 158, 182, 175, 168]
    console.print(f"   heights avg: {mean(heights):.2f} cm")

    scores_with_repeats = [70, 80, 80, 90, 70, 80, 60]
    console.print(f"   scores {scores_with_repeats}")
    console.print(f"     mean={mean(scores_with_repeats)}, "
                  f"median={median(scores_with_repeats)}, "
                  f"mode={mode(scores_with_repeats)}")

    # Median is more representative than mean when outliers exist
    salaries = [40_000, 45_000, 50_000, 55_000, 1_000_000]
    console.print(f"   salaries (1 outlier): mean=${mean(salaries):,.0f}  "
                  f"median=${median(salaries):,.0f}  ← median more honest")

    numbers = list(range(1, 11))
    console.print(f"   random 5 from 1–10: {sample(numbers, 5)}")


# =============================================================================
# 10. FILE HANDLING
# =============================================================================

def demo_file_handling():
    # Write files relative to this script so paths work on any machine
    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    filepath = output_dir / "demo.txt"

    console.print(f"\n[bold]10. File Handling[/bold]")

    with open(filepath, "w") as f:
        f.write("Hello, this is a demo file.\n")
        f.write("Python uses 'with' to auto-close files — no manual f.close() needed.\n")

    with open(filepath, "r") as f:
        content = f.read()

    console.print(Markdown(f"**Written to:** `{filepath}`\n\n```\n{content}```"))


# =============================================================================
# ENTRY POINT — run all demos
# =============================================================================

if __name__ == "__main__":
    demo_variables()
    demo_strings()
    demo_arithmetic()
    demo_unit_conversions()
    demo_lists()
    demo_dicts()
    demo_nested_data()
    demo_functions()
    demo_statistics()
    demo_file_handling()
