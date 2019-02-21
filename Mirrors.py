
def reverse(mystr):
    reversed = ''
    for char in mystr:
        reversed = char + reversed
    if reversed == mystr:
        print("We have a palindrome!")

reverse("DEED")
