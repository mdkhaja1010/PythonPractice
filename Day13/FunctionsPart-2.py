"""
Types of Arguments
1) Positional Arguments
2) Keyword Arguments
3) Default Arguments
4) Variable Length Arguments
5) Keyword Variable Length Arguments
"""
# 1) Positional Arguments:
#Agruments passed to a function in correct positional order
#Changing order will change the results or errors
def myfun(i,j):
    print(i/j)
myfun(10,20)
myfun(20,10)
# 2) Keyword Arguments
#Arguments with parameter names are called the Keyword arguments
#Order does not matter but count matters
def myfun1(i,j):
    print(i/j)

myfun1(i=10, j=20)
myfun1(j=20, i=10)
#3) Default Arguments
#Assign default values to parameters
#after default arguments we should not take non default arguments, otherwise we will get syntax error.
# if not provided during function call default values are considered
def withs(name="sunny", msg="leone"):
    print("hello", name, msg)
withs()
withs(msg="goodmorning")
withs("khaja",msg="goodmorining")

def sum(*n,n1):
    print(n)
sum(10,20,30,n1=20)

#4) Variable Length Arguments
#length of parameters is not fixed we can pass any number of arguments(even zero) using *.
#values are stored as a tuple.
#After variable length they must be keyword arguments
def variableLen(*n):
    print(n)
variableLen()
variableLen(10)
variableLen(10,20,30)

def order_pizza(size, *toppings):
    print(f"ordered a {size} pizza with the following toppings: {', '.join(toppings)}.")

order_pizza("medium")
order_pizza("large","pepper","mushrooms","olives")
#5) Keyword Variable Length Arguments
"""
use **kwargs for keyword variable length arguments
it stores arguments as a dictionary with keys and values
"""
def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
    print(kwargs)

display(a=10,b=20,c=30)
display(k=10,j=100,i=300)

def create_user_profile(name, age, **additonal_info):
    profile={
        "name": name,
        "age": age
    }
    profile.update(additonal_info)
    print("user profile: ", profile)
create_user_profile("khaja",30, loction="chennai",Area="addambakkam",pincode="521001")
"""
Types of functions
A function can take anaother function as an argument
return another function as  result
1) First-Order Functions
Do not take functions as arguments
Do not returns a function as its result
Only operate on basic data types
2) Higher Order Functions
A function takes one or more functions as arguments returns as a function as its result
map(), filter(),reduce()
3) First Class functions
A function assigned to variables (i.e, treated as a value). passed as arguements to other functions
returned from other functions.
"""
#first order function
def myfun1(i,j):
    print(i/j)

myfun1(i=10, j=20)
myfun1(j=20, i=10)
#Higher order functions
def apply(func,value):
    return func(value)
def square(num):
    return(num**2)
print(apply(square,100))

#first class functions
def greet(name):
    return f"hello, {name}!"
greet_func=greet #assigning function to variable
print(greet_func("MADHAN"))
"""
Function vs Module vs Library(package)
A group of lines with some name is called a function
A group of functions saved to a file is called module(.py file)
A group of module is nothing but library or package
"""
#Types of vairables of function
"""
1) Global variable
    declared outside of a funciton and accessible in all functions of a module
    with the help of global key word to make a local variable to global variable
2) Local Variable
    Declared inside a function and accessible only within that function
"""
company_Name="TechCorp" #global variable
def employeeDetails():
    global employeeName #making local variable to global variable
    employeeName="john Doe"#local variable
    print(f"employee: {employeeName}, Company: {company_Name}")
def company_info():
    print(f"welcome to the {company_Name}!")
    print(employeeName)
employeeDetails()
company_info()