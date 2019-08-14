n=int(input())
a = list(map(int,input().split()))
k=int(input())
l,h,m=0,n,0
while l<=h:
    m=int((l+h)/2)
    if a[m]==k:
        l_index,f_index,c=0,0,0
        for i in range(m,n):
            if a[i]==k:
                c=c+1
                l_index=i
        for j in range(m,-1,-1):
            if a[j]==k:
                c=c+1
                f_index=j
        print(f_index," ",l_index," ",c-1)
        break
    elif(a[m]>k):
        h=m-1
    elif(a[m]<k):
        l=m+1
        
