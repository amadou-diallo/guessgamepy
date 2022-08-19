#!/ysr/bin/env python3

import random

prevcat = 0
prevdiff = 0
 

def getGuess():
    #final version: must validate as 0-100, and not crash on illegal input
    g = -1
    while g < 0 or g > 100:
        try:
            g = int(input("Your Guess? 0-100 Only. 0 = quit): "))
            if g < 0 or g > 100:
                print("Guess must be from 1 to 100 please.")
        except ValueError:
            print(" Illegal input: 0-100 only. ")
    return g
     
    
        
    



def playHighLow(rn):
    print("I am thinking of a number from 1 to 100..." + str(rn))
    gnum = 0;
    playing = True
    while playing:
        guess = getGuess()
        gnum += 1
        if guess == 0:
            print("Sorry, you did not guess my number: "
                  + str(rn) + " in " + str(gnum - 1) + " tries.")
            playing = False
        elif guess == rn:
            print ("You guess it! It took " + str(gnum) + " tries.")
            playing = False
        else:
            showHighLow(rn,guess)
            playing = True
            #End of playHighLow

def playHotCold(rn):
    print("I am thinking of a number from 1 to 100..." + str(rn))
    gcount = 0;
    playing = True #boolean
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry, you did not guess my number: "
                  + str(rn) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rn:
            print("You guess it! It took " + str(gcount) + " tries.")
            playing = False
        else:
            showHotCold(rn,guess)
            playing = True
        #End of playHotCold

def showHotCold(rn, guess):
    global prevcat, prevdiff
    diff = abs(rn - guess) #absolute value of difference
    category = 0
    msg = ""
    if diff >= 60:
        category = 1
        msg = "Cold"
    elif diff >= 30:
        category = 2
        msg = "Warm"
    elif diff >= 16:
        category = 3
        msg = "Very warm"
    else:
        category = 4
        msg = "HOT"

    if category  == prevcat:
        #add modifier
        if diff == prevdiff:
            msg += " (same degree) "
        elif diff > prevdiff:
            msg += " (getting colder) "
        else:
            if category == 4:
                msg += " (getting HOTTER) "
            else:
                msg += " (getting warmer) "

    print("Your guess is: " + msg)
    prevcat = category
    prevdiff = diff

def showHighLow(rnum, guess):
    gcount = 0
    playing = True
    while playing:
        guess = getGuess()
        gcount += 1
        if guess == 0:
            print("Sorry, you did not guess my number: "
                  + str(rnum) + " in " + str(gcount-1) + " tries.")
            playing = False
        elif guess == rnum:
            print("You guessed my number in" + str(gcount) + " tries!")
            playing = False
        else:
            if guess < rnum:
                print("Sorry, your guess is too low")
            else:
                print("Sorry, your guess is too high")
            playing = True
   

def main():
    print("Welcome to the Guessing Game")

    gametype = getChoice()
    while gametype != 0:
        rnum = random.randint(1,100)
        if gametype == 1:
            playHotCold(rnum)
        elif gametype == 2:
            playHighLow(rnum)
        else:
            print("I do not know that game!")
        print()
        gametype = getChoice()
    print("Thanks for playing!")

def getChoice():
    c = -1
    while c < 0 or c > 2:
        try:
            c = int(input("Game type: 1=Hot/Cold, 2= High/Low, 0=Quit): "))
            if c < 0 or c > 2:
                print("Unknown game type: 0, 1 or 2 only.")
        except ValueError:
            print("Illegal input: integers from 0 to 2 only")
            c = -1
    return c
            
        


if __name__ == "__main__":
    main()
