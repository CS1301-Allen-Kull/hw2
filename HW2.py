# Tristen Allen - Section A4
# tristen.allen@gatech.edu 903035156
# Adam Kull - Section A4
# akull3@gatech.edu 903135072
# We worked on the homework assignment alone, 
# using only this semester's course materials.

import math

def square(base):
    # calculate square of 'base' parameter
    result = base ** 2
    return result

def taylorSwift(numFans):
    #calculate minutes and hours spent signing swag
    time = numFans * 3
    mins = time % 60
    hours = time // 60
    
    #start time is 9:00 PM
    hourFinished = 9 + hours
    
    #swift must leave at 11:59 PM
    if hourFinished >= 12:
        print("Taylor Swift is done at 11:59 PM.")
        return
    else:
        print("Taylor Swift is done at {}:{:02d} PM.".format(hourFinished, mins))
        return

def girlScoutCookies():
    #get info from user on cookie boxes
    boxes = int(input("How many boxes do you want?"))
    moneyHave = float(input("How much money do you have?"))
    
    #calculate money needed
    costBoxes = boxes * 4
    moneyNeeded = costBoxes - moneyHave
    
    #print amount of money needed
    print("You still need ${:.2f} to buy those delicious cookies.".format(moneyNeeded))

def conversionTime(metersPerSecond):
    #calculate feet per second
    feetPerSecond = metersPerSecond * 3.28084

    #calculate kilometers per hour
    kilometersPerHour = (metersPerSecond / 1000) * 3600

    #calculate miles per hour
    milesPerHour = (feetPerSecond / 5280) * 3600

    #print results of calculation
    print("{:.2f} meters per second is equivalent to {:.2f} miles per hour, {:.2f} feet per second, and {:.2f} kilometers per hour.".format(float(metersPerSecond), float(milesPerHour), float(feetPerSecond), float(kilometersPerHour)))
    
def tipCalculator():
    #get all initial input from user
    billCost = float(input("How much was your bill before taxes and coupons?\nDo NOT enter a dollar sign"))
    tipPercent = float(input("What percentage tip would you like to leave?\nDo NOT enter a percentage sign")) / 100
    discount = float(input("How many dollars off is your coupon?\nDo NOT enter a dollar sign"))
    
    #perform complex calculations
    tip = math.ceil(billCost * tipPercent)
    discountCost = billCost - discount
    tax = discountCost * 0.08
    totalCost = discountCost + tip + tax
    
    #return total cost of meal as a string
    return "${:.2f}".format(totalCost)

def falafel(falafelBalls, hummus, pitaBread):
    #find out the number of sandwiches each ingredient can make
    falafelLimit = falafelBalls // 6
    hummusLimit = hummus // 2
    pitaLimit = pitaBread
    
    #find out which value is smallest
    if (falafelLimit <= hummusLimit and falafelLimit <= pitaLimit):
        numSandwiches = falafelLimit
    elif (hummusLimit < falafelLimit and hummusLimit <= pitaLimit):
        numSandwiches = hummusLimit
    else:
        numSandwiches = pitaLimit
    
    #print results of calculation
    print("With {} falafel balls, {} tablespoons of hummus, and {} pieces of pita bread, you can make a maximum of {} falafels.".format(falafelBalls, hummus, pitaBread, numSandwiches))
