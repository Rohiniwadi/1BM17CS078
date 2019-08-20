def search(l,k):
    if k in l:
        return True
    return False
l=list(map(int,input().split()))
k=int(input("enter he element to be searched"))
print(search(l,k))
