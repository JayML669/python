a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
test = []

choice = input("Hello, welcome to Less Than Ten. Would you like to test your own list or use the program's built in list? (u for user/p for program) \n" )

if choice == "p":
    test.append(a)
elif choice == "u":
    limit = int(input("What would you like the length of your limit to be? \n" ))
    for i in range(limit):
        num = int(input("Enter a number \n" ))
        test.append(num)
div = int(input("What Number would you like to test the lsit with? \n" ))        


for element in test:
    if element < div:
        b.append(element)
print(b)
