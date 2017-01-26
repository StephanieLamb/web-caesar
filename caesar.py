def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    value = alphabet.index(letter.lower())
    return value

def rotate_character(char, rot):
    if char.isalpha():

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rotation = alphabet_position(char) + rot
        new_char = alphabet[rotation % 26]
        if char.isupper():
            new_char = new_char.upper()
        return new_char
    else:
        return char

def encrypt(text, rot):

    encrypted = [rotate_character(c,rot) for c in text]
    return "".join(encrypted)
