# Lecture 71 - Reading Text From a File

my_file = open("fruits.txt")
print(type(my_file))  # <class '_io.TextIOWrapper'>

# The file object returned by open() function is an
# object of type _io.TextIOWrapper.
# The class _io.TextIOWrapper provides methods and attributes which helps us
# to read or write data to and from the file. The following table lists some
# commonly used methods of _io.TextIOWrapper class.

print(my_file.read())

################################################################################

# Exercise 44 - Read Text From File and Print

# On the current folder there's a bear.txt file.
# read and print out the content

file = open("bear.txt")
print(file.read())
