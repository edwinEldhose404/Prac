'''Write a Python function that attempts to divide two numbers and handles the ZeroDivisionError exception. 
Include a finally block to print a message indicating the end of the division operation.'''

def div1(x,y):
    try:
        z=x/y
        print(z)
    except ZeroDivisionError as e:
        print("Cant divide by zero")
    finally:
        print("--Process finished--")

div1(10,5)
div1(5,0)