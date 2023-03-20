"""Challenge question 4."""


def zip(x: list[str], y: list[int]) -> dict[str,int]:
    """Produce a dictionary where the keys are the items of the first list and the values are the corresponding items at same idx of second list."""
    if len(x) != len(y):
        return {}
    if x == [] or y == []:
        return {}
    dictionary: dict[str, int] = {}
    for idx in range(0,len(x)):
        dictionary[x[idx]] = y[idx]
    return dictionary