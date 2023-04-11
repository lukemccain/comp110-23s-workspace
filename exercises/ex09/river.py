"""File to define River class."""

__author__ = "730486310"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """River class."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Checking animals ages."""
        i: int = 0
        fish_list: list[Fish] = []
        while i < len(self.fish):
            if self.fish[i].age <= 3:
                fish_list.append(self.fish[i])
            i += 1
        self.fish = fish_list 
        i = 0
        bears_list: list[Bear] = []
        while i < len(self.bears):
            if self.bears[i].age <= 5:
                bears_list.append(self.bears[i])
            i += 1
        self.bears = bears_list
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Removing fish from ecosystem."""
        i: int = 0
        while i < amount:
            self.fish.pop(0)
            i += 1

    def bears_eating(self):
        """Represents bears eating fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Removes starving bears."""
        i: int = 0
        bear_list: list[Bear] = []
        while i < len(self.bears):
            if self.bears[i].hunger_score >= 0:
                bear_list.append(self.bears[i])
            i += 1
        self.bears = bear_list
        return None
        
    def repopulate_fish(self):
        """Reproducing 4 fish for every 2 parents."""
        length: int = len(self.fish) // 2
        i: int = 0
        while i < length:
            for j in range(0, 4):
                self.fish.append(Fish())
            i += 1
        return None
    
    def repopulate_bears(self):
        """Reproducing 1 new bear for every 2 parents."""
        length: int = len(self.bears)
        i: int = 0
        while i < length:
            new_bear: Bear = Bear()
            self.bears.append(new_bear)
            i += 2
        return None
    
    def view_river(self) -> None:
        """Return the river status, including the day, number of fish and number of bears present."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulate one week of life in the river."""
        i: int = 0
        while i < 7:
            self.one_river_day()
            i += 1