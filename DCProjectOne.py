# Donovan Carr
#while True:
#    silver = float(input("How many silver tickets were sold: "))
#    try:
#        userNumber = int(silver)
#        print("Input is an integer number")
#        print("Input number is: ", userNumber)
#        break;
#    except ValueError:
#        try:
#            float(silver)
#            print("Input is an float number")
#            print("Input number is: ", userNumber)
#            break;
#        except ValueError:
#            if userNumber = str(silver)
#            print("This is not a number. Please enter a number")
#if silver.isnumber():
#    print(silver, 'contains only numbers')
#else:
#    print(silver, 'your input was not a number')

# I could not solve for the error check so I gave up
repeat = 'y'

while repeat == 'y':
    silver = float(input("How many silver tickets were sold: "))
    gold = float(input("How many gold tickets were sold: "))
    platinum = float(input("How many platinum tickets were sold: "))
    SilKets = silver*25
    GolKets = gold*45
    PlaKets = platinum*75
    TotalRevenue = SilKets + GolKets + PlaKets
    TicketTotal = silver+gold+platinum
    print("%-15s %-15s %s" %("Section", "Tickets", "Revenue"))
    print('---------------------------------------')
    print("%-15s %-15d $%d" %("Silver", silver, SilKets))
    print("%-15s %-15d $%d" %("Gold", gold, GolKets))
    print("%-15s %-15d $%d" %("Platinum", platinum, PlaKets))
    print('=======================================')
    print("%-15s %-15d $%d" %("Total", TicketTotal, TotalRevenue))
    repeat = input("Do you want to try again?(y for yes, any key to exit):")
# Make an error check to keep the program from crashing
# Add a loop to ask if the user would like to try again
#print("Sliver Tickets Total:", SilKets)
#print("Gold Tickets Total:", GolKets)
#print("Platinum Tickets Total:", PlaKets)
#print("The total revenue is:", TotalRevenue)
# add coloms and loops
# Position values in the coloms
