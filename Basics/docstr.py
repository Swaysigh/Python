def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)

# docstring is like string which is used to describe functions in our code.
#it is used just after function defination.

def add(m,n):
    '''this function takes an input ,returns the sum of two numbers'''
    print(m+n)

#prints the docstring of add
print(add.__doc__)
