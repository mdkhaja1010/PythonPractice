#Tuple
"""
Tuple is same as list but tuple is immutable once you cannot the content in tuple but you cannot change
i.e., increase the size or decrease the size
Tuple is read only version of list
If we want to represent a group of individual objects as a single entity where insertion preserved and duplicates
are allowed then we should go for list,
Hetrogenous objects
Index-->supports +ve and -ve
Not dynamic
in tuple data represent in () and seperated by comma
"""
#creation of tuple
t=() #emplty tuple paranthesis is optional
t=(10,)#single valued tuple
t=10,10,True,"welcome",10+40j
t1=tuple(range(11))
print(t)
print(type(t))
print(t1)
print(type(t1))
# t2=eval(input("enter tuple: "))
# print(t2)
# print(type(t2))
s="learning python is very easy"
s1=tuple(s.split())
print(s1)

#access data 1) index 2) slice operator
t3=(10,20,30,40,50)
print(t3[2])
print(t3[-1])
#slice operator
print(t3[2:4])
print(t3[3:9])
print(t3[::-1])
#t3[0]=999 #tuple is immutable you cannot change the tuple
#operators in tuple
x=(1,2,3,4,5)
x1=(6,7,8,9,0)
print(x+x1)
#print(x1*2)
print('a'in x1)
print('a' not in x1)
#important function on tuple
#except -->append, insert, remove, pop, extend other all methods are available
print(len(x1))
print(x1.count(9))
print(x1.index(8))
print(sorted(x1))
print(sorted(x1, reverse=True))
print(min(x1))
print(max(x1))
# tuple packing and unpacking
"""
tuple packing is the process of combining multiple values into a
single tuple in a single statement
Tuple unpacking is the process of assigning the values from
a tuple to multiple variables ina single statement
Tuple unpacking is the reverse process of tuple packing
During tuple unpacking the number of variables must match the number
of values otherwise a valueerror will occur
"""
# tuple packing
a=10
b=20
y=(a,b)
print(type(y))
print(y)
z=10,20,30
z1,z2,z3=z #tuple unpacking

#Tuple comprehension
#Not supported in python
    #syntax (experssion for item in sequence if condition)--> generator object
t=[x**2 for x in range(1,6)]
print(t)
print(type(t))

t=(x**2 for x in range(1,6))
print(t)
print(type(t))
