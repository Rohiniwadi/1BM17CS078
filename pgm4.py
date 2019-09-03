class Student:
    def __init__(self):
        self.name = " "
        self.age =0
        self.mark=0
    def validate_marks(self):
        if self.mark>0 and self.mark<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.age>20:
            return True
        else:
            return False
    def check_quali(self):
        if self.validate_marks() and self.validate_age():
            if self.mark>=65:
                return True
            else:
                return False
        else:
            return False
    def setter(self,n,a,m):
        self.name=n
        self.age=a
        self.mark=m
    def getter(self):
        print("name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.mark)
        print("Given information is valid:",self.check_quali())
s1=Student()
s1.setter("r",20,55)
s1.getter()

s2=Student()
s2.setter("e",22,76)
s2.getter()

        
        
