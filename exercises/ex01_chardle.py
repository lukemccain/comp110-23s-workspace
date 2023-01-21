"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730486310"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    exit(print("Error: Word must contain 5 characters"))
character: str = input("Enter a single character: ")
if len(character) != 1:
    exit(print("Error: Character must be a single character."))
matches: int = 0

print("Searching for " + character + " in " + word)

if character == word[0]:
    matches = matches + 1
    print(character + " found at index 0")
if character == word[1]:
    matches = matches + 1
    print(character + " found at index 1")
if character == word[2]:
    matches = matches + 1
    print(character + " found at index 2")
if character == word[3]:
    matches = matches + 1
    print(character + " found at index 3")
if character == word[4]:
    matches = matches + 1
    print(character + " found at index 4")

if matches == 0:
    print("No instances of " + character + " found in " + word)
if matches == 1:
    print("1 instance of " + character + " found in " + word)
if matches == 2:
    print("2 instances of " + character + " found in " + word)
if matches == 3:
    print("3 instances of " + character + " found in " + word)
if matches == 4:
    print("4 instances of " + character + " found in " + word)
if matches == 5:
    print("5 instances of " + character + " found in " + word)