def rot13(n):
    caesarencrypt = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in n:
        if i in alphabet:
            c = alphabet.index(i) + 13
            newChar = alphabet[c % len(alphabet)]
            caesarencrypt = caesarencrypt + newChar
    return caesarencrypt


print(rot13("hello"))
