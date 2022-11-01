#CIS 129 Cesar D. Quihuis-Romero 10/23/2022
#Yum Yum Buger Joint 
#Mod 6 EC Lab

#Global
TAX = .06
BURGER_COST = .99
FRY_COST = .79
SODA_COST = 1.09

#def main
def main():
    totalBurger = getBurger(totalBurger, burgerCount)
    totalFry = getFry()
    totalSoda = getSoda()
    total = calcTotal()
    tax = calcTotal()
    subtotal = calcTotal()
    burgerCount = getBurger()
    fryCount = getFry()
    sodaCount = getSoda()

    declareVariables(endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount) 

    endProgram = "no"

    while endProgram == "no":
        resetVariables(totalBurger, totalFry, totalSoda, total, tax, subtotal)

        endOrder = "no"

        while endOrder == "no":
            print("Enter 1 for Yum Yum Burger")
            print("Enter 2 for Grease Yum Fries")
            print("Enter 3 for Soda Yum")

            option = int(input("Please enter your selection"))

            if option == 1:
                getBurger(totalBurger, burgerCount)

            elif option == 2:
                getFry(totalFry, fryCount)

            elif option == 3:
                getSoda(totalSoda, sodaCount)

            endOrder = str(input("Do you want to end your order? (yes/no): "))
        
        calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax)

        printReceipt(total)

        endProgram = str(input("Do you want to end the program? (yes/no): "))
            
def declareVariables(endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount):

    endProgram = "no"
    endOrder = "no"
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    total = 0
    tax = 0
    subtotal = 0
    option = 0
    burgerCount = 0
    fryCount = 0
    sodaCount = 0
    return endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount

def resetVariables(totalBurger, totalFry, totalSoda, total, tax, subtotal):
    totalBurger = 0
    totalFry = 0
    totalSoda = 0
    tax = 0
    subtotal = 0
    return totalBurger, totalFry, totalSoda, total, tax, subtotal

def getBurger(totalBurger, burgerCount):
    burgerCount = int(input("Enter the number of burgers you want"))
    totalBurger += burgerCount * BURGER_COST
    return totalBurger

def getFry(totalFry, fryCount):
    fryCount = int(input("Enter the number of fries you want"))
    totalFry += fryCount * FRY_COST
    return totalFry

def getSoda(totalSoda, sodaCount):
    sodaCount = int(input("Enter the number of sodas you want"))
    totalSoda += sodaCount * SODA_COST
    return totalSoda

def calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * TAX
    total = subtotal + tax
    return total

def printRecipt(total):
    print('Your total is $', total)

main()

