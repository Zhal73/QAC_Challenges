def name(input):
    lower_string = input.lower()
    splitted = lower_string.split()
    total = 0
    for word in splitted:
        if word == "am":
            total = total + 1
    return total


print(name("Hamburger are not healthy"))