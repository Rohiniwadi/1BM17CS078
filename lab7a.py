f=open("one.txt","w")
for i in range(1001):
    if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           f.write(str(i)+" ")
f.close()
f=open("two.txt","w")
f1=open("one.txt","r")
def ishappy(n):
    cache = []
    while n != 1:
        n = sum(int(i)**2 for i in str(n))
        if n in cache:
            return False
        cache.append(n)
    return True

for i in range(1001):
    if ishappy(i):
        f.write(str(i)+" ") 
f.close()
f1=open("one.txt","r")
f2=open("two.txt","r")
s1=list(f1.read().split(" "))
s2=list(f2.read().split(" "))
l=[]
for i in s1:
    if i in s2 and i not in l:
        l.append(i)
print(l)
f1.close()
f2.close()
        
        
