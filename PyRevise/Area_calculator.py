import math

def aCalc(shape, size):
    if shape =="circle":
        r = size[0]
        return math.pi *(r**2)
    
    elif shape == "rectangle":
        l = size[0]
        b = size[1]
        return l * b
    
    else:
        return "Invalid Statement"
    

print("Rectangle area: ",aCalc("rectangle",(45,21)))
print("Circle area: ",aCalc("circle",(32,)))