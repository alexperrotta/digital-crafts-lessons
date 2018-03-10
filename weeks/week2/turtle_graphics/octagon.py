import turtle 

octagon = turtle.Turtle()

num_sides = 8
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    octagon.forward(side_length)
    octagon.right(angle)
    
turtle.done()