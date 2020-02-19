# Lecture 79 - Builtin Modules

# to see builtin methods and functions:
print("\n BUILTIN METHODS AND FUNCTIONS: \n", dir(__builtins__))

# prints list of python's system module names
import sys
print("\n BUILTIN MODULE NAMES: \n", dir(sys.builtin_module_names))

# There's no builtin sleep method

import time  # Import the time module

# get some help about the imported module and its methods
# help(time)
# dir(time)
# help(time.sleep)


# We'll use an infinite loop and set a delay using the time module
switch: bool = False
while True:
    if switch:
        print("tick")
    else:
        print("tock")
    time.sleep(1)  # sleep the script execution for 1 second
    switch = not switch

