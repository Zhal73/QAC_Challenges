"""
Given a string, return the number of times "am" appears in the string BUT ONLY WHEN "am" is not followed or preceded by any other LETTERS.
 
eg

name("Am I in Amsterdam") → 1
name("I am in Amsterdam am I?") → 2
name("I have been in Amsterdam") → 0
"""

def name(input):
    lower_string = input.lower()
    splitted = lower_string.split()
    total = 0
    for word in splitted:
        if word == "am":
            total = total + 1
    return total