import random

games = 0

win = False
tie = False

choices = ["Rock","Paper","Scissors"]

while True:
    if games > 0:
         command = input("Would you like to play another game of Rock, Papper, Scissors? (y/n) \n")
    else:
         command = input("Would you like to play a game of Rock, Papper, Scissors? (y/n) \n")
        
    
    if command == "n":
        break
    elif command == "y":
        
        name1 = input("What's your name?\n")

        while True:
            

            choice = input(name1 + ", what would you like to play (Rock, Paper, or Scissors)\n")
            
            if choice in choices:

                opponentChoice = choices[random.randint(0,2)]

                if choice == "Rock" and opponentChoice == "Scissors" or choice == "Paper" and opponentChoice == "Scissors" or choice == "Scissors" and opponentChoice == "Paper":
                    win = True
                elif choice == opponentChoice:
                    win = False
                    tie = True
                else:
                    win = False

                break
            
            else:
                print("Thats not Rock, Papper, or Scissors. Check your spelling and make sure that the first letter is capitolized.\n")
                
        if win == True:
            print("Congrats! You Won! You picked " + choice + " and your opponent picked " + opponentChoice +"!\n")
            
        elif win == False:
            if tie == True:
                print("It was a tie. You picked " + choice + " and your opponent picked " + opponentChoice +"!\n")
            else:
                print("You Lost! You picked " + choice + " and your opponent picked " + opponentChoice +"!\n")
        print("********************************************************************************\n")
        games = 1

        
    else:
        print("Thats not y or n! :p")
