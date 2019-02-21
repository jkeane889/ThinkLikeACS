def countAll(newstring):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counts = {}
    for i in newstring:
        if i in alphabet:
            counts[i] = i
