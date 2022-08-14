# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

# Examples

# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re

def to_camel_case(text):
    cleaned_str = re.sub('-|_', ' ', text)
    list_of_words = cleaned_str.split(' ')
    return_str = ''
    for i, word in enumerate(list_of_words):
        if i == 0:
            return_str += word
        else:
            return_str += word.capitalize()
    return return_str    
