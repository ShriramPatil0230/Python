# inputfunction

# a = input("Enter your name: ")
# print(a)

from multiprocessing.sharedctypes import Value
from tokenize import Number
from unittest import result


def addOneTwo(Numbers):    
    #  Value of (Number) is come From (Var)
    Result = Numbers + 1
    # Result = 0 + 1 for Var1
    return Result

Var1 = 0
# Value of Var is 0
print(Var1)
Var2 = addOneTwo(Var1)
Var3 = addOneTwo(Var2)
print(Var2)
print(Var3)

def addOneAddTwo(Number1,Number2):
    Result = Number1 + 1
    Result += Number2 + 2
    return Result

Sum = addOneAddTwo(Var2,Var3) 
print(Sum)  