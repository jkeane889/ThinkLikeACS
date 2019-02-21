import string


def remove(sub, newstring):
    count = newstring.count(sub)
    if count > 0:
        found = True
        while count > 0:
            updatedstring = newstring.replace(sub, " ")
            return updatedstring
    else:
        found = False


print(remove('ha', 'Timehaoncehaoverha'))
