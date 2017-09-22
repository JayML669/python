import random

a=[]
b=[]
lists = [a,b]
c=[]

for element in lists:
    for x in range(10):
        element.append(random.randint(1,100))
print(str(a))
print(str(b))



for element in a:
    if not element in c:
        if element in b:
            c.append(element)
        
    

    

print(str(c))
        
