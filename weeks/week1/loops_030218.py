1 to 10
Using a for loop and the range function, print out the numbers between 1 and 10 inclusive, one on a line. Example output:

for number in range(1, 11):    #from index 1 to index 10
    print number

$ python 1_to_10.py
123456789
10


n to m
Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:

start = int(raw_input("Start from: "))
end = int(raw_input("End on: "))

for number in range(start, end + 1):   # the + 1 will make it print the 8
    print number

$ python n_to_m.py
Start from: 2
End on: 8
2345678



Odd Numbers
Print each odd number between 1 and 10 inclusive. Example output:

$ python odd_numbers.py
13579
Hint: you will need to use the modulus operator % to determine whether a number is odd or even.


for number in range(1, 11, 2):  #we add the 2 to skip every other number 
    print number

or 


for number in range(1, 11): 
    if number % 2:  #if the number has a remainder after dividing by 2, print the number
    print number 



Print a Square
Print a 5x5 square of * characters. Example output:

$ python square.py
*****
*****
*****
*****
*****

n = 5

for number in range(n)
    print "*" * n





Print a Square II
Print a NxN square of * characters. Prompt the user for N. Example output:

$ python square2.py
How big is the square? 10
**********
**********
**********
**********
**********
**********
**********
**********
**********
**********

n = int(raw_input("How big is the square?"))

for number in range(n)
    print "*" * n




Print a Box
Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

$ python box.py
Width? 6
Height? 4
******
*    *
*    *
******

width = int(raw_input("Width?"))
height = int(raw_input("Height?"))

for row in range(height):
    if row == 0:
        print "*" * width  # this will print the top row of *, remember this is referring to the index
    elif row == height - 1:
        print "*" * width  # this will print the bottom row of *
    else:
        spaces = width - 2  # this will print the middle rows
        print "*" + (" " * spaces) + "*"  #it's going to multiple first and than add

or 

width = int(raw_input("Width?"))
height = int(raw_input("Height?"))

for row in range(height):
    if row == 0 or row == height - 1:
        print "*" * width
    else:
        spaces = width - 2  #this is 8 spaces
        print "*" + (" " * spaces) + "*"  #so it will print a * then 8 spaces and then another *




# Print a Triangle
# Print a triangle consisting of * characters like this:

   *
  ***
 *****
*******


height = 4
base = height * 2 - 1  # this defines the base of the triangle, which is 7 stars (4x2 = 8 (index), 8-1= 7, to get 7 stars )

for row in range(1, height + 1):  # this accounts for the index
    spaces = height - row  #using the row number to calculate how many spaces we need
    print " " * spaces + "*" * (row * 2 - 1)  #this 2nd half doubles the rows so you get the full triangle

    # note: " " * spaces handles the left side and row * 2 - 1) handles the right side






Print a Triangle II
Given a number as the height, print a triangle as in “Print a Triangle” but with the given height.

height = int(raw_input("How tall is the tree?"))
base = height * 2 - 1

for row in range(height + 1):
    spaces = height - row
    print " " * spaces + "*" * (row * 2 - 1)





Multiplication Table
Print the multiplication table for numbers from 1 up to 10. Example output:

$ python multiplication_table.py
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
...
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
...
10 X 8 = 80
10 X 9 = 90
10 X 10 = 100

n = 10

for number1 in range(1, n + 1):
    for number2 in range(1, n + 1):
        result = number1 + number2
        print "%d X %d = %d" % (number1, number2, result)




Bonus: Print a Banner
Given a string, input by the user, print that string with a box around it. The box should stretch to the length of the string. Example session:

$ python banner.py
Text? Welcome to DigitalCrafts
****************************
* Welcome to DigitalCrafts *
****************************

phrase = "Welcome to Digital Crafts"
width = len.phrase
height = 3

for row in range(height):
    if row == 0 or row == 2:
        print "*" * (len.width + 2)
    else:
        spaces = width + 2
        print "*" + spaces + "*"    








Bonus: Triangle Numbers
Print the first 100 triangle numbers. What is a triangle number? Read this:

https://www.mathsisfun.com/algebra/triangular-numbers.html.







Bonus: Factor a Number
Given a number, print its factors. What are factors?

https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-andfactors/v/finding-factors-of-a-number