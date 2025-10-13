import itertools
import string
import time

def common_guess(password :str, filename = "passwords.txt"):
    try:
        with open(filename, "r", encoding= "utf-8") as file:
            password_list = file.read().splitlines()

    except FileNotFoundError:
        print("file does not exist!")
        return None
    
    for i, match in enumerate(password_list, start=1):
        if match == password:
            return f"Common match: {match} (#{i})"
        
def brute_force(word: str, length: int, digits: False, Symbols: False) -> str | None:
    # performs brute force action on finding a word

    #modify this tool for total symbols

    chars : str = string.ascii_lowercase

    if digits:
        chars += string.digits

    if Symbols:
        chars += string.punctuation

    attempts: int = 0
    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        guess :str = "".join(guess)

        if guess == word:
            return f"{word} was cracked in {attempts:,} attempts"
        
def main():
    print("Searching...")
    input_password = input("Please Enter your password( 5 word for now) to be cracked: ")

    start_time = time.perf_counter()

    if common_password := common_guess(input_password):
        print(common_password)

    else:
        if cracked := brute_force(input_password, length= 5, digits= True, Symbols= False):
            print(cracked)

        else:
            print("We could not crack it!")

    end_time = time.perf_counter()

    print(round(end_time - start_time, 2), "s")


if __name__ == "__main__":
    main()