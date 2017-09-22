z=0
y=[]
num=int(input("what number would you like to find the divisors for?\n"))
x=range(1,num+1)
for element in x:
    if num%element==0:
        y.append(element)
print(y)


for element in y:
    z += element

if z - num > num:
    print(str(num) + " is an abundant number!")
