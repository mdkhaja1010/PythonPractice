#Dictionary Data Structure
"""
List, Tuple, Set--> represent individual objects as entity
Dictionary--> represent individual objects as a key-value pairs --> Dictionary
Duplicate keys are allowed, but duplicates values are allowed
hetrogenous objects
insertion order is preserved
Dynamic and mutable behaviour
indexing and slicing are applicable for dictionary
key--> is the gateway
if the specific key is not available then we get key error
if the key is not available then a new entry will be added to the dictionary with specified key value pair
if the key is already available then old value will be replaced with the new value.
"""
#creation of dictionary
d={}#empty curly braces
d=dict() #we can use this also
d[100]="kiran"
d[200]="ravi"
d[300]="kiran"
#d[300]="deep"
c={1:"khaja",2:"manohar",3:"prashanth",4:"bhanu"}#elements in advance
print(d)
print(type(d))
print(c)
print(type(c))
#access data from the dictionary
print(c[2])
if 8 in d:
    print(d[9])
c[2]="manohar reddy"
print(c)
c[5]="sai"
print(c)
#Delete data or remove the data from the dictionary
del(c[5])#deleting particular object
print(c)
# c.clear()#clearing entire data
# print(c)
#del c #deleting entire dictionary object
#functions or methods in dictionary
'''
len()
clear()
d.get(key) <==> d[key]
    returns None
d.get(key, default value)
    returns default value
'''
e=len(c)
print(e)
print(type(e))
s=c.get(2)
print(s)
print(type(s))
print(c.get(6))
print(c.get(6,"kjjas"))
#pop(key)-->key error
#popitem(c)--> remove random entry
# c.pop(2)
# print(c)
# print(c.popitem())
# print(c)
#keys()
#values()
#items()--> returns key and value pairs
print(d.keys())
print(d.values())
print(d.items())
d1=d.copy()
print(d1)
d.update({400:"dups",500:"Khaja"})
print(d)

#dictionary comprehension
f={x:x*x for x in range(1,6)}
print(f)







