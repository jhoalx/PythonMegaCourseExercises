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
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

################################################################################
# Access 1st, 3rd, 6th items
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

################################################################################
# append 1st weekend to workdays (oh, please, no)
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
print(workdays)
