#Morse Code
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}


#Ask for user input
def ask_input():
    user_input = input('Enter text: ').upper()
    user_input = list(user_input)
    return user_input


'''Loop through user_input string and convert each character/letter into a Morse Code by matching the key.
If character is not in the morse_code dictionary, replace it with #
Space is represented with /'''


def converter(input):
    converted_string = []
    for char in input:
        if char == " ":
            converted_string.append("/")
        elif char not in morse_code:
            code = '#'
            converted_string.append(code)
        for key, value in morse_code.items():
            if char == key:
                code = value
                converted_string.append(code)

    result = " ".join(converted_string)
    return result


print(converter(ask_input()))