num = int(input("What Number Woud You Like To Test Divisibilty For? "))
div = int(input("What Number Would You Like To Test The Number With? "))

if num % div == 0:
    ans = (str(num) + ", Is Divisible By " + str(div))
else:
    ans = (str(num) + ", Is Not Divisible By " + str(div) + " But It Is")

if num % 2 == 0:
    ans += " Even"
else:
    ans += " Odd"
    
if num % 4 == 0:
    ans += " And Divisible By Four"

print("The Number You Input, " + ans +"!")
