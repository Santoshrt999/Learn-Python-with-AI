"""
Python Playground - Simple and Famous Programs
@author: Santosh Goteti

This module contains various Python programs covering different skills
and concepts. Includes basic programs, mathematical operations, string
manipulation, and interactive programs.
"""

# ============================================================================
# 1. FIBONACCI SERIES
# ============================================================================
def fibonacci_series(n):
    """Generate Fibonacci series up to n terms"""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

n = 10
print("1. Fibonacci series:")
print(fibonacci_series(n))

# ============================================================================
# 2. FACTORIAL
# ============================================================================
def factorial(num):
    """Calculate factorial of a number recursively"""
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
print("\n2. Factorial of 5:", factorial(5))

# ============================================================================
# 3. PRIME NUMBER CHECK
# ============================================================================
def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print("\n3. Prime numbers between 1 and 20:")
primes = [x for x in range(1, 21) if is_prime(x)]
print(primes)

# ============================================================================
# 4. PALINDROME CHECK
# ============================================================================
def is_palindrome(s):
    """Check if a string is a palindrome"""
    s = s.replace(" ", "").lower()
    return s == s[::-1]

print("\n4. Palindrome Check:")
print("'racecar' is palindrome:", is_palindrome("racecar"))
print("'hello' is palindrome:", is_palindrome("hello"))

# ============================================================================
# 5. ARMSTRONG NUMBER
# ============================================================================
def is_armstrong(num):
    """Check if a number is an Armstrong number"""
    digits = len(str(num))
    sum_of_powers = sum(int(digit)**digits for digit in str(num))
    return sum_of_powers == num

print("\n5. Armstrong Numbers between 1 and 1000:")
armstrong_nums = [x for x in range(1, 1001) if is_armstrong(x)]
print(armstrong_nums)

# ============================================================================
# 6. REVERSE A STRING
# ============================================================================
def reverse_string(s):
    """Reverse a string"""
    #explain this
    # s[::-1] uses slicing to reverse the string
    return s[::-1]
print("\n6. Reverse String:")
print("'Python' reversed:", reverse_string("Python"))

# ============================================================================
# 7. SUM OF DIGITS
# ============================================================================
def sum_of_digits(num):
    """Calculate sum of all digits in a number"""
    return sum(int(digit) for digit in str(abs(num)))

print("\n7. Sum of digits in 12345:", sum_of_digits(12345))

# ============================================================================
# 8. GREATEST COMMON DIVISOR (GCD)
# ============================================================================
def gcd(a, b):
    """Find GCD using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

print("\n8. GCD of 48 and 18:", gcd(48, 18))

# ============================================================================
# 9. LEAST COMMON MULTIPLE (LCM)
# ============================================================================
def lcm(a, b):
    """Calculate LCM of two numbers"""
    return (a * b) // gcd(a, b)

print("\n9. LCM of 12 and 18:", lcm(12, 18))

# ============================================================================
# 10. BUBBLE SORT
# ============================================================================
def bubble_sort(arr):
    """Sort array using bubble sort algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("\n10. Bubble Sort:")
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# ============================================================================
# 11. BINARY SEARCH
# ============================================================================
def binary_search(arr, target):
    """Find target in sorted array using binary search"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("\n11. Binary Search (find 25 in [11, 12, 22, 25, 34, 64, 90]):")
print("Index:", binary_search([11, 12, 22, 25, 34, 64, 90], 25))

# ============================================================================
# 12. INTERACTIVE: CALCULATOR
# ============================================================================
def interactive_calculator():
    """Simple interactive calculator"""
    print("\n12. INTERACTIVE CALCULATOR")
    print("Operations: +, -, *, /, %")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation: ")
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero")
        elif op == '%':
            print(f"Result: {num1 % num2}" if num2 != 0 else "Error: Modulo by zero")
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input")

# Uncomment to run interactive calculator
# interactive_calculator()

# ============================================================================
# 13. INTERACTIVE: NUMBER GUESSING GAME
# ============================================================================
def guessing_game():
    """Interactive number guessing game"""
    import random
    print("\n13. INTERACTIVE NUMBER GUESSING GAME")
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1
            
            if guess < secret:
                print("Too low, try again!")
            elif guess > secret:
                print("Too high, try again!")
            else:
                print(f"Correct! You guessed in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number")

# Uncomment to run guessing game
# guessing_game()

# ============================================================================
# 14. FACTORIAL USING ITERATION
# ============================================================================
def factorial_iterative(num):
    """Calculate factorial using iteration"""
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result

print("\n14. Factorial of 6 (iterative):", factorial_iterative(6))

# ============================================================================
# 15. POWER FUNCTION
# ============================================================================
def power(base, exp):
    """Calculate base raised to exponent"""
    if exp == 0:
        return 1
    result = 1
    for _ in range(exp):
        result *= base
    return result

print("\n15. 2 raised to power 8:", power(2, 8))

# ============================================================================
# 16. MULTIPLICATION TABLE
# ============================================================================
def multiplication_table(num):
    """Generate multiplication table for a number"""
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

print("\n16. Multiplication table of 5:")
multiplication_table(5)

# ============================================================================
# 17. VOWEL COUNTER
# ============================================================================
def count_vowels(s):
    """Count vowels in a string"""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print("\n17. Vowels in 'Python Programming':", count_vowels("Python Programming"))

# ============================================================================
# 18. DUPLICATE REMOVER
# ============================================================================

def remove_duplicates(lst):
    """Remove dupes while preserving order"""
    visited = set()
    final_List=[]
    for num in lst:
        if num not in visited:
            visited.add(num)
            final_List.append(num)
    return final_List

lst = [1, 2, 2, 3, 3, 4, 5, 5]
print(f"\n18. Remove duplicates from {lst}:")
print(f"final list is {remove_duplicates(lst)}")

# ============================================================================
# 19. LIST FLATTENER
# ============================================================================
def flatten_list(lst):
    """Flatten a nested list"""
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

print("\n19. Flatten [[1,2],[3,[4,5]],6]:")
print(flatten_list([[1, 2], [3, [4, 5]], 6]))

# ============================================================================
# 20. ANAGRAM CHECK
# ============================================================================
def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print("\n20. Anagram Check:")
print("'listen' and 'silent' are anagrams:", is_anagram("listen", "silent"))

# ============================================================================
# 21. AI-POWERED FUN PROBLEM
# ============================================================================
def generate_ai_engine():
    """Generate a simple AI engine that powers the riddle game."""
    return {
        "name": "Simple Riddle AI",
        "version": "1.0",
        "riddle": {
            "question": "I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?",
            "answer": "echo",
            "prompt": "Your answer: "
        }
    }

def ai_riddle_game(ai_engine=None):
    """Interactive AI-powered riddle game that prompts the user and validates the answer."""
    riddle = "I speak without a mouth and hear without ears. I have nobody, but I come alive with wind. What am I?"
    answer = "echo"
    print("\n21. AI-Powered Riddle Game:")
    print("Riddle:", riddle)
    guess = input("Your answer: ").strip().lower()
    if guess == answer:
        print("Correct! The answer is echo.")
    else:
        print("Not quite. The answer is echo.")

ai_riddle_game()









