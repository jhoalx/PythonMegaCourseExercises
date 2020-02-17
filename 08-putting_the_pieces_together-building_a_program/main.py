# Sections 55 to 59
################################################################################

# it is required to build a simple program that accepts
# user input (multiple times), the program should expect
# the input "\end" as keyword to stop receiving user
# input and thereafter output the whole user input


global_input_list = []


def sentence_maker(phrase: str) -> str:
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}".format(capitalized)


while True:
    current_input: str = input("Please type some text: ")
    if current_input == "\end":
        break
    else:
        global_input_list.append(sentence_maker(current_input))

print(" ".join(global_input_list))
