#CIS-129 Cesar D. Quihuis-Romero 
#Module 6 Lab part 3 exersice 10/22/2022

#Program recieves the number of bottles returned over 7 days and calculates the total number of bottles collected and the total amount of money paid for the bottles in USD $

#def main
def main():
    endProgram = 'no'
    while endProgram == 'no':
        totalBottles = getBottles()
        totalPayout = calcPayout(totalBottles)
        printInfo(totalBottles, totalPayout)
        endProgram = input('Do you want to end the program? (Enter yes or no): ')

#def getbottles will return totalbottles retured over 7 days
def getBottles():
    totalBottles = 0
    todayBottles = 0
    counter = 1

    while counter <= 7:
        todayBottles = int(input('Enter number of bottles for today:'))
        totalBottles += todayBottles
        counter += 1
        
    return totalBottles

#def calpayout will calculate the payout
def calcPayout(totalBottles):
    totalPayout = 0
    totalPayout = totalBottles * .10
    return totalPayout

#def printinfo will display the information
def printInfo(totalBottles, totalPayout):
    print('The total number of bottles collected is', totalBottles)
    print('The total paid out is $', totalPayout)

#call to main
main()