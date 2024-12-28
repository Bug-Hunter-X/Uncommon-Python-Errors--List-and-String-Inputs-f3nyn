# Uncommon Python Errors

This repository demonstrates some less common errors that can arise in Python due to unexpected input types. The primary example involves a function that gracefully handles ZeroDivisionError and TypeError, but exposes vulnerabilities when lists or strings are supplied where numeric inputs are anticipated.

## Issues Addressed

- **Unexpected input types:** The code highlights issues that occur when unexpected data types (like lists or strings) are fed to a function designed for numeric operations.
- **Robust error handling:** The included solution provides a more robust way to handle the uncommon errors shown in the `bug.py` example.

## How to Run

1. Clone this repository.
2. Run `bug.py` to observe the errors.
3. Compare its output to the results of running `bugSolution.py`, which shows improved error handling.