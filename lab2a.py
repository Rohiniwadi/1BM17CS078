def smallest_element(a,k):
    for i in range(k):
        m=i
        for j in range(i+1,len(a)):
            if(a[m]>a[j]):
                m=j
        a[i],a[m]=a[m],a[i]
    print(a[k-1])
       
a=list(map(int,input().split()))
k=int(input())
smallest_element(a,k)
