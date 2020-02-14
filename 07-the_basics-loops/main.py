# FOR loops

friday_temperatures = [9.1, 8.8, 7.6]
for temperature in friday_temperatures:
    print(round(temperature))

# loop trough string characters
for letter in "hello":
    print(letter)

################################################################################
# Exercise 30 - Loop over colors

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

################################################################################
# Exercise 31 - Loop over big colors
# Loop over the color items and print out the item in every loop only if the
# item is greater than 50
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

################################################################################
# Exercise 32 - Loop over integer colors
# Loop over the color items and print out the item in every loop only if the
# item is integer
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int:
        print(color)

################################################################################
# Exercise 33 - Loop over int and big
# Loop over the color items and print out the item  in every loop
# only if the item is an integer
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for color in colors:
    if type(color) == int and color > 50:
        print(color)


################################################################################

# For Loop Over a Function

# Note that using loops you can call any function multiple times,
# even your own functions. Let's suppose we defined this function:

def celsius_to_kelvin(cels):
    return cels + 273.15


# That is a function that gets a number as input,
# adds 273.15 to it and returns the result.
# A for loop allows us to execute that function over a list of numbers:

monday_temperatures = [9.1, 8.8, -270.15]

for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))

# The output of that would be:
# 282.25
# 281.95
# 3.0

# So, in the first iteration celsius_to_kelvin(9.1) was executed,
# in the second celsius_to_kelvin(8.8)
# and in the third celsius_to_kelvin(-270.15).

# That's just something to keep in mind.
