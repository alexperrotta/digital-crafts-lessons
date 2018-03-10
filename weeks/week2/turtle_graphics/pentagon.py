import turtle 

pentagon = turtle.Turtle()

num_sides = 5
side_length = 70
angle = 360.0 / num_sides 

for i in range(num_sides):
    pentagon.forward(side_length)
    pentagon.right(angle)
    
turtle.done()