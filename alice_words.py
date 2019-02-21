import string

readalice = open(
    "C:/Users/jkean/Desktop/Programming/PycharmProjects/PythonTraining/AliceInWonderland.txt", "r")
writealice = open(
    "C:/Users/jkean/Desktop/Programming/PycharmProjects/PythonTraining/AliceDictionary.txt", "w")


def main():
    alicedict = {}
    aline = readalice.readline()
    for aline in readalice:
        index = 0
        values = aline.split()
        for i in values:
            if i in alicedict:
                alicedict[i] += 1
            else:
                alicedict[i] = 1
                index = index + 1
    for letter, value in alicedict.items():
        print('{}\t{}'.format(letter, value))

    readalice.close()
    writealice.close()


main()
