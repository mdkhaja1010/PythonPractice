"""
functions in python
Lamda functions: for instant usage i.e. for one time task we can go for lambda function
it is also anonymous or nameless functions
by default lambda functions return result automatically
syntax
lambda argument_list:expression
arguments for Higher order function--> Map(), Filter(), reduce()
"""
#calculate a square of a number
def square(a):
    print (a*a)
square(10)
#lambda function
s=lambda a:a*a
print(s(100))
#lambda 10:10*10 it is not possible

#sum of 2 numbers
def sum(a,b):
    print (a+b)
sum(10,20)
k=lambda a,b:a+b
print(k(10,30))
# find biggest of 2 numbers
def big(a,b):
    if(a>b):
        print(str(a)+" a is larger")
    else:
        print(str(b)+" b is larger")

big(10, 20)

f=lambda c,d:c if c>d else d
print(f(20,60))

#filter function
"""
filter values from given sequence based on condition
syntax--> filter(function, sequence)
"""
l=[10,15,20,25,30,40,50,60]
#Normal function
# def isEven(l):
#     if l%2==0:
#         return True
#     else:
#         return False
# print(list(filter(isEven,l)))
#lambda function
print(list(filter(lambda x:x%2==0,l)))
print(list(filter(lambda x:x%2!=0,l)))

#Filter employees with salary >50000

employees=[{'name':'Alice','salary':60000}, {'name':'Bob','salary':40000}]
print(list(filter (lambda emp:emp['salary']>50000, employees)))


