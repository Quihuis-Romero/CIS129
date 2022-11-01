import random

def main():
    endProgram = "n"
    endGame = "n"
    reRoll = "n"
  

    while endProgram == "n":

        while endGame == "n":
            winnersName = "NO NAME"
            p1Name, p2Name = inputName()
            p1Number = 0
            p2Number = 0
            while reRoll == "n":
                winnersName = rollDice(p1Number, p2Number, p1Name, p2Name)

                displayInfo(winnersName)

                reRoll = getReRoll()

        endGame = getEndGame()

    endProgram = getEndProgram()

def inputName():
    p1Name = str(input("Enter Player One's name: "))
    p2Name = str(input("Enter Player Two's name"))
    return p1Name, p2Name

def rollDice(p1Number, p2Number, p1Name, p2Name):
    p1Number = random.randint(1,6)
    p2Number = random.randint(1,6)

    print(f"{p1Name}'s number is {p1Number}")
    print(f"{p2Name}'s number is {p2Number}")

    while p1Number == p2Number:
        print("TIE")
        reRoll = str(input('Roll again? (y/n)'))

        while reRoll != "y" and reRoll != "n":
            reRoll = str(input('Roll again? (y/n)'))
        if reRoll == "y":
            print('Rerolling...')
            continue
        elif reRoll == "n":
            print('Thank You for Playing!')
            break
    if p1Number > p2Number:
        winnersName = p1Name
    elif p2Number > p1Number:
        winnersName = p2Name

    return winnersName

def getEndGame():
    endGame = str(input('Do want to end the game? (y/n)'))
    return endGame

def getEndProgram():
    endProgram = str(input('Do you want to end the Program? (y/n)'))
    return endProgram

def getReRoll():
    reRoll = str(input('Do you want to reRoll? (y/n)'))
    return reRoll

def displayInfo(winnersName):
    print(f'{winnersName} is the winner!')

main()