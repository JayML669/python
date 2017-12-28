from random import *
 
miamisafe=True
grow = False
reprint = False
miamiXPosition=2
miamiYPosition=5
hurricaneXPosition=randint(25,29)
hurricaneYPosition=randint(25,29)
while miamisafe==True:
       
        for y in range(30):
            for x in range(30):
                if x==miamiXPosition and y==miamiYPosition and x!=hurricaneXPosition and y!=hurricaneYPosition:
                    print("M",end="")
                elif x==hurricaneXPosition and y==hurricaneYPosition:
                    print("@",end="")
                elif x - hurricaneXPosition ==-1 and grow ==  True and y == hurricaneYPosition or x-hurricaneXPosition ==1 and grow ==  True and y == hurricaneYPosition:
                    print("@",end="")
                elif y - hurricaneYPosition ==-1 and grow ==  True and x == hurricaneXPosition or y-hurricaneYPosition ==1 and grow ==  True and x == hurricaneXPosition:
                    print("@",end="")
                else:
                    print(".",end="")
 
            print()
        input("Hit return to continue")
        if hurricaneXPosition>miamiXPosition:
            hurricaneXPosition-=randint(1,3)
        elif hurricaneXPosition<miamiXPosition:
            hurricaneXPosition+=randint(1,3)
           
        if hurricaneYPosition>miamiYPosition:
            hurricaneYPosition-=randint(1,3)
        elif hurricaneYPosition<miamiYPosition:
            hurricaneYPosition+=randint(1,3)
       
        growthchance=randint(0,10)
        if growthchance == 8:
            grow = True

        distanceX = miamiXPosition - hurricaneXPosition
        distanceY = miamiYPosition - hurricaneYPosition
           
        if miamiXPosition == hurricaneXPosition and miamiYPosition == hurricaneYPosition or grow == True and abs(distanceX) + abs(distanceY) == 1:
            miamisafe = False
        
            
        if grow == True and reprint == False:
            print("The Hurricane Has Grown")
            reprint = True
           

print("MIAMI HAS BEEN DESTROYYEEDDDD")
