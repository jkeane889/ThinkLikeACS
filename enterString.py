def alphaString():
    print('Please enter a sentence for analysis: ')
    newstring = input('Sentence: ')
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counts = {}
    index = 0
    for i in alphabet:
        counts[i] = 0
        index = index + 1
    for key in newstring:
        if key in alphabet:
            counts[key] += 1
    for letter, value in counts.items():
        print('{}\t{}'.format(letter, value))


alphaString()
