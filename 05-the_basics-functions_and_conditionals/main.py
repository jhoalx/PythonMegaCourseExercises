# define a function (pro style, with type-hints and return type)
# example purpose only, there's already a mean function in 'statistics' module


def mean(number_list: list) -> int:
    result: int = sum(number_list) / len(number_list)
    return result


print(mean([1, 3, 5, 10]))  # Should output 4.75


################################################################################

# Define a function that calculates the area of a square.
def square_area(side: int) -> int:
    return side * side


print("square area for side length 5: ", square_area(5))


################################################################################

# Define a function that converts fluid ounces to milliliters knowing that
# 1 fluid ounce is equal to 29.57353 milliliters. For example, I was to call
# your function with foo(1)  I would get an output of 29.57353
# If I called it with foo(5)  I would get 147.86765, and so on

def ounces_to_milliliters(ounces: float) -> float:
    return ounces * 29.57353


print("5 ounces to milliliters: ", ounces_to_milliliters(5))
