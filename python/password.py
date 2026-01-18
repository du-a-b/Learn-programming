import os
import string
import secrets
import random
from typing import Dict, Tuple, List

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def parse_choices(user_wants: str) -> Dict[str, bool]:
    """Return a dict of which categories the user selected."""
    wants = {
        "lowercase": '1' in user_wants,
        "uppercase": '2' in user_wants,
        "digits":    '3' in user_wants,
        "symbols":   '4' in user_wants,
        "everything":'5' in user_wants,
    }
    return wants

def build_pools() -> Dict[str, str]:
    """Return mapping from category name to characters."""
    return {
        "lowercase": string.ascii_lowercase,
        "uppercase": string.ascii_uppercase,
        "digits":    string.digits,
        "symbols":   string.punctuation,
        "everything": string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
    }

def get_user_length(min_length: int, max_length: int = 1024) -> int:
    """Prompt user for password length with validation."""
    while True:
        val = input(f"How long should the password be? (min {min_length}, max {max_length}): ").strip()
        try:
            length = int(val)
            if length < min_length:
                print(f"Password length must be at least {min_length}.")
                continue
            if length > max_length:
                print(f"Password length must be at most {max_length}.")
                continue
            return length
        except ValueError:
            print("Please enter a valid integer.")

def generate_password(length: int, selected_pools: List[str], pools_map: Dict[str, str]) -> str:
    """
    Generate a password with:
    - at least one character from each selected pool
    - the remainder chosen from the combined pool
    Uses secrets for cryptographic randomness.
    """
    if not selected_pools:
        raise ValueError("No character categories selected.")

    # Ensure at least one char from each selected category
    password_chars: List[str] = []
    for name in selected_pools:
        chars = pools_map[name]
        password_chars.append(secrets.choice(chars))

    if length < len(password_chars):
        raise ValueError(f"Length {length} is too short for the {len(password_chars)} selected categories.")

    # Build combined pool
    combined = "".join(pools_map[name] for name in selected_pools)
    # Fill the rest
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(combined))

    # Shuffle securely
    rand = random.SystemRandom()
    rand.shuffle(password_chars)

    return "".join(password_chars)

def main():
    pools_map = build_pools()

    clear_screen()
    print("\n" + "=" * 40)
    print("  PASSWORD GENERATOR")
    print("=" * 40 + "\n")

    print("Select character types (e.g., '13' for lowercase + digits):\n")
    print("  [1] Lowercase")
    print("  [2] Uppercase")
    print("  [3] Digits")
    print("  [4] Symbols")
    print("  [5] Everything\n")

    user_wants = input("Enter your choice(s): ").strip()
    choices = parse_choices(user_wants)

    # Interpret choices into a list of pool keys
    selected_pools: List[str] = []
    if choices["everything"]:
        # If user chose 'everything', treat it as the only selected pool
        selected_pools = ["everything"]
    else:
        if choices["lowercase"]:
            selected_pools.append("lowercase")
        if choices["uppercase"]:
            selected_pools.append("uppercase")
        if choices["digits"]:
            selected_pools.append("digits")
        if choices["symbols"]:
            selected_pools.append("symbols")

    if not selected_pools:
        print("\nNo valid character categories selected. Exiting.")
        return

    print(f"\nYou selected: {user_wants}")
    print("Awesome choice!\n")

    length = get_user_length(min_length=len(selected_pools))

    try:
        password = generate_password(length, selected_pools, pools_map)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print("\n" + "-" * 40)
    print(f"Your password: {password}")
    print("-" * 40 + "\n")

if __name__ == "__main__":
    main()
