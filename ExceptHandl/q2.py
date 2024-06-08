'''Create a function that checks if a given string is a palindrome.
 Raise a custom PalindromeError if the input is not a valid string.'''

class PalindromeError(Exception):
    pass


def palin(str1):
    if type(str1)!=str:
        raise PalindromeError
    
    if str1 != str1[::-1]:
        return False
    else:
        return True
    
try:
    print(palin("abcba"))
    print(palin(42))
    print(palin("racecar"))
except PalindromeError as e:
    print("Error Occurred")