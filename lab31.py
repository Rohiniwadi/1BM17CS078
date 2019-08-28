def quicksortr(a,l,h):
    if(l<h):
        ps=partition(a,l,h)
        quicksortr(a,l,ps-1)
        quicksortr(a,ps+1,h)
def partition(a,l,h):
    i,j=l+1,h
    while True:
        while a[l]>=a[i] and i<h:
          i=i+1
        while a[l]<a[j] and j>=l:
          j=j-1
        if(i<j):
          a[i],a[j]=a[j],a[i]
        else:
          a[l],a[j]=a[j],a[l]
          return j
l=list(map(int,input().split()))
quicksortr(l,0,(len(l)-1))
print(l)
