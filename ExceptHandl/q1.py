'''Write a function that takes two numbers as input and
 divides the first number by the second number.
 Raise a ZeroDivisionError if the second number is zero.'''

def div1(x,y):
    if y==0:
        raise ZeroDivisionError
    else:
        return x/y
try:
    print(div1(6,3))
    print(div1(10,0))
    print(div1(5,6))
except:
    print("You cannot divide by zero");
