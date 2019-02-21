def removeChar(n):
    char = "aA"
    newstring = ""
    for eachChar in n:
        if eachChar not in char:
            newstring = newstring + eachChar
    return newstring

print(removeChar("Atomic"))
