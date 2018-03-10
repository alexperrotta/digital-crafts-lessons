# phrase = "Welcome to Digital Crafts"
# width = len.phrase
# height = 3

# for row in range(height):
#     if row == 0 or row == 2:
#         print "*" * (len.width + 2)
#     else:
#         spaces = width + 2
#         print "*" + spaces + "*" 

secret_number = "5"
guessed = raw_input("Guess a number: "
answer = " "

for answer in guessed:
    if answer == 5:
        print "You win!"
    elif answer != 5:
        print "Guess again."
    else:
        print "You lose."
