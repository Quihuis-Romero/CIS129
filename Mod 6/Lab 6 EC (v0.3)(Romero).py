#global


TAX = .06
B_COST = .99
F_COST = .79
S_COST = 1.09

def main():
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
#            reset = "no"
#            while reset == "no":
            numberOfOrder = int(input('Enter your order number'))
            if numberOfOrder == 1:
                totalBurger = getBurger(totalBurger)
            elif numberOfOrder == 2:
                totalFry = getFry(totalFry)
            elif numberOfOrder == 3:
                totalSoda = getSoda(totalSoda)
 #           if reset != "no":
 #           print('An error has occured, order is restarting')
 #               endProgram = restart(endProgram)


            endOrder = str(input('Do you want to end your order (yes/no)'))

        subtotal = calcSubTotal(totalBurger, totalFry, totalSoda)
        total = calcTotal(subtotal)
        formatedTotal = "{:,.2f}".format(total)
        printTotal(totalBurger, totalFry, totalSoda, subtotal, formatedTotal)
        endProgram = str(input('Do you want to exit the program? (yes/no)'))

#def restart():
#    print('restarting...')
#    endProgram = "yes"
#    return (endProgram)
def welcome():
#    burger = "1 - Yum Yum Burger: $.99"
#    fry = "2 - Yum Grease Fries: $.79"
#    soda = "3 - Soda Yum: $1.09"

#    print('Welcome to Yum Yum Burger')

#    print('Home of the Yum Yum Burger')

#    print('Voted #1 dumb yum burger for 4 years runnin!')

#    print(f'Menu: {burger}') 
   
#    print(f'      {fry}')

#    print(f'      {soda}')

    print('Enter 1 for Yum Yum  Burger')
    print('Enter 2 for Grease Yum Fries')
    print('Enter 3 for Soda Yum')
    


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
#    elif check == "n":
        reset = str(input('would you like to restart your order? (y/n)'))
        return reset
def calcTotal(subTotal):
    total = (subTotal * TAX) + subTotal
    return total
        

def printTotal(totalBurger, totalFry, totalSoda, subtotal, formatedTotal):
#    if totalBurger >= 1:
       
#        print(f'{totalBurger} burger(s) @ {B_COST} = {(totalBurger * B_COST)}')
#    if totalFry >= 1:
        
#        print(f'{totalFry} fries @ {F_COST} = {(totalFry * F_COST)}')
#    if totalSoda >= 1:
       
#        print(f'{totalSoda} soda(s) @ {S_COST} = {(totalSoda * S_COST)}')
    
 
#    print(f'Your subtotal is {subtotal} @ {TAX}')
 
    print('Your total is $', formatedTotal)


main()