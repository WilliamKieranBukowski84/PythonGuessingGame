#william K. Bukowski - Guessing game | 2022

import random

#on/off variable
flicker = True

#main logic block
while flicker:

    # user prompt
    print("Hello, welcome to Guessing Game")
    print("")
    print("Please input a number and the machine will tell")
    print("you if you were correct. Range is 0-10: ")

    inputVar = int(input())
    print("input is:")
    print(inputVar)

    #random number generator
    randomNum = (round(10*random.random()))
    print("machine number is:")
    print(randomNum)

    #if/else print if game is won or lost
    if randomNum == inputVar:
        print("you win")
    else:
        print("you lose")

        ###########################################
        print("Would you like to play again? Y/N:")

        # gets user decision to continue game or not
        onOff = input()

        # if/else turn loop on/off
        if onOff == "y":
            flicker = True
            print("Play again it is!")
        elif onOff == "n":
            flicker = False
            print("Goodbye!")
        else:
            flicker = True
            print("I suppose you want to play again?")


