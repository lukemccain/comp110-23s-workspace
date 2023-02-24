"""Real Wordle."""

__author__ = "730486310"


def contains_char(word_being_searched: str, character_being_searched_for: str) -> bool:
    """Searching for character in any index of the given word."""
    assert len(character_being_searched_for) == 1
    i: int = 0
    while i < len(word_being_searched):
        if character_being_searched_for == word_being_searched[i]:
            return True
        i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given two strings of equal length, a green, yellow, or white box will appear based on the guess/secret, like in Wordle."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    s: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            s = s + GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                s = s + YELLOW_BOX
            else:
                s = s + WHITE_BOX
        i = i + 1
    return s


def input_guess(expected_length: int) -> str:
    """User will be prompted to insert a word of the correct character length, until successful."""
    word: str = input(f"Enter a {expected_length} character word: ")
    if len(word) == expected_length:
        return word
    while expected_length != len(word):
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word
        

def main() -> None:
    """The entry point of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    success: bool = False
    while turns < 7 and not success:
        print(f"=== Turn {turns}/6 ===")
        guess: str = (input_guess(5))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turns}/6 turns!")
            success = True
        else:
            turns = turns + 1
            success = False
    if turns == 7 and not success:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()