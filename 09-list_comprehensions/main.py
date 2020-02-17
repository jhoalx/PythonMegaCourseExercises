# Section 60 - Simple List Comprehension
# A List comprehension is a way to build lists without having to use for loops


# there's a common storage technique to save some bytes,
# consists of storing floats as integers an divide by 10
# when querying the info, here's an example

stored_temperatures = [221, 234, 340, 230]

corrected_temperatures = []
for temp in stored_temperatures:
    corrected_temperatures.append(temp / 10)

print(corrected_temperatures)
# Outputs [22.1, 23.4, 34.0, 23.0]

# Neater way to do this in 1 line of code


corrected_temperatures2 = [temp / 10 for temp in stored_temperatures]
print(corrected_temperatures2)  # prints exactly the same output

################################################################################

# Lecture 61 - List Comprehension with If Conditional

stored_temperatures = [221, 234, 0, 340, -9999, 230]  # non valid value included

corrected_temperatures = [temp / 10 for temp in stored_temperatures if temp > 0]
# Only if the temperature is greater than 0
print(corrected_temperatures)


################################################################################


# Exercise 36 - Only Numbers

# Define a function that takes as parameter a list that contains both numbers
# and strings and returns the list containing only the numbers.
# For example, I called your function with
# foo([99, 'no data', 95, 94, 'no data'])
#  it should return [99, 95, 94]

def foo(input_list: list) -> list:
    return [val for val in input_list if isinstance(val, int)]


print(foo([99, 'no data', 95, 94, 'no data']))


################################################################################

# Exercise 37 - Only Positive Numbers

# Define a function that takes as parameter list of numbers and returns
# the list containing only the numbers that are greater than 0.
# For example, I called your function with foo2([-5, 3, -1, 101])
#  it should return [3, 101]

def foo2(input_list: list) -> list:
    return [val for val in input_list if val > 0]


print(foo2([-5, 3, -1, 101]))

################################################################################

# Lecture 62 - List Comprehension with If-Else Conditional

# When using if-else conditional, the for loop is moved to the end
stored_temperatures = [221, 234, 0, 340, -9999, 230]

new_temps = [temp / 10 if temp > 0 else 0 for temp in stored_temperatures]
print(new_temps)


################################################################################

# Exercise 38 - Zeros Instead

# Define a function that takes as parameter a list that contains both
# numbers and strings and returns the same list but with zeros
# instead of strings. For example, I called your function with
# foo([99, 'no data', 95, 94, 'no data'])
# it should return [99, 0, 95, 94, 0]

def foo3(input_list: list) -> list:
    return [val if isinstance(val, int) else 0 for val in input_list]


print(foo3([99, 'no data', 95, 94, 'no data']))


################################################################################

# Exercise 39 - Convert and Sum Up

# Define a function that takes as parameter a list that contains decimal numbers
# as strings and returns the sum of those numbers.
# For example, I called your function with
# foo(['1.2', '2.6', '3.3'])
# it should return 7.1
# Note that the floats of the input list are string datatypes.

def foo4(input_list: list) -> float:
    return sum([float(val) for val in input_list])


print(foo4(['1.2', '2.6', '3.3']))
