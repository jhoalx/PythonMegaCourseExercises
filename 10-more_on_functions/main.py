# Lecture 64 - Functions with Multiple Arguments


def area(a: float, b: float) -> float:
    return a * b


print(area(5.1, 8.1))


################################################################################

# Exercise 40 - Function with Multiple Parameters

# Implements a function that takes two strings as parameters,
# concatenates them, and returns the result.

def foo(param_a: str, param_b: str) -> str:
    return param_a + param_b


print(foo("first, ", "second, "))
