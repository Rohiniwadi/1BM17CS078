def heapsort(a,n):
    for i in range(3):
        l=2*i+1
        if l+1<n:
            if a[l]<=a[i] and a[l+1]<=a[i]:
                continue
            else:
                return False
        elif l<n and a[l]<=a[i]:
            continue
        else:
            return False
    return True
l=[19,15,10,7,12,11]
print(heapsort(l,len(l)))
