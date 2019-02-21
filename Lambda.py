'''
Lambda serves as a small, isolated, stand-alone variable to be used inside a local variable.

Allows you to build functionality without creating a whole new function that you are only going to use one time.

'''


answer = lambda x: x*7
print(answer(5))