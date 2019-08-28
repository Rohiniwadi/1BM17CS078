def mergesort(a):
    if len(a)>1:
        m=len(a)//2
        l1=a[:m]
        l2=a[m:]
        mergesort(l1)
        mergesort(l2)

        i,j,k=0,0,0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                a[k]=l1[i]
                i=i+1
            else:
                a[k]=l2[j]
                j=j+1
            k=k+1
        while i<len(l1):
            a[k]=l1[i]
            i=i+1
            k=k+1
        while j<len(l2):
            a[k]=l2[j]
            j=j+1
            k=k+1
l=list(map(int,input().split()))
mergesort(l)
print(l)
