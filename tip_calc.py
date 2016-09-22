bill = float(raw_input("How much was the bill? "))
service = str.upper(raw_input("How was the service (Good, Bad, OK)? "))

if service == "GOOD":
    print "Tip amount is $%.2f." % ((bill * .20))
    print "Total is $%.2f." % ((bill + (bill * .20)))

elif service == "BAD":
    print "Tip amount is $%.2f." % ((bill * .10))
    print "Total is $%.2f." % ((bill + (bill * .10)))

else:
    print "Tip amount is $%.2f." % ((bill * .15))
    print "Total is $%.2f." % ((bill + (bill * .15)))
