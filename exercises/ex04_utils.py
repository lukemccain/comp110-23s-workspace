"""Practice with Lists."""

__author__ = "730486310"


def all(list_of_int: list[int], given_int: int) -> bool:
    i: int = 0
    while i < len(list_of_int):
        if given_int == list_of_int[i]:
            i += 1
        else:
            if list_of_int == list():
                return False
            return False
    return True

    
int_list_for_all: list[int] = [1,1,1]
integer_for_all: int = 1
print(all(int_list_for_all, integer_for_all))

def max(list_of_int: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    i: int = 0
    idx: int = 0
    max: int = 0
    while i < len(list_of_int):
        if list_of_int[i] >= list_of_int[idx]:
            max == list_of_int[i]
        else:
            idx += 1
        i += 1
    return max

integer_list_for_max: list[int] = [1,3,2]
print(max(integer_list_for_max))


def is_equal(list_of_int: list[int], second_list_of_int: list[int]) -> bool:
    i: int = 0
    while i < len(list_of_int) and i < len(second_list_of_int):
        if list_of_int[i] == second_list_of_int[i]:
            i += 1
        else:
            return False
    return True

int_list_for_is_equal: list[int] = [1,0,1]
second_list_of_int_for_is_equal: list[int] = [1,0,1]
print(is_equal(int_list_for_is_equal, second_list_of_int_for_is_equal))