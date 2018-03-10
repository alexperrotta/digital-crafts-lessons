from turtle import * 

# an equilateral triangle

def drawTriangle():
    triangle = turtle.Turtle()
    num_sides = 3
    side_length = 70
    angle = 360.0 / num_sides 
    for i in range(num_sides):
        triangle.forward(side_length)
        triangle.right(angle)

drawTriangle()


# a square

def drawSquare():
    square = turtle.Turtle()
    num_sides = 4
    side_length = 70
    angle = 360.0 / num_sides 
    for i in range(num_sides):
        square.forward(side_length)
        square.right(angle)

drawSquare()


# a pentagon

def drawPentagon():
    pentagon = turtle.Turtle()
    num_sides = 5
    side_length = 70
    angle = 360.0 / num_sides 
    for i in range(num_sides):
        pentagon.forward(side_length)
        pentagon.right(angle)

drawPentagon()


# a hexagon

def drawHexagon():
    hexagon = turtle.Turtle()
    num_sides = 6
    side_length = 70
    angle = 360.0 / num_sides 
    for i in range(num_sides):
        hexagon.forward(side_length)
        hexagon.right(angle)

drawHexagon()

# an octagon 

def drawOctagon():
    octagon = turtle.Turtle()
    num_sides = 8
    side_length = 70
    angle = 360.0 / num_sides 
    for i in range(num_sides):
        octagon.forward(side_length)
        octagon.right(angle)

drawOctagon()

# a star

def drawStar():
    star = turtle.Turtle()
    for i in range(50):
    star.forward(50)
    star.right(144)

drawStar()

# a circle

def drawCircle():
    width(10) 
    circle(180)

drawCircle()