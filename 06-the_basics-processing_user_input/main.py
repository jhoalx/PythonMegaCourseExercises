def weather_condition(temperature: float) -> str:
    if temperature >= 10:
        return "Warm"
    else:
        return "Cold"


current_temperature = float(input("Please type current temperature: "))
print(weather_condition(current_temperature))

################################################################################

# String formatting
user_input = input("Please, enter your name: ")

# %-formatting
# Unfortunately, this kind of formatting isn’t great because it is verbose and
# leads to errors, like not displaying tuples or dictionaries correctly
message1 = "Hello %s, nice to meet you" % user_input

# recommended formatting method, Literal String Interpolation
# or more commonly called "F-strings"
# F-strings are fast! Much faster than %-formatting and str.format()
# notice the F before the double-quotes
message2 = F"Another greeting {user_input}, have a nice day"
print(message1)
print(message2)

################################################################################
# String formatting with multiple variables

new_string1 = input("please type first string")
new_string2 = input("please type second string")

# %-formatting, again, not recommended
print("First string: %s, second string: %s" % (new_string1, new_string2))

# F-string
print(F"First string: {new_string1}, second string: {new_string2}")


################################################################################

# Exercise 28 - String Formatting
# Implement a function that gets a person's name as parameter and greets the
# person with "Hi Person". For example, if I called your function with
# foo("Marry")  the function should return "Hi Marry"

#
def greet(name: str) -> str:
    # return "Hi %s" % name
    return F"Hi {name}"


print(greet("john"))


################################################################################

# Exercise 29 - String Formatting and Uppercase
# Implement a function that gets a person's name as parameter and greets
# the person with "Hi Person" . The first letter should always be uppercase.
# For example, if I called your function with foo("Marry") or foo("marry")
# the function should return "Hi Marry" in all cases

def greet2(name: str) -> str:
    # return "Hi %s" % name.capitalize()
    return F"Hi {name.capitalize()}"


print(greet2("john"))

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
# Section Wrap Up

# In this section you learned that:
# A Python program can get user input via the input function:

# The input function halts the execution of the program
# and gets text input from the user:

name = input("Enter your name: ")

# The input function converts any input to a string,
# but you can convert it back to int or float:

experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12

# You can format strings with (works both on Python 2 and 3):

name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))
# Output: Hi Sim, you have 1.5 years of experience.

# You can also format strings with (Python 3 only):

name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
# Output: Hi Sim, you have 1.5 years of experience.
