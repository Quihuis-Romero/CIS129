#global
import math
import time
#do close loop with a yes codition and != yes or != no
#how correct bad input
    #I would like to clean up yes and no with getYesorNo() as outlined in main, but requires more work

#version control
#v1.5 (caputres 1.3 and 1.4)
#        corrected some of the loops, implament safe guards for bad order number and resets in bad order reaches calculation
#v0.0 series 
    #all moddeled as close to lession prompt 
    #tried to limit complexity 

TAX = .06
B_COST = .99
F_COST = .79
S_COST = 1.09

def main():
#    yesList
#    noList
#getYesOrNo() that correcet input .lower or .uppper and return either true or false not a string
    endProgram =  "no"
    endOrder = "no"
    welcome()

    while endProgram == "no":
        totalBurger = 0
        totalFry = 0
        totalSoda = 0
        total = 0
        subtotal = 0
        
        while endOrder == "no":
#          reset = "no"
#        while reset == "no":
            numberOfOrder = getOrder()#lowercase
#            if numberOfOrder not in range(1,4):
#                print('Errrrreroreo erororer')
#                break
                
            if numberOfOrder == 1:
                totalBurger = getBurger(totalBurger)
                
            elif numberOfOrder == 2:
                totalFry = getFry(totalFry)
                
            elif numberOfOrder == 3:
                totalSoda = getSoda(totalSoda)
#        if reset == "yes":
#            endOrder = "yes"
 #           if reset != "no":
 #           print('An error has occured, order is restarting')
 #               endProgram = restart(endProgram)
            endOrder = str(input('Do you want to end your order (yes/no)'))

        subtotal = calcSubTotal(totalBurger, totalFry, totalSoda)
        if subtotal == -1:
            endOrder = "no"
            continue
        total = calcTotal(subtotal)
        formatedSubTotal = "{:,.2f}".format(subtotal)
        formatedTotal = "{:,.2f}".format(total)
        
        printTotal(totalBurger, totalFry, totalSoda, formatedSubTotal, formatedTotal)
        endProgram = str(input('Do you want to exit the program? (yes/no)'))
#def reset():
#    print('Invailed opiton, please try again.')
#    endOrder = "yes"
#    return endOrder
#def restart():
#    print('restarting...')
#    endProgram = "yes" 
#    return (endProgram)
def welcome():
    burger = "1 - Yum Yum Burger: $.99"
    fry = "2 - Yum Grease Fries: $.79"
    soda = "3 - Soda Yum: $1.09"
    time.sleep(1)
    print('Welcome to Yum Yum Burger')
    time.sleep(1)
    print('Home of the Yum Yum Burger')
    time.sleep(1)
    print('Voted #1 dumb yum burger for 4 years runnin!')
    time.sleep(2)
    print(f'Menu: {burger}') 
    time.sleep(2)
    print(f'      {fry}')
    time.sleep(2)
    print(f'      {soda}')

def getOrder():
    numberOfOrder = int(input('Enter your order number')) 

    while numberOfOrder < 1 or numberOfOrder > 3:
        numberOfOrder = int(input('Please enter a valid menu number (1-3)'))
    
    return numberOfOrder



def getBurger(totalBurger):
    burgerCount = int(input('Enter the number of burgers you want'))
 #   totalBurger += burgerCount 
 #   for burgerCount in range [0-99]:
    totalBurger += burgerCount
    return totalBurger

def getFry(totalFry):
    fryCount = int(input('Enter the number of fries'))
    totalFry += fryCount
    return totalFry

def getSoda(totalSoda):
    sodaCount = int(input('Enter the number of sodas'))
    totalSoda += sodaCount
    return totalSoda
    
def calcSubTotal(totalBurger, totalFry, totalSoda):
    print(f'You ordered: {totalBurger} burger(s), {totalFry} fries, and {totalSoda} soda(s)')
    check = str(input('is this correct? (y/n)'))
    if check == "y":
        subTotal = (totalBurger*B_COST) + (totalFry*F_COST) + (totalSoda*S_COST)
#        total = (subTotal * TAX) + subTotal
        return subTotal
    elif check == "n":
        print("Sorry for the inconvience, resetting order.")
        return -1

def calcTotal(subTotal):
    total = (subTotal * TAX) + subTotal
    return total
        

def printTotal(totalBurger, totalFry, totalSoda, formatedSubTotal, formatedTotal):
    if totalBurger >= 1:
        time.sleep(1)
        print(f'{totalBurger} burger(s) @ {B_COST} = {(totalBurger * B_COST)}')
    if totalFry >= 1:
        time.sleep(1)
        print(f'{totalFry} fries @ {F_COST} = {(totalFry * F_COST)}')
    if totalSoda >= 1:
        time.sleep(1)
        print(f'{totalSoda} soda(s) @ {S_COST} = {(totalSoda * S_COST)}')
    
    time.sleep(1)
    print(f'Your subtotal is {formatedSubTotal} @ {TAX}')
    time.sleep(1)
    print('Your total is $', formatedTotal)


main()