"""File to define Bear class."""


class Bear:
    """Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing of Bear Class."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """One day in the river ecosystem."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int) -> None:
        """What occurs when the bear eats."""
        self.hunger_score += num_fish