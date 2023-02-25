"""Practice with Lists."""

__author__ = "730486310"


def all(input: list[int], integer: int) -> bool:
    """Testing if all integers in list are equal to the given int."""
    i: int = 0
    while i < len(input):
        if integer == input[i]:
            i += 1
        else:
            return False
        if input == list():
            return False
    return True


def max(input: list[int]) -> int:
    """Trying to find the max int in a list of int."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = input[i]
    counter: int = 1
    while i < len(input):
        if input[counter] > max:
            max == input[counter]
        i += 1
    return max


def is_equal(list_of_int: list[int], second_list_of_int: list[int]) -> bool:
    """Testing if every int at every index is equal to eachother."""
    i: int = 0
    while i < len(list_of_int) and i < len(second_list_of_int):
        if list_of_int[i] == second_list_of_int[i]:
            i += 1
        else:
            return False
    if len(list_of_int) != len(second_list_of_int):
        return False
    if list_of_int == list() or second_list_of_int == list():
        return False
    if list_of_int == list() and second_list_of_int == list():
        return False
    return True