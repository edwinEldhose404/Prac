

def fName(names, max):
    l = []
    for name in names:
        if(len(name)<max):
            l.append(name)
    return l

names = ["Reynolds","Ryan","Gosling","Pitt","Brad","Bale"]

final = fName(names, 5)
print("names shorter than 5 characters:", final)
