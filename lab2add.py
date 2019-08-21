def search(a,k):
    l,m,h=0,0,len(a)-1
    while(l<h):
        m=int((l+h)/2)
        if(a[m]==k):
            return m
        elif a[m]>=a[l]:
            if(a[m]>k and a[l]<=k):
                h=m-1
            else:
                l=m+1
        else:
            if(a[m]<k and k<=a[h]):
                l=m+1
            else:
                h=m-1
        if(a[l]==k):
            return l
    return -1
       
a=list(map(int,input().split()))
k=int(input())
if(search(a,k)==-1):
    print("not found")
else:
    print("found at index",search(a,k))
