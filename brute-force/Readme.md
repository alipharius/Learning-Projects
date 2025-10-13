# Brute-Force Password Cracker

> A simple Python script that tries to “crack” a given password by first checking a common password list, then using brute-force combinations.

## What This Does

This program checks if a password appears in a list of common passwords and, if not, attempts to find it by trying every possible combination of characters (letters, digits, and optional symbols).

## Why I Built This

- To learn about brute-force algorithms and iteration with itertools

- To practice file handling and error handling in Python

- Because I was curious about how password cracking tools work on a small scale

## Quick Start
```bash
cd [project-folder]
python main.py
```


Make sure you have a passwords.txt file in the same directory, containing one common password per line (e.g. 123456, password, qwerty, etc.).

## Features

- Checks against a common password list before brute-forcing

- Supports lowercase letters and digits (symbols optional)

- Displays how many attempts and how long the cracking took

- Handles missing password files gracefully

## What I Learned

- How to use itertools.product() to generate all combinations of characters

- How to read and handle files safely using with open()

- How to measure execution time with time.perf_counter()

- How to structure a main function and use the walrus operator (:=)

## Notes / Future Improvements

- Add adjustable password length (currently fixed at 5 characters)

- Add option to include uppercase letters or custom character sets

- Display progress updates or estimated time remaining

- Add a more efficient search strategy (e.g., dictionary-based or pattern-based)

Built as part of my learning journey
