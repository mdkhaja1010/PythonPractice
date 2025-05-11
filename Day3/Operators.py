# Arithmatic Operators
from operator import truediv

a=10.0
b=2
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#Relational or comparision operators and Equality Operator
e=10
f=1
print(e>f)
print(e<f)
print(e<=f)
print(e>=f)
print(e==f)
print(e!=f)
print(10<20<20>40)
print(10==30==20!=0)
print("----------")
#logical operator
#boolean
x=True
y=False
print(x and y)
print(x or y)
print(not y)
#Non boolean
#0 and empty string -->false
#non empty string or non zero -->true
#x and y --> if x is false then result is x else it is y
# 10 and 20 --> 20
#x or Y --> if x is true the result is x otherwise y
# 10 or 20 --> 10
#not x
#not 10 --> false
print("example" and "examplesoft")
print("" and "examplesoft")
print("" or "examplesoft")
print("example"and "examplesoft")
print("******88")
#assignment operator
z=10
k=20
# z=z+20
# k=k-10
z+=20
k-=10
print(z)
print(k)
print("&&&&&&&&&&&")
#terinary or conditional operator
"""
action-1 a if condition else b
"""
a="Rashi" if 10>5 else "Lokesh"
print(a)

#special operators
#identity
d=100
g=100
print(id(d))
print(id(g))
print (d is g)
print (d is not  g)
# membership
s=[1,2,3,4,5,6]
print(1 in s)
print(1 not in s)

#Operators Precedence
result=3+6*(5**2)/10-4
print(result)