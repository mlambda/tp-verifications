check:
	flake8 --count bad_options.py ruleset.py simple_code.py
	mypy bad_options.py ruleset.py simple_code.py
	pylint bad_options.py ruleset.py simple_code.py
	black --check bad_options.py ruleset.py simple_code.py
