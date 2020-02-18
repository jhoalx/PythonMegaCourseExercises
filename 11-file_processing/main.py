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

################################################################################

# Lecture 72 - File Cursor

# .read() method moves the cursor to the end of the file
# file contents can be stored to a variable
file = open("bear.txt")
file_contents = file.read()

################################################################################

# Lecture 73 - Closing a File

# When reading files, an object is created in RAM, it remains there until
# the execution of the program ends, a good practice is to close it
# once the needed processing is complete (lecture 72)

file.close()
print(file_contents)
