#set Data structure
"""
list, tuple--> group of values as a single entity
set--> group of unique values as a single entity
Duplicates are not allowed
insertion order is not preserved
indexing and slicing is not supported to access the data
supports homogenous and hetrogenous objects are allowed
Mutable once declare set we can increase or decrease by size
inside {} we can declare element and seperated by ,
"""
#Creation of Set Objects
#s={} #empty set is not possible for empth set you need to write set()
#s=set()# empty set
s={10,"welcome",True,"c",10+5j,10,10.5}# elements in advance duplicates are not allowed in output

print(s)
print(type(s))
# t=eval(input("enter set data :"))#dynamic set creation
# print(t)
# print(type(t))
s1=set(range(11))
print(s1)
#functions on set
set1={10,20,30}
print(set1)
set1.add(40)
print(set1)
set1.update([20,40,50,60])
print(set1)
s2=set1.copy()
print(s2)
set1.add(90)
print(set1)
print(s2)
#access to data in set indexing and slicing is not supported
#pop() it removes and returns some random element from the set
#remove() it removes specified element from the set and if the specified element not present in the set then we will get key error
#discard() it removes specified element from the set and if the specified element not present in the set then we won't get any error
#clear() to remove all elements from the set
#print(set1.pop())
set1.remove(30)
print(set1)
#set1.remove(100) #if the element is not available it throws key error
set1.discard(100) #if the element is not available discard won't throw any error
set1.clear()
print(set1)
#Mathematical operators on set
"""
on multiple sets we can apply this operators
union() to return all the elements in the set
intersection() to return only common elements
differece() to return the elements in the first set not in the second set
symmetric_difference() to return the elements either in x and y we can use this
"""
x={10,20,30,40}
y={40,50,60,70}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(y.difference(x))
print(x.symmetric_difference(y))
print(300 in x)
print(300 not in x)
#set comprehension
z={k*k for k in range(10)}
print(z)


