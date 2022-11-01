#Cesar D. Quihuis-Romero CIS-129 10/28/2022
#The program will take input as string for name, it will then assign a random vaule inform of an interger, declaring the larger number as a "winner"

#import random for random.ranint()
#need TRUE and FALSE for getYesOrNo() 
import random


#def main
def main():
    print()

    #init var
    endProgram = "n"
    playerOne = "NO NAME"
    playerTwo = "NO NAME"
    newGame = "n"
    #call to function inputName
    playerOne, playerTwo = inputName(playerOne, playerTwo)


    while newGame == "n":
    #establish shell while loop
        while endProgram == "n":
        #populate var
            winnersName = "NO NAME"
            p1number = 0
            p2number = 0

        #call to rollDice
            winnersName = rollDice(p1number, p2number, playerOne, playerTwo, winnersName)
        #call to displayInfo
            displayInfo(winnersName)
            newGame = startNewGame()

            newGame = str(input("Do you quit game? (y/n)"))
        endProgram = str(input('Do you want to end program? (yes/no)'))

#function getName or inputName
def inputName(playerOne, playerTwo):
    playerOne = str(input("Enter Player One's name")) 
    playerTwo = str(input("Enter Player Two's name"))
    return playerOne, playerTwo

#function getRandom or rollDice
#def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    #p1number = random.randint(1,6)
    #p2number = random.randint(1,6)
    #while p1number == p2number:
        #reRoll = str(input("Tie. Roll again? (y/n)"))
        #while reRoll != "y" and reRoll != "n":
            #print("Please enter y or n")
            #reRoll = str(input('Tie. Roll again? (y/n)'))
        #if reRoll == "y":
#            print("Rerolling...")
            #rollDice(p1number, p2number, playerOne, playerTwo, winnersName)
        #elif reRoll == "n":
            #print("Thank you for playing")
           # return "Game Over"
    #if reRoll == "y":
    #            print("Rerolling...")
     #   p1number = random.randint(1,6)
     #   p2number = random.randint(1,6)
#issues
def rollDice(p1number, p2number, playerOne, playerTwo, winnersName):
    p1number = random.randint(1,6)
    p2number = random.randint(1,6)
    print(f"{playerOne} rolled a {p1number}")
    print(f"{playerTwo} rolled a {p1number}")
    while p1number == p2number:
        reRoll = str(input("Tie. Roll again? (y/n)"))
        while reRoll != "y" and reRoll != "n":
            print("Please enter y or n")
            reRoll = str(input('Tie. Roll again? (y/n)'))
        if reRoll == "y":
#            print("Rerolling...")
            p1number = random.randint(1,6)
            p2number = random.randint(1,6)
        elif reRoll == "n":
            print("Thank you for playing")
            return "Game Over" 


    if p1number > p2number:
        winnersName = playerOne
    elif p2number > p1number:
        winnersName = playerTwo
    
    return winnersName

#function displayInfo
def displayInfo(winnersName):
    print(f'{winnersName} is the winner!')

def startNewGame():
    newGame = str(input('Do you want to start a New Game? (y/n)'))

    while newGame != "y" and newGame != "n":
        print("Please select y to start a new game or select n to end the game.")
        newGame = str(input('Do you want to start a New Game? (y/n)'))
    if newGame == "y":
        newGame = "y"
        return newGame
    elif newGame == "n":
        print("Thank you for playing")
        endProgram = "yes"
        return endProgram
    
#function to establish a yes or no based on user input return a TRUE or FALSE statement (also .lower formating to all yes and no)
#def getYesOrNo():
#    yes = ["YES", "Y"].tolower 
#    no = ["NO", "N"].tolower


#call to main
main()



