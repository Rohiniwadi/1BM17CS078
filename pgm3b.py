import string
from random import randint
str1=string.printable
print("randamly generated password:")
for i in range(6):
    print(str1[randint(0,100)],end="")
 
