#s=""
s=''

print(type(s))
k="123"
print(type(k))
o=123
s=str(o)
print(type(s))
n="""welcome 
to 
testing"""#''' sting ''' are used some times
print(n)

#p="welcome to \"python\""
p="welcome to 'python'"
print(p)
i="welcome to"
#accessing characters inside the string
print(i[4])
print(i[-10])
print(len(i))
for x in range(0,len(i),1):
    print(str(x)+"hello")
#slice operator
#s[begin index:end index:step]--s[10:100:1]-->10--starting, 100-->Ending
u="learning python is very easy"
print(u[1:7:1])
print(u[1:7])
print(u[1:7:2])
print(u[:7])
print(u[7:])
print(u[::])
#if end index is out of range then slice operator will never raise index error rather it will consider full string staring from begin index in both forward and reverse directions
print(u[0:100:1])
print(u[::-1])
print(u[3:7:-1])#if a start index is lessthan the end index in the forward direction there is no print
print(u[7:3:1])
print(u[7:7:-1])
"""
@@ if start index < end index in backward direction then result is always empty
@@ if start index > end index in forward direction then result is always empty
@@ if start index == end index in both directions then result is always empty.
"""
