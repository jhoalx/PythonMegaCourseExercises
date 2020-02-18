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


################################################################################

# Lecture 67 - Functions with an Arbitrary Number of Non-keyword Arguments

def mean(*arguments):
    return sum(arguments) / len(arguments)


print(mean(1, 2, 3, 6, 9))


################################################################################

# Exercise 41 - Average Function
# Define a function that takes an indefinite number of numbers as arguments and
# returns their average. If I called your function with foo(10, 20, 30, 40)
# it should return the 25, the average of those numbers.

def average(*args):
    return sum(args) / len(args)


################################################################################

# Exercise 42 - Indefinite Number of Strings Processed
# Define a function that takes an indefinite number of strings as parameters
# and returns a list containing all the strings in UPPERCASE and sorted
# alphabetically. For example, if I called your function with
# foo("snow", "glacier", "iceberg")  it should return
# ["GLACIER", "ICEBERG", "SNOW"]


def upper_sorted(*args: str) -> list:
    return sorted([text.upper() for text in args])


print(upper_sorted("snow", "glacier", "iceberg"))
