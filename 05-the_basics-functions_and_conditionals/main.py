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


################################################################################

# Intro to conditionals
# If

# This mean function will Conditionally operate both for lists and dictionaries values
def mean(value: list or dict) -> float:
    if type(value) == dict:
        result = sum(value.values()) / len(value)
    elif type(value) == list:
        result = sum(value) / len(value)
    else:
        raise TypeError("Only list or dictionary as parameter")
    return result


student_grades = {"ruben": 9.1, "joan": 9.2, "mauro": 9.3}
print("student grades mean: ", mean(student_grades))

################################################################################

# Bonus Code: Using "and" and "or" in a Conditional
# You learned to check for one single condition:

x = 1

if x == 1:
    print("Yes")
else:
    print("No")

# You can also check if two conditions are met
# at the same time using an and operator:

x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")
# That will return Yes since x == 1 and y ==1 are both True.


# You can also check if one of two conditions are met using an or operator

x = 1
y = 1

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")


# That will return Yes since at least one of the conditions is True. In this case x == 1 is True.

################################################################################

# Password Controller exercise
# Define a function that:
#   (1) takes a string as parameter
#   (2) returns False  if the string contains less than 8 characters
#   (3) returns True if the string contains 8 or more characters
#   (4) If I called your function with foo("mypass")  it would return False
#   If I called it with foo("mylongpassword")  it would return  True and so on

def foo(parameter: str) -> bool:
    if len(parameter) < 8:
        return False
    else:
        return True


print(foo("mypass"))
print(foo("mylongpassword"))


################################################################################


# Warm or Cold Exercise
# Define a function that:
#   (1) takes a temperature as parameter
#   (2) returns "Warm" if the temperature is greater than 7
#   (3) returns "Cold" if the temperature is equal or less than 7
# If i called the function with foo_two(10) it would return "Warm"
# If called with foo_two(7) or foo_two(5) it would return "Cold"
# in both cases and so on.

def foo_two(temp: int) -> str:
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


################################################################################


x: int = -3
y: int = 1
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")


################################################################################

# Exercise 27 -  Hot, Warm, Cold
# Define a function that:
#   (1) takes a temperature as parameter
#   (2) returns Hot  if the temperature is greater than 25
#   (3) returns Warm if the temperature is between 15 and 25, including 15 and 25.
#   (4) returns Cold if the temperature is less than 15.


def hot_warm_cold(temp: float) -> str:
    if temp > 25:
        return "Hot"
    elif 15 < temp < 25:  # same as: elif temp > 15 and temp < 25
        return "Warm"
    else:
        return "Cold"


################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# Section Wrap Up

# In this section you learned to:

# Define a function
def cube_volume(a):
    return a * a * a


# Write a conditional block:

message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")

# Write a conditional block of multiple conditions:

message = "hello there"

if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

# Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")

# Output is Yes since both x and y are 1.


# Use the or operator to check if at least one condition is True

x = 1
y = 2

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

# Output is Yes since x is 1.


# Check if a value is of a certain type with:

print(isinstance("abc", str))
print(isinstance([1, 2, 3], list))
# or
print(type("abc") == str)
print(type([1, 2, 3]) == list)
