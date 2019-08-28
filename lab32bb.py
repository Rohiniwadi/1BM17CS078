
def bubblesort(a):
    c=0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            c=c+1
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    return c
l=list(map(int,input().split()))
print("no of comparision for bubble sort",bubblesort(l))
 l=list(map(int,input().split()))
#print("no of comparision for bubble sort",bubblesort(l))
