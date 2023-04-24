"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730486310"


class Simpy:
    """Simpy Class."""

    values: list[float]

    def __init__(self, floats: list[float]):
        """Simpy constructor."""
        self.values = floats

    def __str__(self) -> str:
        """Will override string operator."""
        return f"Simpy({self.values})"
    
    def fill(self, float_val: float, num_val: int) -> None:
        """Fill Simpy's values with a specific number."""
        self.values = []
        i = 0
        while i < num_val:
            self.values.append(float_val)
            i += 1
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with a range of values."""
        assert step != 0.0
        i = start
        if step > 0:
            while i < stop:
                self.values.append(i)
                i += step
        else:
            while i > stop:
                self.values.append(i)
                i += step

    def sum(self) -> float:
        """Return the sum of all items in the values attribute."""
        sum: float = 0.0
        i: int = 0
        while i < len(self.values):
            sum += self.values[i]
            i += 1
        return sum
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Can add two Simpy objects."""
        result: Simpy = Simpy([])
        if type(rhs) == Simpy:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(rhs.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
            return result
        if type(rhs) == float:
            for x in self.values:
                result.values.append(x + rhs)
            return result
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Can raise one Simpy object by another Simpy object."""
        result: Simpy = Simpy([])
        if type(rhs) == Simpy:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(rhs.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
            return result
        if type(rhs) == float:
            for x in self.values:
                result.values.append(x ** rhs)
            return result
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Will override equal operator."""
        result: list[bool] = []
        if type(rhs) == Simpy:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(rhs.values):
                if rhs.values[i] == self.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        if type(rhs) == float:
            for x in self.values:
                if x == rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Will override greater than operator."""
        result: list[bool] = []
        if type(rhs) == Simpy:
            assert len(rhs.values) == len(self.values)
            i: int = 0
            while i < len(rhs.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else:
                    result.append(False)
                i += 1
        else:
            for x in self.values:
                if x > rhs:
                    result.append(True)
                else:
                    result.append(False)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Will override indexing function."""
        if type(rhs) == int:
            result: float = self.values[rhs]
            return result
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result