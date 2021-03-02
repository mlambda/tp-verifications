"""Usage of bad_options.py and ruleset.py."""

from bad_options import Options
from ruleset import RuleSet

rs: RuleSet[str] = RuleSet()
rs.add_dep("A", "B")
rs.add_dep("B", "C")
rs.add_dep("C", "D")


options = Options(rs)
options.toggle("A")
print(options.selected)


# rs: RuleSet[int] = RuleSet()
# rs.add_dep(1, 2)
# rs.add_dep(2, 3)
# rs.add_dep(3, 4)


# options = Options(rs)
# options.toggle(1)
# print(options.selected)
