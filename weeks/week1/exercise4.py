totalAmount = int(raw_input("Enter the total amount."))
quality = raw_input("How is the quality of service?")
if quality == "good":
    tipPercentage = totalAmount * .2
if quality == "fair":
    tipPercentage = totalAmount * .15
elif quality == "bad":
    tipPercentage = totalAmount * .10
else:
    print "That's not a valid response."
print tipPercentage

party = int(raw_input("How many in your party?"))
split = (totalAmount + tipPercentage) / party
print split