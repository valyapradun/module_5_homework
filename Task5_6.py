"""
Implement a decorator call_once which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments.

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
55
print(sum_of_numbers(999, 100))
55
print(sum_of_numbers(134, 412))
55
print(sum_of_numbers(856, 232))
55
"""

import functools


def call_once(func):
    first_result = None

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal first_result
        if first_result is None:
            first_result = func(*args, **kwargs)
        return first_result
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))