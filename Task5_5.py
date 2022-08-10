"""
Implement a decorator remember_result which remembers last result of function it decorates and prints it before next call.

@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result
"""

import functools

def remember_result(func):
    last_result = None

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal last_result
        print(f"Last result = '{last_result}'")
        last_result = func(*args, **kwargs)

    return wrapper


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = '{result}'")
    return result


if __name__ == '__main__':
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)
