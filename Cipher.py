import string


def encrypt(message, cipher):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            pos = alphabet.index(char)
            encrypted = encrypted + cipher[pos]
    return encrypted


def decrypt(message, alphabet):
    cipher = "badcfehgjilknmporqtsvuxwzy"
    decrypted = ''
    for char in message:
        if char == ' ':
            decrypted = decrypted + ' '
        else:
            pos = cipher.index(char)
            decrypted = decrypted + alphabet[pos]
    return decrypted


print(encrypt('hello world', "badcfehgjilknmporqtsvuxwzy"))
print(decrypt('gfkkp xpqkc', "abcdefghijklmnopqrstuvwxyz"))
