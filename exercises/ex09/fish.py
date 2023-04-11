"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int
    
    def __init__(self):
        """Initialization of Fish class."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """One day in the river ecosystem."""
        self.age += 1
        return None