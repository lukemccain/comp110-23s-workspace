"""Dictionary Functions."""

__author__ = "730486310"


def invert(inp_d: dict[str, str]) -> dict[str, str]:
    """Return a dictionary that inverts the keys and values."""
    ret_dict: dict[str, str] = {}
    counter_d: dict[str, int] = {}
    for key in inp_d:
        ret_dict[inp_d[key]] = key
        if inp_d[key] in counter_d:
            counter_d[inp_d[key]] += 1
        else:
            counter_d[inp_d[key]] = 0
        if counter_d[inp_d[key]] > 0:
            raise KeyError("Cannot have two of the same keys in dictionary.")
    return ret_dict


def favorite_color(old_d: dict[str, str]) -> str:
    """Returns string of the color from input dictionary that occurs the most."""
    final_color: str
    new_d: dict[str, int] = {}
    for name in old_d:
        color: str = old_d[name]
        if color in new_d:
            new_d[color] += 1
        else:
            new_d[color] = 1
    max: int = 0
    for color in new_d:
        if new_d[color] > max:
            max = new_d[color]
            final_color = color
    return final_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Returns a dictionary where keys are strings from list and values are the number of times each string appears in the list."""
    new_d: dict[str, int] = {}
    for word in inp_list:
        if word in new_d:
            new_d[word] += 1
        else:
            new_d[word] = 1
    return new_d