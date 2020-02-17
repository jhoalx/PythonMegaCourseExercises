import datetime

################################################################################
myNowVariable = datetime.datetime.now()
print(myNowVariable)

################################################################################
myNumber = 1337
myText = "Leet"

print(myNumber, myText)

################################################################################
# Simple Types
x = 10  # integer
y = '10'  # string
z = 13.37  # float

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

################################################################################
# List Types
student_grades = [9.1, 8.8, 7.5]

################################################################################
# Ranges
rangeList = list(range(1, 10))
print(rangeList)

rangeListWithStep = list(range(1, 10, 2))
print(rangeListWithStep)

################################################################################
# dir() is a powerful inbuilt function in Python3,
# which returns list of the attributes and methods of any object
# (say functions , modules, strings, lists, dictionaries etc.)
print(dir(list))
print(dir(int))
print(dir(str))

print(help(str.upper))

print(myText.upper())
print("The Thing That Should Not Be".upper())

################################################################################
# Dictionaries

student_grades_dictionary = {"John": 9.9, "Salchichón": 8.8, "Rambo": 7.7}
grades_sum = sum(student_grades_dictionary.values())
grades_count = len(student_grades_dictionary)
print("students average grades: ", grades_sum / grades_count)

################################################################################
# Tuple Types
# a tuple is basically an immutable list (faster)
grades_tuple = (7, 8, 9)
nested_tuple = ((10, 20), (30, 40, 50), (60, 70, 80, 90))

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# Section Wrap up

# Summary: Integers, Floats, Lists, Dictionaries, Tuples, dir, help
# In this section you learned that:

# Integers are for representing whole numbers:
rank = 10
eggs = 12
people = 34

# Floats represent continuous values:
temperature = 10.2
rainfall = 5.98
elevation = 1031.88

# Strings represent any text:
message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"

# Lists represent arrays of values that
# may change during the course of the program:
members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]

# Dictionaries represent pairs of keys and values:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}

# Keys of a dictionary can be extracted with:
phone_numbers.keys()

# Values of a dictionary can be extracted with:
phone_numbers.values()

# Tuples represent arrays of values that are
# not to be changed during the course of the program:
vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# To find out what attributes a type has:
dir(str)
dir(list)
dir(dict)

# To find out what Python builtin functions there are:
dir(__builtins__)  # This yields different output in python console vs .py file

# Documentation for a Python command can be found with:
help(str)
help(str.replace)
help(dict.values)
