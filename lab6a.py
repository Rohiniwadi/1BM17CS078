def nqueen(k,n):
    global c
    global x
    for i in range(n):
        if place(k,i):
            x[k]=i
            if (k==(n-1)):
                print(x)
                c=c+1
            else:
                nqueen(k+1,n)
def place(k,i):
    global x
    for j in range(k):
        if (x[j]==i) or abs(x[j]-i)==abs(j-k):
            return False
    return True
x=[0]*4
c=0
nqueen(0,4)

print(c)
