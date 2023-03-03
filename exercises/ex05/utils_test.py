"""Unit Testing."""

__author__ = "730486310"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Should return only even values in a list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_many_items() -> None:
    """Should return only even values in a list."""
    test_list: list[int] = [1, 2, 3, 4]
    assert only_evens(test_list) == [2, 4]


def test_only_evens_many_items_with_negatives() -> None:
    """Should return only even values in a list."""
    test_list: list[int] = [-2, -1, 0, 1, 2]
    assert only_evens(test_list) == [-2, 0, 2]


def test_sub_empty() -> None:
    """Should return subset list starting at start index and ending/excluding last index."""
    test_list: list[int] = []
    test_first_index: int = 2
    test_last_index: int = 4
    assert sub(test_list, test_first_index, test_last_index) == []


def test_sub_many_items() -> None:
    """Should return subset list starting at start index and ending/excluding last index."""
    test_list: list[int] = [10, 20, 30, 40]
    test_first_index: int = 1
    test_last_index: int = 3
    assert sub(test_list, test_first_index, test_last_index) == [20, 30]


def test_sub_many_items_with_negatives() -> None:
    """Should return subset list starting at start index and ending/excluding last index."""
    test_list: list[int] = [-20, -10, 0, 10, 20]
    test_first_index: int = 0
    test_last_index: int = 4
    assert sub(test_list, test_first_index, test_last_index) == [-20, -10, 0, 10]


def test_concat_empty() -> None:
    """Given two list, we should expect to return a third list, containing all elements in the first and second list, respectively."""
    test_list1: list[int] = []
    test_list2: list[int] = []
    assert concat(test_list1, test_list2) == []


def test_concat_many_items() -> None:
    """Given two list, we should expect to return a third list, containing all elements in the first and second list, respectively."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4, 5, 6]


def test_concat_many_items_with_negatives() -> None:
    """Given two list, we should expect to return a third list, containing all elements in the first and second list, respectively."""
    test_list1: list[int] = [-3, -2, -1]
    test_list2: list[int] = [1, 2, 3]
    assert concat(test_list1, test_list2) == [-3, -2, -1, 1, 2, 3]