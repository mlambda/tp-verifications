from functools import wraps


def decorator(function):
    @wraps(function)
    def new_function(*args, **kwargs):
        print("Decorated!")
        return function(*args, **kwargs)

    return new_function


def double(iterable):
    for item in iterable:
        yield item * 2
