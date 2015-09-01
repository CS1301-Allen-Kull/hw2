# Tristen Allen - Section A4
# tristen.allen@gatech.edu 903035156
# Adam Kull - Section A4
# akull3@gatech.edu 903135072
# We worked on the homework assignment alone, 
# using only this semester's course materials.

def square(base):
    result = base ** 2
    return result

def taylorSwift(numFans):
    time = numFans * 3
    mins = time % 60
    h = time // 60
    hrs = 9 + h
    if hrs > 12:
        hrs = hrs - 12
        print("Taylor Swift is done at " + str(hrs) + ":" + str(mins) + " AM.")
    elif hrs < 12:
        print("Taylor Swift is done at " + str(hrs) + ":" + str(mins) + " PM.")
    else:
        print("Taylor Swift is done at " + str(hrs) + ":" + str(mins) + " AM.")

def girlScoutCookies():
    b = int( input("How Many Boxes Do You Want?") )
    m = float( input("How Much Money Do You Have?") )
