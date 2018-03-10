totalAmount = int(raw_input("Enter the total amount."))
tipPercentage = int(raw_input("Enter the tip percentage amount."))
tipAmount = (totalAmount * tipPercentage) / 100
print "The tip is %s" % tipAmount
