name="ETE"
rev=""
for i in range(len(name)):
    rev=name[i]+rev

print("rev", rev)
if name==rev:
    print("the string is palindrome")
else:
    print("the string is not palindrome")