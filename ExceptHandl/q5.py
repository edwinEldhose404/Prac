'''Create a Python program that converts a string to an integer. Handle the ValueError exception if the 
string cannot be converted to an integer, and print a message indicating the error.'''

def convert(str1):
    try:
        num = int(str1)
        return num
    except ValueError:
        return "Invalid Input"

print(convert("72")," ",convert("Alonso"))