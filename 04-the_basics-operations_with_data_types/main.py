################################################################################
monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(21.3)  # append object to the end of the list

print(monday_temperatures)

################################################################################

# Clear the list
monday_temperatures.clear()
print(monday_temperatures)

################################################################################
# Recreate the list for sequential execution output purposes
monday_temperatures = [9.1, 8.8, 7.5]

# Get help for list's index method
print(help(list.index))

# As help said, lets find the index for the first occurrence (it's 2)
print(monday_temperatures.index(7.5))

# repeat search this time for 9.1, Start looking up at index 1 (8.8) and forward
# raises error because the value is not present
# print(monday_temperatures.index(9.1, 1))

# repeat search, Start looking up at index 2 (7.5) and forward,
# the found index is still 2 doesnt matter if it started looking up at index 2)
print(monday_temperatures.index(7.5, 2))

################################################################################
# Append item to list
seconds = [1.2323442655, 1.4534345567, 1.023458894, 2.879524862, 1.981751683]
current = 1.10001399445
seconds.append(current)
print(seconds)

################################################################################
# Remove first occurrence of value 1.2323442655

seconds.remove(1.2323442655)
print(seconds)

################################################################################
# Remove 2 items from list

seconds.remove(1.10001399445)
seconds.remove(2.879524862)
print(seconds)

################################################################################
# Accessing List Items

print(monday_temperatures.__getitem__(1))
print(monday_temperatures[1])

################################################################################
# Access third item
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882",
           "KOC9889482"]
print(serials[2])

################################################################################
# Access 1st, 3rd, 6th items
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882",
           "KOC9889482"]
print(serials[0], serials[2], serials[5])

################################################################################
# append 1st weekend to workdays (oh, please, no)
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)

################################################################################
# Access a "slice"
monday_temperatures.append(10.10)
monday_temperatures.append(11.11)
print("monday_temperatures variable value: ", monday_temperatures)

# from 2nd index inclusive to 3rd index exclusive
sliceVariable = monday_temperatures[1:2]
print(sliceVariable)

# from 1st index inclusive to 3rd index exclusive
print(monday_temperatures[0:2])

print(monday_temperatures[:3])  # from 1st index to 4th index exclusive
print(monday_temperatures[3:])  # from 4th index forward

################################################################################
# Accessing Items and Slices with Negative Indexes (from right to left)
print(monday_temperatures[-1])  # prints 5th item
print(monday_temperatures[-5])  # prints 1st item

# Access negative slices
# prints 4th item onwards, "The tail of the list"
print(monday_temperatures[-2:])

print(monday_temperatures[-5:-2])  # prints 1st to 3rd

################################################################################
# Accessing Characters and Slices in Strings

myString = "Hello"
print(myString[1])  # prints "e"
print(myString[-1])  # prints "o"
print(myString[:3])  # prints "hel"

# having a mixed object type list

mixedList = ['Hello', 1, 2, 3]
print(mixedList[0][3:])  # prints "lo"

################################################################################
# SLice of a list, 2nd to 4th
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

################################################################################
# Slice of a list, First 3 items
print(letters[:3])

################################################################################
# Slice of a list, Last 3 items
print(letters[4:])

################################################################################
# Accessing items in Dictionaries
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(student_grades["Sim"])

english_to_portuguese = {"rain": "chuva", "sun": "sol"}

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# Section Wrap Up

# Summary: Positive/Negative Indexes, Slicing
# In this section you learned that:

# Lists, strings, and tuples have a positive index system:

# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#    0      1      2      3      4      5      6

# And a negative index system:

# ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#   -7     -6     -5     -4     -3     -2     -1


# In a list, the 2nd, 3rd, and 4th items can be accessed with:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[1:4])
# Output: ['Tue', 'Wed', 'Thu']

# First three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:3])
# Output:['Mon', 'Tue', 'Wed']


# Last three items of a list:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[-3:])
# Output: ['Fri', 'Sat', 'Sun']


# Everything but the last:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:-1])
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']


# Everything but the last two:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days[:-2])
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']


# A single in a dictionary can be accessed using its key:
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
print(phone_numbers["Marry Simpsons"])
# Output: '+423998200919'
