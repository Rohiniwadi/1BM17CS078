l1 =[]
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i%2==0):
      l1.append(l[i])
print(l1)
