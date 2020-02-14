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
