# occurances of each character
word="madam"
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
for k,v in d.items():
    print(k, "occured", v, "times")
