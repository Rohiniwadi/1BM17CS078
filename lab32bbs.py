def selectionsort(a):
    c=0
    for i in range(len(l)-1):
        m=i
        for j in range(i+1,len(a)):
            c=c+1
            if(a[m]>a[j]):
                m=j
        a[i],a[m]=a[m],a[i]
    return c
l=list(map(int,input().split()))
print("no of comparision for selection sort",selectionsort(l))
