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


################################################################################

# Lecture 68 - Functions with an Arbitrary Number of Keyword Arguments

def foo4(**kwargs):  # notice the two asterisks (**)
    return kwargs


# print(foo4(1, 2, 3)) # produces an error, arguments should have keyword

# All arguments must be named (keyword)
print(foo4(a=1, b=2, c=3))  # returns a dictionary


################################################################################

# Exercise 43 - Indefinite Number of Keyword Arguments

# call find_sum() with the correct parameters,
# so that the output of the code is 9

def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=3, b=3, c=3))


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# Section Wrap Up

# In this section you learned that:

# Functions can have more than one parameter:
def volume(a, b, c):
    return a * b * c


# Functions can have default parameters (e.g. coefficient):
def converter(feet, coefficient=3.2808):
    meters = feet / coefficient
    return meters


print(converter(10))  # Output: 3.0480370641306997


# Arguments can be passed as non-keyword (positional) arguments (e.g. a)
# or keyword arguments (e.g. b=2 and c=10):

def volume(a, b, c):
    return a * b * c


print(volume(1, b=2, c=10))


# An *args parameter allows the  function to be called with an
# arbitrary number of non-keyword arguments:

def find_max(*args):
    return max(args)


print(find_max(3, 99, 1001, 2, 8))


# Output: 1001


# An **kwargs parameter allows the function to be called with an
# arbitrary number of keyword arguments:}

def find_winner(**kwargs):
    return max(kwargs, key=kwargs.get)


print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))  # Output: Sim

# See function_summary.png
