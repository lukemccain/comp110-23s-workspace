"""The Game of Wordle."""

__author__ = "730486310"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
s: str = ""


while len(guess) != 6:
    guess: str = input("That was not 6 letters! Try again: ")

while i < len(secret_word):
    if guess[i] == secret_word[i]:
        s = s + GREEN_BOX
    else:
        character_exists: bool = False
        alternate: int = 0
        while not character_exists and alternate < len(secret_word):
            if guess[i] == secret_word[alternate]:
                character_exists: bool = True
                s = s + YELLOW_BOX
            else:
                alternate = alternate + 1
        if character_exists == False:
            s = s + WHITE_BOX
    i = i + 1
print(s)
if len(guess) == 6:
    if guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")