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