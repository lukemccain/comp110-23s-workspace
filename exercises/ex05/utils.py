"""Functions that will be tested."""

__author__ = "730486310"

def only_evens(evens: list[int]) -> list[int]:
    """Should only return even numbers in a list."""
    i: int = 0
    even_numbers: list[int] = []
    while i < len(evens):
        if evens[i] % 2 == 0:
            even_numbers.append(evens[i])
        i += 1
    return even_numbers


def concat(first: list[int], second: list[int]) -> list[int]:
    """Given two lists, we should generate a new list containing all elements of first, followed by second."""
    i: int = 0
    final: list[int] = []
    while i < len(first):
        final.append(first[i])
        i += 1
    i = 0
    while i < len(second):
        final.append(second[i])
        i += 1
    return final


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Should generate a subset list from original list containing only numbers from starting index and end index (not inclusive)."""
    final: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(a_list):
        end_index = len(a_list)
    if len(a_list) == 0 or start_index >= len(a_list) or end_index <= 0:
        return []
    while start_index < end_index:
        final.append(a_list[start_index])
        start_index += 1
    return final