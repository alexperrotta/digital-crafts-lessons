# from turtle import *

# coord_list = [(100, -100, 100)]

# for coord in coord_list:
#     # up()
#     home()
#     x, y, size = coord
#     setheading(270)
#     forward(x)
#     setheading(0)
#     forward(y)
#     setheading(45)
#     forward(size)



# mainloop()

import turtle 

triangle = turtle.Turtle()

num_sides = 3
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    triangle.forward(side_length)
    triangle.right(angle)
    
turtle.done()