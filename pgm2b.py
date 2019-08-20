def rev(s):
    l=s.split()
    l.reverse()
    print(" ".join(l))
def revstr(s):
    l=s.split()
    l1=[]
    for i in l:
        l1+=i[: :-1]
        l1+=" "
    print("".join(l1))
s=input("enter a string")
rev(s)
revstr(s)
