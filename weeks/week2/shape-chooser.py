# function for drawing a triangle

def drawTriangle():
    height = int(raw_input("What's the height?"))
    base = height * 2 - 1
    for row in range(1, height + 1): 
        spaces = height - row  
        print " " * spaces + "*" * (row * 2 - 1)
    print "Here you go!"

# function for drawing a square

def drawSquare():
    width = int(raw_input("What's the length and width?"))
    for number in range(width):
        print "*" * width
    print "Here you go!"

# function for drawing a box

def drawBox():
    height = int(raw_input("What's the height?"))
    width = int(raw_input("What's the width?"))
    for row in range(height):
        if row == 0 or row == height - 1:
            print "*" * width
        else:
            spaces = width - 2  
            print "*" + (" " * spaces) + "*"
    print "Here you go!"

# function for random insults
import random
def randomInsults():
    insult = random.randint(1,5)
    if insult == 1:
        print("I am sick when I do look on thee")
    elif insult == 2:
        print("I scorn you, scurvy companion.")
    elif insult == 3:
        print("More of your conversation would infect my brain.")
    elif insult == 4:
        print("Poisonous bunch-backed toad!")
    elif insult == 5:
        print("Thou art a boil, a plague sore")
    else:
        print("Thou sodden-witted lord!")


# function to ask if the player wants to go again

def playAgain():
        again = raw_input("Would you like to play again? Y or N ")
        if again.upper() == 'Y':
            shapeChooser()
        elif again.upper() == 'N':
            print "Ok, Bye!"
            quit()
        else: 
            randomInsults()
            shapeChooser()


# function for choosing the shape

def shapeChooser():
    choice = raw_input(""" 
        What shape do you wish to print?: 
        1 Triangle 
        2 Square 
        3 Box
        """)
    if choice == "1":
        drawTriangle()
    elif choice == "2":
        drawSquare()
    elif choice == "3":
        drawBox()
    else:
        print "Invalid answer."
        shapeChooser()

shapeChooser()
playAgain()
