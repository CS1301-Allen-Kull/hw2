# Tristen Allen - Section A4
# tristen.allen@gatech.edu 903035156
# Adam Kull - Section A4
# akull3@gatech.edu 903135072
# We worked on the homework assignment alone, 
# using only this semester's course materials.

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
        print("Taylor Swift is done at " + str(hourFinished) + ":" + str(mins) + " PM.")
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
