def smallest_element(a,k):
    for i in range(k):
        for j in range(len(a)-i-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1]=a[j+1],a[j]
    print(a[len(a)-k])
       
a=list(map(int,input().split()))
k=int(input())
smallest_element(a,k)
