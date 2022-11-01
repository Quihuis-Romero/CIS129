

#glboal
TAX = .06
B_COST = .99
F_COST = .79
S_COST = 1.09


def main():
    endProgram = declareVariables(endProgram, endOrder, totalBurger, totalFry, totalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount)
    endOrder = declareVariables(endOrder)
    while endProgram == "no":
        endOrder = declareVariables(endOrder)
        resetVariables(totalBurger, totalFry, totalSoda, total, tax, subtotal)

        while endOrder == "no":
            print("Enter 1 for Yum Yum Burger")
            print("Enter 2 for Grease Yum Fries")
            print("Enter 3 for Soda Yum")

            option = int(input('Enter your selection: ')) 

            if option == 1:
                burgerCount = declareVariables(burgerCount)
                totalBurger = resetVariables(totalBurger)
                burgerOrder = getBurger(totalBurger, burgerCount)
                return burgerOrder
            elif option == 2:
                fryCount = declareVariables(fryCount)
                totalFry = resetVariables(totalFry)
                fryOrder = getFry(totalFry, fryCount)
                return fryOrder
            elif option == 3:
                sodaCount = declareVariables(sodaCount)
                totalSoda = resetVariables(totalSoda)
                sodaOrder = getSoda(totalSoda, sodaCount)
                return sodaOrder
            endOrder = str(input('Do you want to end your order? (yes/no):'))
        total = resetVariables(total)
        tax = resetVariables(tax)
        subtotal = resetVariables(subtotal)
        calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax)
        printReceipt(total)

        endProgram = str(input('Do you want to end the program? (yes/no):'))


def declareVariables(endProgram, endOrder, totalBurger, totalFry, TotalSoda, total, tax, subtotal, option, burgerCount, fryCount, sodaCount):
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
    total = 0
    tax = 0
    subtotal = 0
    return totalBurger, totalFry, totalSoda, total, tax, subtotal

def getBurger(totalBurger, burgerCount):
    burgerCount = int(input('Enter the number of burgers you want'))
    totalBurger += burgerCount * B_COST
    return totalBurger, burgerCount

def getFry(totalFry, fryCount):
    fryCount = int(input('Enter the number of fries you want'))
    totalFry += fryCount * F_COST
    return totalFry, fryCount

def getSoda(totalSoda, sodaCount):
    sodaCount = int(input('Enter the number of sodas you want'))
    totalSoda += sodaCount * S_COST
    return totalSoda, sodaCount
def calcTotal(totalBurger, totalFry, totalSoda, total, subtotal, tax):
    subtotal = totalBurger + totalFry + totalSoda
    tax = subtotal * TAX
    total = subtotal + tax
    return total, subtotal, tax
def printReceipt(total):
    print('Your total is $', total)




















main()