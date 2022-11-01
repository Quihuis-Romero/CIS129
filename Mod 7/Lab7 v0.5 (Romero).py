#Lab7 v0.4 
#Cesar D. Quihuis-Romero
#v.5
    #cleaned up getYesOrNo(), did not need extra question.
#v0.4 (more like 0.6)
    #v0.4 added a lot
    #yesorno() works
    #custom user prompt for quitting game, new game, and exiting program. 
    #bad stuff still happens when input other then y/Y and n/N
#v0.3 and bellow
    #did a poor job of commenting out old code I wanted to leave it looking clean
    #i should have captured some of the jumps that i hade to get the product to work the way it does

import random

#def of main
def main():
    #baselines
    endProgram = False
    endGame = False
    p1name = "P1"
    p2name = "p2"
    p1number = 0
    p2number = 0
    winnerName = "NO NAME"
    #first loop (program space)
    while endProgram == False:
            #second loop (game space)
            while endGame == False:
                #update baseline from functions (get user input)
                p1name = getP1Name()
                p2name = getP2Name()
                #roll//resolve the rolls
                p1number = p1roll()
                p2number = p2roll()
                #calc winner//resolve the winner
                winnerName = rollDice(p1name, p2name, p1number, p2number)
                #print results
                displayWinner(winnerName)

                #first quit for easy new game reset
                endGame = getYesOrNo("Do you want to quit the game? (y/n)")
            #second to leave game space    
            endGame = getYesOrNo("Do you want to start a new game? (y/n)")
            if endGame == True:
                endGame = False
                continue
            #third to leave program   
            endProgram = getYesOrNo("Do you want end the program? (y/n)")
#input user input formate it to lower and check against my def of yes and no 
#bad input should get screened out and only yes or no passes
def getYesOrNo(prompt):
    yesNo = str(input(prompt)).lower()
    while yesNo != "y" and yesNo != "n" and yesNo != "yes" and yesNo != "no":
        yesNo = str(input(prompt)).lower()
        
    if yesNo == "y" or yesNo == "yes":
        return True
    elif yesNo == "n" or yesNo == "no":
        return False
#get name// i separated into two to ensure only one date piece is returned at a time
def getP1Name():
    p1name = str(input("Enter Player One's Name: "))
    return p1name
def getP2Name():
    p2name = str(input("Enter Player Two's Name: "))
    return p2name
#rolls//i separated into two for same reason as name
def p1roll():
    p1roll = random.randint(1,6)
    return p1roll
def p2roll():
    p2roll = random.randint(1,6)
    return p2roll
#resolve the dice roll to see who won, added a print to show player the results of their roll
def rollDice(p1name, p2name, p1number, p2number): 
    print(f"{p1name} rolled a: {p1number}")
    print(f"{p2name} rolled a: {p2number}")

    if p1number == p2number:
        print("TIE")
    elif p1number > p2number:
        winnerName = p1name
        return winnerName
    elif p2number > p1number:
        winnerName = p2name
        return winnerName
#display the winner
def displayWinner(winnerName):
    print(f'{winnerName} is the winner!')
#call to main
main()