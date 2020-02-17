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


################################################################################

# Lecture 49 - Looping through a Dictionary

student_grades = {"Valentine": 4.9, "Redfield": 3.9, "Kennedy": 3.1}

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)

################################################################################

# Lecture 50 - Bonus Code: Dictionary Loop and String Formatting

# You can combine a dictionary for loop with string formatting to create
# text containing information from the dictionary

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

# Another (better) way to do it:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

# In both cases the output is:
# John Smith has as phone number +37682929928
# Marry Simpons has as phone number +423998200919


################################################################################

# Exercise 34 - Loop over dictionary and Format
# Make the code print out the following output using a for loop:
# John Smith: +37682929928
# Marry Simpons: +423998200919

# So, the code should loop over the dictionary items and in each
# iteration should print out the dictionary key, a colon, a space, and the corresponding  value.

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("%s: %s" % (key, value))  # legacy
    print("{}: {}".format(key, value))  # python 3
    print(F"{key}: {value}")  # python 3

################################################################################

# Exercise 35
# Loop over the phone_numbers values and in each loop print out the phone
# number, but with '00' instead of '+'. In other words, your code should output:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for num in phone_numbers.values():
    print(num.replace('+', '00'))

################################################################################

# Lecture 51 - While Loops: How and Why

a: int = 3

while a < 10:
    print(a)
    a += 1
