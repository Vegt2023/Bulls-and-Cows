import random


INTRO = """Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------"""


def print_intro() -> None:
    """Print the game intro text."""
    print(INTRO)


def generate_secret(length: int = 4) -> str:
    """Generate a random secret number with unique digits, not starting with zero."""
    first = random.choice("123456789")
    remaining_pool = [d for d in "0123456789" if d != first]
    rest = random.sample(remaining_pool, k=length - 1)
    return first + "".join(rest)


def validate_guess(guess: str, length: int = 4) -> tuple[bool, str]:
    """Validate user input according to Bulls & Cows rules."""
    if len(guess) != length:
        return False, f"Invalid length: expected {length} digits."
    if not guess.isdigit():
        return False, "Invalid input: use digits only."
    if guess[0] == "0":
        return False, "Invalid number: must not start with zero."
    if len(set(guess)) != length:
        return False, "Invalid number: digits must be unique (no duplicates)."
    return True, ""


def count_bulls_cows(secret: str, guess: str) -> tuple[int, int]:
    """Return (bulls, cows) for a guess compared to secret."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    # Since digits are unique, cows = common digits - bulls
    common = sum(ch in secret for ch in guess)
    cows = common - bulls
    return bulls, cows


def plural(n: int, singular: str, plural_word: str | None = None) -> str:
    """Return correctly pluralized word for English output."""
    word = singular if n == 1 else (plural_word or f"{singular}s")
    return f"{n} {word}"


def play_round() -> int:
    """Play one round and return number of guesses."""
    secret = generate_secret()
    guesses = 0

    while True:
        tip = input(">>> ").strip()
        
        # DEV
        if tip == "__dev__":
            print(f"[DEV] Secret number is: {secret}")
            continue

        ok, msg = validate_guess(tip)

        if not ok:
            print(msg)
            continue

        guesses += 1
        bulls, cows = count_bulls_cows(secret, tip)

        if tip == secret:
            print("Correct, you've guessed the right number")
            print(f"in {guesses} guesses!")
            print("-----------------------------------------------")
            print("That's amazing!")
            return guesses

        print(f"{plural(bulls, 'bull')}, {plural(cows, 'cow')}")
        print("-----------------------------------------------")



def main() -> None:
    """Main entry point. Stores game statistics."""
    stats: list[int] = []

    while True:
        print_intro()
        guesses = play_round()
        stats.append(guesses)

        print("-----------------------------------------------")
        print("Game statistics:")
        for i, g in enumerate(stats, start=1):
            print(f"Game {i}: {g} guesses")
        avg = sum(stats) / len(stats)
        print(f"Average guesses: {avg:.2f}")

        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            break


main()
