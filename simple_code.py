def add(a, b):
    return a + b


add(1, 2)


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


sum([1, 2, 3])


def upper_keys(dictionary):
    return {k.upper(): v for k, v in dictionary.items()}


upper_keys({"a": 1, "b": 2})
