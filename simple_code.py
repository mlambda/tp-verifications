"""Simple code to test mypy."""
from collections.abc import Iterable, Mapping
from typing import TypeVar


def add(a: int, b: int) -> int:
    """
    Compute the sum between two numbers.

    :param a: First number
    :param b: Second number
    :return: Sum of the two numbers.
    """
    return a + b


add(1, 2)


def sum(numbers: Iterable[int]) -> int:
    """
    Compute the sum of an iterable of numbers.

    :param numbers: Iterable of numbers
    :return: Sum of the numbers.
    """
    total = 0
    for number in numbers:
        total += number
    return total


sum([1, 2, 3])


_T = TypeVar("_T")


def upper_keys(mapping: Mapping[str, _T]) -> dict[str, _T]:
    """
    Create a dictionary with uppercase keys from a given dictionary.

    :param mapping: Input mapping
    :return: Dictionary with the uppercase keys.
    """
    return {k.upper(): v for k, v in mapping.items()}


upper_keys({"a": 1, "b": 2})
