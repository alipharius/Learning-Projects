import string
import secrets

def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
        
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
        
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)

    new_password = ''

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]
    return new_password


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate secure passwords with Python's secrets module"
    )

    parser.add_argument(
        "-l", "--length",
        type=int,
        default=10,
        help="Length of the password (default: 10)"
    )

    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)"
    )

    
    symbols_group = parser.add_mutually_exclusive_group()
    symbols_group.add_argument(
        "-s", "--symbols",
        action="store_true",
        help="Include symbols in the password"
    )
    symbols_group.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclude symbols from the password"
    )

    uppercase_group = parser.add_mutually_exclusive_group()
    uppercase_group.add_argument(
        "-u", "--uppercase",
        action="store_true",
        help="Include uppercase letters in the password"
    )
    uppercase_group.add_argument(
        "--no-uppercase",
        action="store_true",
        help="Exclude uppercase letters from the password"
    )

    args = parser.parse_args()

    
    use_symbols = args.symbols and not args.no_symbols
    use_uppercase = args.uppercase and not args.no_uppercase

    for i in range(args.count):
        new_pass = generate_password(
            length=args.length,
            symbols=use_symbols,
            uppercase=use_uppercase
        )
        specs = f"Uppercase: {contains_upper(new_pass)} , Symbols: {contains_symbols(new_pass)}"
        print(f"{i+1} -> \"{new_pass}\" ({specs})")

