#functions in python:
'''
if a group of statements is repeatedly required then it is not recommended
to write these statements everytime seperately. We have to define these
statements as a single unit and we can call that unit any number of times based on our
requirement without rewriting. this unit is nothing but function.
A function is a set of statements upon calling performs certain task
avoid below issues using functions
Memory Issue
Code Duplication
Code Maintanance
Function and Method are different in python
Types of Functions
1) Built in Functions
     print(),id(), type(),eval(), int(), etc.,
2) User defined functions
  programmers develop functions explicitly according to business requirements
Syntax of user defined functions
-------------------------------
def function(inputs or parameters):
    statement1
    statement2.....
    return result
inputs or parameters and return are optional
parameters --> inputs to the funtion
Arguments--> Actual values passed to input during the function call
'''
#function declarion
def sample_function():
    """This is a sample message to print the message"""
    print("hello world")
#function declaration or invocation
sample_function()


def sample_function(name):
    print(f"hello world {name} ")

sample_function("Khaja")

def add(a,b):
    return a+b
print(add(3,4))
"""
Functions with 
1) No arguments No return value
2) With arguments No return value
3) With arguments with return value
4) No arguments with return value
"""
#1) No arguments No return value
def myfunc():
    print("function with no return and no argument")
# x=myfunc()
myfunc()
print(myfunc())
#2) With arguments No return value
def myfunc1(name):
    print(f"function with argument No return value {name} to the value")
myfunc1("khaja")
print(myfunc1("khaja"))
#3) With arguments with return value
def myfunc2(name):
    return f"hello {name}"
x=myfunc2("khajas")
print(x)
print(myfunc2("khajasss"))
#4) No arguments with return value
def myfunc3():
    x=10
    y=20
    return x+y
z=myfunc3()
print(z)
print(myfunc3())

#python function return any number of values in the form of tuple
def myfunc4():
    return "hello khaja","hellow Manohar","hellow Prashanth"
print(myfunc4())