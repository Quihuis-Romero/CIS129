#CIS-129 Cesar D. Quihuis-Romero (personal versions)
#Module 6 Lab part 3 exersice 10/22/2022

#Program recieves the number of bottles returned over 7 days and calculates the total number of bottles collected and the total amount of money paid for the bottles in USD $

#attempting to add a redirect for bad user inputs
#trying to figure out input sanitation options for this program
#globals

RETURN_RATE = .10 #allows for altering of .10 cent return if needed 

#def main
def main():
    endProgram = 'no'
    while endProgram == 'no':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        formatedBottles = "{:,.0f}".format(totalBottles)
        truncPayout = "{:,.2f}".format(totalPayout)
        printInfo(formatedBottles, truncPayout)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')
        

#def getbottles will return totalbottles retured over 7 days
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1
#    redirect = print('Please enter a valid number')

    #could prompt user to only put in whole number of bottles deposited, but would still need a redirect in case bad input is recieved
    while counter <= 7: #could make sure all values are input as integers and drop float, or even format todayBottles to ensure it will always be a integer
        todayBottles = float(input('Enter number of bottles for today:'))  #not really familiar how to translate float into int and ensure it will only calculate based on whole bottles
#if I could figure out how to translate a float into a int it would go here (i.e formatedTodayBottles = syntax for converting float into int)  (at least I think)      
        totalBottles += todayBottles
        counter += 1
#        if todayBottles != float():
#            print(redirect)
        
    return totalBottles

#def calcPayout will calculate the payout
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * RETURN_RATE
    return totalPayout

#def printinfo will display the information
def printInfo(formatedBottles, truncPayout):
    print('The total number of bottles collected is', formatedBottles) #not satisfied will print out it is rounding up and not truncating might need import math for math.trunc
    print('The total paid out is $', truncPayout) #formating is working here to display USD familiar display

#call to main
main()