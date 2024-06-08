'''Write a Python script that iterates through a list of integers and attempts to divide each integer by 
zero. Handle the ZeroDivisionError exception within a try-except block,
 and use a finally block to print a message indicating the end of the iteration process.'''

def zdiv(ls):
    for i in ls:
        try:
            print(i/0)
        except:
            pass
        finally:
            print("Exception handled")

list1 = [1,6,2,4,5,3]
zdiv(list1)