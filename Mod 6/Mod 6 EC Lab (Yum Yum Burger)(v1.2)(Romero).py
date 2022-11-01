
import time 

TAX = .06
B_COST = .99
F_COST = .79
S_COST = 1.09

def main():
    endProgram = "no"
    while endProgram == "no":
        endOrder = "no"
        while endOrder == "no":
            customerOrder = getCustomerOrder(numBs, numFs, numSs, total)
            total = getTotal(total)
            totalwTax = total * TAX
            print(totalwTax)

def getCustomerOrder():
    numBs = 0
    numFs = 0
    numSs = 0

    num1 = "#1: Yum Yum Burger $.99"
    num2 = "#2: Yum Grease Fries $.79"
    num3 = "#3: Soda Yum $1.09"
    array1 = [num1,num2,num3]
    print(array1)
    time.sleep(2)
    print("Welcome to Yum Yum Burger!")
    time.sleep(1)
    print("Home of the Yum Yum Burger!")
    time.sleep(1)
    print("Voted #1 dumb yum Burger 4 years in a row!")

    input = int(input('Enter order number: (#1,#2,#3)'))
    if input == 1:
        check = str(input('Did you want a Yum Yum Burger? (y/n)'))
        if check == 'y':
            burgerOrder = getBurgerOrder(numBs)
            return burgerOrder
        elif check != 'y':
            error1 = getBadCheck()
            return error1
    elif input == 2:
        check = str(input('Did you want Yum Grease Fries? (y/n)'))
        if check == 'y':
            fryOrder = getFryOrder(numFs)
            return fryOrder
        elif check != 'y':
            error2 = getBadCheck()
            return error2   
    elif input == 3:
        check = str(input('Did you want a refreshing Soda Yum? (y/n'))
        if check == 'y':
            sodaOrder = getSodaOrder(numSs)
            return sodaOrder
        elif check != 'y':
            error3 = getBadCheck()
            return error3
    elif input == 4:
        print('Select a valid option from the menu')
        #return to start

    

def getBurgerOrder(numBs):
    numBs = int(input('Enter the number of bugers for your order:'))
    return numBs
def getFryOrder(numFs):
    numFs = int(input('Enter the number of fries for your order:'))
    return numFs
def getSodaOrder(numSs):
    numSs = int(input('Enter the number of sodas for your order:'))
    return numSs
def getBadCheck(input):
    input = 4
    return input
def getTotal(numBs, numFs, numSs):
    costOfBurgers = numBs * B_COST
    costOfFrys = numFs * F_COST
    costOfSoda = numSs * S_COST
    total = costOfBurgers + costOfFrys + costOfSoda
    return costOfBurgers, costOfFrys, costOfSoda, total







main()