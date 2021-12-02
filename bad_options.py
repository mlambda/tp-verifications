"""Options management."""
from collections.abc import Hashable, Iterable
from typing import Generic, TypeVar

from ruleset import RuleSet

_T = TypeVar("_T", bound=Hashable)


class Options(Generic[_T]):
    """Options management."""

    def __init__(self, rule_set: RuleSet[_T]) -> None:
        """
        Initialize a set of options.

        Args:
            rule_set: RuleSet to use to model dependencies.
        """
        self.rule_set = rule_set
        self.selected: set[_T] = set()

    def selection(self) -> set[_T]:
        """
        Return a view of the selected options.

        Returns:
            Set of selected options.
        """
        return set(self.selected)

    def remove_dependents(self, options: Iterable[_T]) -> None:
        """
        Remove options and their dependents from the selection.

        Args:
            options: Options to remove from the selection.
        """
        to_remove = set(options)
        done = False
        while not done:
            done = True
            for i, other_option in enumerate(self.selected):
                if to_remove & self.rule_set.compute_deps(other_option):
                    if other_option not in to_remove:
                        done = False
                    to_remove.add(other_option)
        self.selected -= to_remove

    def toggle(self, option: _T) -> None:
        """
        Toggle an option.

        Args:
            option: Which option to toggle.
        """
        if option in self.selected:
            self.remove_dependents({option})
        else:
            deps = self.rule_set.compute_deps(option)
            self.remove_dependents(
                set.union(*[self.rule_set.conflicts[d] for d in deps])
            )
            self.selected |= deps
