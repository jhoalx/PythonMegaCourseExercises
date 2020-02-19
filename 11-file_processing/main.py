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

################################################################################

# Exercise 45 - Reading and Processing Text

# Read the bear.txt  file, and print out the first 90 characters of its content.

file = open("bear.txt")
print(file.read()[:91])
file.close()


################################################################################

# Exercise 46 - File Processing Inside Function
# Define a function that gets a single string character and a filepath as
# parameters and returns the number of occurrences of that character in the file

def foo(char: str, file_path: str) -> int:
    file_open = open(file_path)
    file_text = file_open.read()
    return file_text.count(char)


print(foo('a', "bear.txt"))

################################################################################

# Lecture 74 - Opening Files Using "with" context manager
# the context manager ("with") will apply close method automatically

with open("fruits.txt") as my_file:
    content = my_file.read()

print(content)

################################################################################

# Lecture 75 - Different Filepaths

with open("files/lorem_ricksum.txt") as lorem_ricksum:
    rick_text = lorem_ricksum.read()

print(rick_text)

################################################################################

# Lecture 76 - Writing Text to a File

# help(open)

# if the file exists, it'll be overwritten
with open("vegetables.txt", "w") as my_file:
    my_file.write('Tomato\nCucumber')  # notice \n (new line)
    my_file.write('\nGarlic')

################################################################################

# Exercise 47 - Write Snail

# Use Python to create a file with name 'file.txt'  and write 'snail' there
with open('file.txt', 'w') as new_file:
    new_file.write('snail')

################################################################################

# Exercise 48 - Write First 90

# Create a 'first.txt' file that contains the first 90 characters of 'bear.txt'
# Note that you should read the content of 'bear.txt' with Python,
# extract its first 90 characters with Python,
# and write those characters in 'first.txt' with Python.

with open('bear.txt') as bear_txt:
    with open('first.txt', 'w') as first_txt:
        first_txt.write(bear_txt.read()[:90])

################################################################################

# Lecture 77 - Appending Text to an Existing File


with open('fruits.txt', 'a') as fruits_file:  # 'a' for append mode (no read)
    fruits_file.write('\nStrawberry')

with open('fruits.txt', 'a+') as fruits_file:  # 'a+' for append and read mode
    fruits_file.write('\nCherry')
    fruits_file.seek(0)  # put the cursor at the 0 position of the file
    result = fruits_file.read()

print(result)

################################################################################

# Exercise 49 - Read and Append

# Append the text of 'bear1.txt' to 'bear2.txt'. In other words, 'bear2.txt'
# should contain its text and the text of 'bear1.txt' after that

with open('bear1.txt') as source_file:
    with open('bear2.txt', 'a+') as destination:
        destination.write(source_file.read())

################################################################################

# Exercise 50 - Copy n-times

# The existing content of data.txt looks like this:
# 1.3, 1.5
# 2.3, 2.7

# Use Python to modify the content of data.txt
# so that its content looks like below:

# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7
# 1.3, 1.5
# 2.3, 2.7

# So, you need to find a way to insert the existing content two more times.

with open('data.txt', 'a+') as data:
    data.seek(0)
    content = data.read()
    data.write("\n" + content)
    data.write("\n" + content)

print(content)
