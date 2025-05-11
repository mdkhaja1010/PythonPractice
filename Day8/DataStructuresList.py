#Data Structure in Python--List
"""
Group of individual objects as a single entity where
insertion order preserved and
duplicates are allowed then we should go for list
Hetrogeneous objects in list data structure.
Dynamic with respect to the size
list data Structure is mutable
index --> +ve and -ve
Square braces--> individual objects
"""
#creation of lists
#list1=["khaja","london",20000.12,8434343]#empty list
#list2=eval(input("enter data: "))
list2 =list(range(11))
print(list2)
print(type(list2))
s="learning python is very easy"
list3=s.split()
print(list3)

#Access elements inside the list
#index
#slice operator
print(len(list3))
print(list3[4])
print(list3[-1])
#slice operator
print(list3[1:3:2])
list3.append(909)
print(list3[1:4:2])
print(list3)
list3[5]=1000
print(list3)
print("*****************")
#Traversing
#sequencial access of each element inside a list
for x in range(len(list3)):
    if "easy"==list3[x]:
        print(list3[x])
#functions
sample=[10,20,30,40,50,10]
print(len(sample))
print(sample.count(10))
sample.append(10)
print(sample)
sample.insert(1,20)
print(sample)
sample.extend(list3)
print(sample)
sample.remove(20)
print(sample)
print("((((((")
sample.pop()
sample.pop(4)
print(sample)
sample.reverse()
print(sample)
# sample.sort()
# print(sample)
sample.clear()
print(sample)
#remove multiple items
print("))))))))))))))))))))))))")
list4=[10,20,30,40,70,]
list5=[20,60,50,90,80,20,30]
for y in list5:
    if y in list4:
        list4.remove(y)
print(list4)
#Aliasing & cloning
"""
THe process of giving another reference variable to the existing list is called aliasing
the problem in this approach is by using one reference 
variable if we are changing content, the those chages will 
be reflected to other reference variable
"""
slist=[1,2,3,4]
y=slist
y[1]=77
print(slist)
print(y)
print("&&&&&&&&&")
#cloning
s1=[9,1,4,5,0]
s2=s1[:]#s2=s1.copy()
s2[1]=12
print(s1)
print(s2)
#operators
#concatination & repitation
n1=[10,20]
n2=[30,40]
print(n1+n2)
print(n1*2)
#membership operator
print(10 in n1)
print(10 not in n1)
#nested list
mylist=[10,[20,40],[50,60,70]]
print(mylist[0])
print(mylist[1])
print(mylist[1][1])
print(mylist[2][2])
#list comprehension
"""
it is very easy and compact way of creating list objects from any
any iterable objects(like list, tuple, dictionary, range etc) based on some condition.
"""
list9= [x*x*x for x in range(11) if x%3==0]
print(list9)

words=["kit","hight","apple","jam","avacado"]
l=[word[0] for word in words]
print(l)

