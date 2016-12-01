import string


def check_pangram(text):
    alpha = string.ascii_lowercase
    for letter in alpha:
        if letter not in text:
            if letter.upper() not in text:
                return False
    return True
