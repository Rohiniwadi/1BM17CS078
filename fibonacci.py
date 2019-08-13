fib =[]
a,b,c=0,1,0
for i in range(int(input())):
	fib.append(a)
	c=a
	a=b
	b=b+c
print(fib)
