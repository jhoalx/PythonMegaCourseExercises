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
