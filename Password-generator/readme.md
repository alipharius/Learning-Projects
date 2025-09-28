# Password-generator

A secure password generator written in Python using the `secrets` module.

## Features

- Generate random passwords with letters, numbers, symbols.
- Include or exclude uppercase letters.
- Include or exclude symbols.
- Generate multiple passwords at once.
- Command-line interface (CLI) with short and long flags.

## Usage

```bash
# Generate 1 password of length 16 with symbols and uppercase letters
python password_generator.py -l 16 -s -u

# Generate 3 passwords of length 12 without symbols
python password_generator.py -l 12 --count 3 --no-symbols
```
## Flags

Flag	Description:

| Flag            | Description                         |
|-----------------|-------------------------------------|
| `-l, --length`  | Length of the password (default: 10)|
| `-c, --count`   | Number of passwords (default: 1)    |
| `-s, --symbols` | Include symbols                     |
| `--no-symbols`  | Exclude symbols                     |
| `-u, --uppercase` | Include uppercase letters         |
| `--no-uppercase` | Exclude uppercase letters          |


## Testing
This project includes unit tests to ensure that all functions behave correctly.

Install pytest
If you don’t already have pytest installed:

`pip install pytest`

Run the tests
From the root of the project folder, run:

`pytest`

You should see output like:

============================= test session starts =============================

collected 7 items

tests/test_password_generator.py .......                                 [100%]

============================== 7 passed in 0.05s ==============================

What’s Tested:
- contains_upper() function

- contains_symbols() function

- generate_password() length and character type behavior

- Passwords generated with or without symbols/uppercase letters
