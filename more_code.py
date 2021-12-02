"""More advanced code to test mypy."""
from collections.abc import Callable, Iterable, Iterator
from functools import wraps
from typing import ParamSpec, Protocol, TypeVar

_P = ParamSpec("_P")
_T = TypeVar("_T")


def decorator(function: Callable[_P, _T]) -> Callable[_P, _T]:
    """Decorate a function to print “Decorated!”."""

    @wraps(function)
    def new_function(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        print("Decorated!")
        return function(*args, **kwargs)

    return new_function


_T_co = TypeVar("_T_co", covariant=True)


class SupportsIntMultiplication(Protocol[_T_co]):
    """Protocol for objects that can be multiplied by ints."""

    def __mul__(self, other: int) -> _T_co:
        """Multiply by an int."""
        ...


def double(iterable: Iterable[SupportsIntMultiplication[_T]]) -> Iterator[_T]:
    """Double the items of the iterable."""
    for item in iterable:
        yield item * 2


double(["a", "b", "c"])
