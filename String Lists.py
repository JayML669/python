string = input("What word would you like to test the palindromey-ness of?\n")
string=str(string)

pal=string[::-1]


if pal == string:
    print("That word is a palindrome!")
else:
    print("That word is not a palindrome")
    
