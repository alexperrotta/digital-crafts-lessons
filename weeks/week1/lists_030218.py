# Python Exercises: Lists

Sum the Numbers
Given a list of numbers, print their sum. When I say given something, just make something up and store it in a variable.

numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

total = 0  # set a container variable to store the total in
for number in numbers:  # for each number in the numbers list
    total += number  # add the current number to the existing total
    # note here the use of the '+=' as a method of adding the RHS to the LHS

print total  # print the total number



Largest Number
Given a list of numbers, print the largest of the numbers.

numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

largest = max(numbers)

print largest


Smallest Number
Given a list of numbers, print the smallest of the numbers.

numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

smallest = min(numbers)

print smallest



Even Numbers
Given a list of numbers, print each number in the list that is even.

numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

for number in numbers:  # for each number the numbers list
    if number % 2 == 0:  # if there is no remainder after dividing by 2
        print number  # print the current number




Positive Numbers
Given a list of numbers, print each number in the list that is greater than zero.

numbers = [2, 3, 6, -10, -4, 0, 9, 32, 5]

numbers2 = [x for x in numbers if x >= 0]

print numbers2






Positive Numbers II
Given a list of numbers, create a new list which contains every number in the given list which is positive.

newlist = 0
for number in numbers:
    if number > 0:
        newlist += 1
    print newlist 




Multiply a list
Given a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. And print this list.






Multiply Vectors
Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

[2, 4, 5] x [2, 3, 6] = [4, 12, 30]



Matrix Addition
Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as a list of lists:

[ [2, -2],
[5, 3] ]


Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.

Example: to add

1 3
2 4
and

5 2
1 0
results in

6 5
3 4


Matrix Addition II
Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.



De-dup
Given an list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.





Bonus: Matrix Multiplication
Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix. How do you multiple two matricies?

https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplyingmatrices-by-matrices/v/matrix-multiplication-intro