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
