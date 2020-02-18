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
################################################################################
# Lecture 66 - Default and Non-default Parameters and Keyword and
# Non-Keyword Arguments.

# With Keyword Arguments the position does not matter
print(foo(param_b="first, ", param_a="second, "))


# You can specify default parameter values
def foo2(param_a="Hi", param_b="User") -> str:
    return param_a + param_b


# Default parameter value *With Typehint*
def foo3(param_a: str = "Hi", param_b: str = "User") -> str:
    return param_a + param_b
