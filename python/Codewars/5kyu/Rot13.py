def rot13(message):
    alphabet = [*'abcdefghijklmnopqrstuvwxyz']
    output = ''
    for char in message:
        if char.lower() in alphabet:
            loc = alphabet.index(char.lower()) + 13
            loc = loc - len(alphabet) if loc > len(alphabet) - 1 else loc
            output += alphabet[loc].upper() if char.isupper() else alphabet[loc]
        else:
            output += char
    return output
