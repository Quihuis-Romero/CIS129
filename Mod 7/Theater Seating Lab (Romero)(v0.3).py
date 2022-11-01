#Cesar D. Quihuis-Romero
#Theater Seating Lab
#v.03
    #cleaned up getYesOrNo(), did not need the extra variable 
#v.02
    #getYesOrNo() functional
    

#Globals
A_SEATS = 20
B_SEATS = 15
C_SEATS = 10
TAX = 0 #added for later expansion if sales tax is needed to be calculated as well


#section A is <= 300
#section B <=500
#section C <=200

def main():
    aSeats = 0
    bSeats = 0
    cSeats = 0
    endProgram = False

    while endProgram == False:
        aSeats = getSectionA()
        bSeats = getSectionB()
        cSeats = getSectionC()

        subTotal = calcSubTotal(aSeats, bSeats, cSeats)
    #   total = calcTotal(subTotal)
    #   formattedTotal = "${:,.2f}".format(total)
        formattedSubTotal = "${:,.2f}".format(subTotal)
        printTotal(formattedSubTotal)

        endProgram = getYesOrNo('Do you want to exit the program? (y/n)')

def getSectionA():
    aSeats = int(input('Please enter the number of tickets sold in section A (max: 300) '))
    
    while aSeats < 0 or aSeats > 300:
        aSeats = int(input('Please enter the number of seats sold in section A (max 300) '))
    
    return aSeats

def getSectionB():
    bSeats = int(input('Please enter the number of tickets sold in section B (max: 500) '))

    while bSeats < 0 or bSeats > 500:
        bSeats = int(input('Please enter the number of tickets sold in section B (max: 500) '))

    return bSeats

def getSectionC():
    cSeats = int(input('Please enter the number of tickets sold in section C (Max: 200) '))

    while cSeats < 0 or cSeats > 200: 
        cSeats = int(input('Please enter the number of tickets sold in section C (Max: 200)'))

    return cSeats

def calcSubTotal(aSeats, bSeats, cSeats):
    aRev = aSeats * A_SEATS
    bRev = bSeats * B_SEATS
    cRev = cSeats * C_SEATS
    fA_Rev = "${:,.2f}".format(aRev)
    fB_Rev = "${:,.2f}".format(bRev)
    fC_Rev = "${:,.2f}".format(cRev)
    print(f'Section A totals {fA_Rev} with {aSeats} seat(s) sold')
    print(f'Section B totals {fB_Rev} with {bSeats} seat(s) sold')
    print(f'Section C totals {fC_Rev} with {cSeats} seat(s) sold')
    subTotal = aRev + bRev + cRev

    return subTotal
#Added for later expansion if Sales tax is required as well
#def calcTotal(subTotal):
#    total = subTotal * TAX 
def printTotal(formattedSubTotal):
    print(f'Total revenue from tickets sales was {formattedSubTotal} ')

def getYesOrNo(prompt):
    yesNo = str(input(prompt)).lower()
    while yesNo != "y" and yesNo != "n" and yesNo != "yes" and yesNo != "no":
        yesNo = str(input(prompt)).lower()
    if yesNo == "y" or yesNo == "yes":
        return True
    elif yesNo == "n" or yesNo == "no":
        return False

main()
