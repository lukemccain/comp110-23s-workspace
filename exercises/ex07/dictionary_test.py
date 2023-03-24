"""Dictionary Testing."""

__author__ = "730486310"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Should return a dictionary that inverts the keys and values."""
    test_d: dict[str, str] = {}
    assert invert(test_d) == {}


def test_invert_with_letters() -> None:
    """Should return a dictionary that inverts the keys and values."""
    test_d: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(test_d) == {"b": "a", "d": "c", "f": "e"}


def test_invert_with_words() -> None:
    """Should return a dictionary that inverts the keys and values."""
    test_d: dict[str, str] = {"michael": "jordan", "lebron": "james"}
    assert invert(test_d) == {"jordan": "michael", "james": "lebron"}


def test_favorite_color_one_color() -> None:
    """Should return the color that occurs the most in a dictionary."""
    test_d: dict[str, str] = {"Luke": "blue"}
    assert favorite_color(test_d) == "blue"


def test_favorite_color_with_many_names_and_colors() -> None:
    """Should return the color that occurs the most in a dictionary."""
    test_d: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_d) == "blue"


def test_favorite_color_with_two_colors_tying() -> None:
    """Should return the color that occurs the most in a dictionary."""
    test_d: dict[str, str] = {"Luke": "blue", "Hudson": "orange", "Dalton": "blue", "Terence": "orange"}
    assert favorite_color(test_d) == "blue"


def test_count_one_word() -> None:
    """Should return a dictionary where keys are strings found in input list and values are the number of times that string occurs."""
    test_l: list[str] = ["hello"]
    assert count(test_l) == {"hello": 1}


def test_count_one_word_occuring_more() -> None:
    """Should return a dictionary where keys are strings found in input list and values are the number of times that string occurs."""
    test_l: list[str] = ["hello", "my", "name", "is", "Luke", "hello"]
    assert count(test_l) == {"hello": 2, "my": 1, "name": 1, "is": 1, "Luke": 1}


def test_count_with_many_words_occuring_more() -> None:
    """Should return a dictionary where keys are strings found in input list and values are the number of times that string occurs."""
    test_l: list[str] = ["chicken", "leg", "chicken", "leg", "piece"]
    assert count(test_l) == {"chicken": 2, "leg": 2, "piece": 1}