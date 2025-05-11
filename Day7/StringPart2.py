#Mathematical operators
'''
+====concationation--> while concating both are strings
*---Repitition--> one arguement must be string  and other must be integer
'''
s="Welcome"
s1="to python programming"
print(s+s1)
s2=s1*10
print(s2)
s3=s+str(1)
#Len()--> returns the length of the string
print(len(s3))
#presence of characters or substring in main string
#Identiy is, is not
#Membership-->in, not in
print("o" in s3)
print ("W" not in s3)
#remove spaces in python
"""
rstrip()-->right hand side spaces remove
lstrip()-->left hand side spaces remove
strip()--> both hand spaces
"""
s4=" welcome to python string "
print(s4.strip())
print(s4.lstrip())
print(s4.rstrip())
#comparison of strings
"""
Lexicographically -->Comparison will be done in ASCII American standard code for Information interchange
first character comparison will be done 
ord()--> based on character return ASCII code
chr()--> based on ASCII return character
"""
print(ord("J"))
print(chr(74))
n1="Bharath"
n2="Bhushan"
print(n1<n2)
print(n1==n2)

#Find SubStrings:
"""
find()-->index of first occurance of substing
if substring is not available return -1
index()--> same as find()-->Error if not found
rfind()--> index of last occurance of substring--> -1 if not found
rindex()-->same as rfind -->Error if not found
"""
k="python is very very easy"
print(k.find("very"))
print(k.rfind("avery"))
print(k.index("very"))
print(k.rindex("very"))

# count() method returns number of times substring occurs
print(k.count("easy"))
# replace() a substring in main string
l="learning python is very difficult"
l1=l.replace("difficult","easy")#changing in data
print(l)
print(l1)
#splitting --> return list and joining the strings
"""
date=01/01/2023
"""
date="01/01/2023"
date1="welcome to python"
print(date1.split())
print(date.split("/"))
# join --> sequence --> list, tuple, set, dictionary
f=['welcome', 'to', 'python']
f1="@".join(f)
print(f1)
"""
change the case
upper()=> converts all characters to upper case
lower()=> converts all characters to lower case
swapcase()=> converts all lower case characters to uppercase and vice versa
title()=> converts all character to title case i.e first character in every word should be upper
capitalize()=> only first character will be converted to upper case and all remaining characters can be converted to lower case
"""
y="welcom to testing"
print(y.upper())
print(y.lower())
print(y.swapcase())
print(y.capitalize())
print(y.title())

"""
Check type of characters
isalnum()=> returns True if all characters are alphanumberic (a to z, z to a, 0 to 9)
isalpha()=> returns True if all characters are only alphabet symbols (a to z, A to Z)
isdigit()=> returns True if all characters are digits only(0 to 9)
islower()=> returns True if all characters are lower case alphabet symbols
isupper()=> returns True if all characters are upper case alphabet symbols
istitle()=> returns True if all characters is in title case
isspace()=> returns True if all characters if string contains only spaces
"""
print("priya988".isalnum())
print("priya988".isalpha())
print("priya".isalpha())
print("2323".isdigit())
print("sdfs".isdigit())
print("abc".islower())
print("ABC".isupper())
print("Learing python".istitle())
print("Learning Python".istitle())
print(" ".isspace())

#String formatting
"""
String formatting ensures that the information is presented in a clear readable and organized manner
f-strings
format()+{}
"""

print("my name is mohan, salary is 25000 located in london")
name="khaja"
salary=49999
country="India"
print(f"my name is {name}, salary is {salary} located in {country}")
print("my name is {}, salary is {} located in {}".format(name,salary, country))



