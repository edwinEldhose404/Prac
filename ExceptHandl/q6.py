'''Write a Python function that takes a number as input and returns its square root. Handle the case where 
the input is a negative number by raising a custom exception called NegativeNumberError.'''

class NegativeNumberError(Exception):
    pass

def numroot(x):
    if x<0:
        raise NegativeNumberError
    
    for i in range(2,x):
        if x/i==i:
            return i
    return "No square root"

try:
    print(numroot(36))
    print(numroot(20))
    print(numroot(-24))
except NegativeNumberError as e:
    print("Error: Negative Number Detected!")