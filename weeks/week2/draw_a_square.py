from turtle import *

def draw_square():
    for i in range(4):
        forward(100)
        left(90)



if __name__ == '__main__':  # run this file only if being run as the main program
    draw_square()

    up() # lifts up the pen so it doesn't draw a line
    forward(200)
    down() # puts the pen down

    draw_square()

    mainloop() # causes the program to hang
