bill = float(raw_input("How much was the bill? "))
service = str.upper(raw_input("How was the service (Good, Bad, OK)? "))
customer = float(raw_input("Split how many ways? "))

if service == "GOOD":
    print "Tip amount is $%.2f." % ((bill * .20))
    print "Total is $%.2f." % ((bill + (bill * .20)))
    print "Amount per person: $%.2f." % ((((bill + (bill * .20))) / customer))

elif service == "BAD":
    print "Tip amount is $%.2f." % ((bill * .10))
    print "Total is $%.2f." % ((bill + (bill * .10)))
    print "Amount per person: $%.2f." % ((((bill + (bill * .20))) / customer))

else:
    print "Tip amount is $%.2f." % ((bill * .15))
    print "Total is $%.2f." % ((bill + (bill * .15)))
    print "Amount per person: $%.2f." % ((((bill + (bill * .20))) / customer))
