#range
print(list(range(10)))
print(list(range(5,10)))
print(list(range(5,10,1)))
print(list(range(2,10,2)))
print(list(range(10,1,-2)))
print(list(range(10,1,1)))

#for loop
#print(1 to 10)
for x in range(1,10):
    print(x)
#even numbers printing
for y in range(0,10):
    if(y%2==0):
        print(y)
for z in range(1,15,2):
    print(z)
#print each characters
s="sunny Leone"
for k in s:
    print(k)
for l in range(10):
    print("khaja"+" "+str(l))

#nested for loop
for m in range(1,5):
    for n in range(1,8):
       print(f"{m} x {n} = {m*n}", end="\t")
    print()
#Transfer statements:
cart=[10,20,600,90,100,800]
for product in cart:
    if product>500:
        print("insurance required "+ str(product))
        break
    print(product)
print("****************")
cart1=[10,20,600,90,100,800]
for item in cart1:
    if item>500:
        print("insurance required "+ str(item))
        continue
    print(item)

print("&&&&&&&&&&&&&&&&&&&&&&")
cart2=[10,20,600,90,100,800]
for item2 in cart2:
    if item2>500:
        print("insurance required "+ str(item2))
        pass
    print(item2)
print("@@@@@@@@@@@@@@@@@@@@@@")
cart3=[10,20,10,90,100,12]
for item3 in cart3:
    if item3>500:
        print("insurance required "+ str(item3))
        break
else:
    print("No insurace required")
