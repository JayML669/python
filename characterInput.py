yearsAdd = 0;
name = input("Enter Your Name: ")
age = int(input("Enter You Age: "))
thisYear = input("Will you turn " + str(age +1) + " this year?(y/n) ")
repeat = int(input("Whats Your Favorite Number? "))
if thisYear == "y":
    yearsAdd = 99
elif thisYear == "n":
    yearsAdd = 100
else:
    print("Thats Not y or n")
    exit();
    
birth = 2017-age
year100 = birth + yearsAdd


print(repeat * ("Hi " + name + " you will turn 100 in " + str(year100) + "!\n"))
    


