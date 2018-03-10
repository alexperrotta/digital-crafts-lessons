import turtle 

square = turtle.Turtle()

# Loop 4 times. Everything I want to repeat is 
# *indented* by four spaces.
for i in range(4):
    square.forward(50)
    square.right(90)
    
# This isn't indented, so we aren't repeating it.
turtle.done()