import numpy as np

#1)
def multi():
    a=np.random.randint(10,size=(2,3,4))
    b=np.random.randint(10,size=(3,4))
    print(a*b)

#2)
def calc():
    ar=int(input("Enter rows for a "))
    ac=int(input("Enter columns for a "))
    a=np.random.randint(10,size=(ar,ac))


    br=int(input("Enter rows for a "))
    bc=int(input("Enter columns for a "))
    b=np.random.randint(10,size=(br,bc))


    o=input("what operation do you need to do")
    if o=="+":
        return(a+b)
    elif o=="-":
        return(a-b)
    elif o=="*":
        return(a*b)
    elif o=="/":
        return(a/b)
    else:
        return("wrong input")




#3)
def outerprod():
    e=np.random.randint(10,size=(5,3))
    f=np.random.randint(10,size=5)
    op=e[:,:,np.newaxis]*f[np.newaxis,np.newaxis,:]
    print(op)



#4)
def skipslice():
    g=np.random.randint(10,size=(4,3,2))
    print(g[::2, ::2, :])


#5)
def sum_diagonal(h, i, j):
   
    len_i = len(i)
    len_j = len(j)
    
    k = np.zeros((len_i, len_j))
    
    for m in range(len_i):
        for n in range(len_j):
            row, col = i[m], j[n]
            diag_sum = 0
            
            while row < h.shape[0] and col < h.shape[1]:
                diag_sum += h[row, col]
                row += 1
                col += 1
            
            k[m, n] = diag_sum
    
    return k




#6)
def calcadjmeans():
    ar=int(input("Enter rows for a "))
    ac=int(input("Enter columns for a "))
    l=np.random.randint(10,size=(ar,ac))
    print(l)

    r_mean=np.mean(l,axis=1)
    c_mean=np.mean(l,axis=0)
    m=r_mean*c_mean

    return m



#7)
def flatten():
    l=np.random.randint(10,size=(4,6))
    print(l)
    z=l.reshape(2,2,6)
    print(z)
    c=z.ravel()
    print(c)



#8)
def rollarr()
    l=np.random.randint(10,size=(4,6))
    o=int(input("Enter position "))
    r=np.roll(l,o,axis=0)
    print(r)

#9)

def replace_with_neighbor_mean(p, x):
    
    p = p.copy()
    
    rows, cols = p.shape
    
    # Function to calculate the mean of neighbors
    def mean_of_neighbors(i, j):
        neighbors = []
        # Check and collect horizontal and vertical neighbors
        if i > 0:
            neighbors.append(p[i-1, j])
        if i < rows - 1:
            neighbors.append(p[i+1, j])
        if j > 0:
            neighbors.append(p[i, j-1])
        if j < cols - 1:
            neighbors.append(p[i, j+1])
        return np.mean(neighbors) if neighbors else x
    
    # Iterate over the array and replace occurrences of x
    for i in range(rows):
        for j in range(cols):
            if p[i, j] == x:
                p[i, j] = mean_of_neighbors(i, j)
    
    return p

# Example usage
np.random.seed(0)  # For reproducibility
p = np.random.randint(0, 10, (5, 5))
x = 5
print("Original array:")
print(p)
print("Modified array:")
print(replace_with_neighbor_mean(p, x))

