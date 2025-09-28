# Password Generator

A secure password generator written in Python using the `secrets` module.

## Features

- Generate random passwords with letters, numbers, symbols.
- Include or exclude uppercase letters.
- Include or exclude symbols.
- Generate multiple passwords at once.
- Command-line interface (CLI) with short and long flags.

## Usage

```bash
# generate 1 password of length 16 with symbols and uppercase letters
python password_generator.py -l 16 -s -u

# generate 3 passwords of length 12 without symbols
python password_generator.py -l 12 --count 3 --no-symbols

| Flag            | Description                         |
|-----------------|-------------------------------------|
| `-l, --length`  | Length of the password (default: 10)|
| `-c, --count`   | Number of passwords (default: 1)    |
| `-s, --symbols` | Include symbols                     |
| `--no-symbols`  | Exclude symbols                     |
| `-u, --uppercase` | Include uppercase letters         |
| `--no-uppercase` | Exclude uppercase letters          |

