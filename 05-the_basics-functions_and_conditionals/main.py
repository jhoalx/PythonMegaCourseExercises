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
