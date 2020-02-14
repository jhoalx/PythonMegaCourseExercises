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
