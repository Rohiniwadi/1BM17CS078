class calldetails:
    def __init__(self,a,b,c,d):
        self.calledfrom=a
        self.calledto=b
        self.duration=c
        self.type=d
    def printout(self):
        print("called from number:",self.calledfrom)
        print("called to number:",self.calledto)
        print("duration:",self.duration)
        print("type of call:",self.type)


class util:
    def __init__(self):
        self.li=None
    def parse_customer(self,li):
        l=[]
        for i in range(len(li)):
            a=li[i].split(",")
            b=calldetails(a[0],a[1],a[2],a[3])
            b.printout()
            l.append(b)


call1="9999900011,9339339330,23,STD"
call2="9999900013,9339339331,22,STD"
call3="9999900022,9339339332,30,local"

list_of_call=[call1,call2,call3]
util().parse_customer(list_of_call)
