# Donovan Carr
# Programming Exercise 12, Software Sales.
# Do Ch.3 Algorithm WorkBench questions
# 1, 3, 5, 6 and 7. Also
# Don't forget Ch.3 quize under unit 4
Again = 'y'
while Again == 'y':
    CustomerOrder = float(input("How many packages would you like to order?: "))
    OrderPrice = CustomerOrder*99
    if CustomerOrder >= 10 and CustomerOrder <= 19:
        print("You got the 10% discount")
        Ten_Percent_Discount = OrderPrice*.10
        TotalPrice = OrderPrice - Ten_Percent_Discount
        print("Your total is ", TotalPrice)
    else:
        if CustomerOrder >= 1 and CustomerOrder <= 9:
            print("You did not get the discount")
            print("Your total is ", CustomerOrder)
    
    if CustomerOrder >= 20 and CustomerOrder <= 49:
        print("You got the 20% discount")
        Twenty_Percent_Discount = OrderPrice*.20
        TotalPrice = OrderPrice - Twenty_Percent_Discount
        print("Your total is ", TotalPrice)
# Make it a loop and format it
    if CustomerOrder >= 50 and CustomerOrder <= 99:
        print("You got the 30% discount")
        Thirty_Percent_Discount = OrderPrice*.30
        TotalPrice = OrderPrice - Thirty_Percent_Discount
        print("Your total is $", TotalPrice)

    if CustomerOrder >= 100:
        print("You got the 40% discount")
        Thirty_Percent_Discount = OrderPrice*.40
        TotalPrice = OrderPrice - Thirty_Percent_Discount
        print("Your total is $", TotalPrice)
        
    Again = input("Would you like to try again(y for yes or any key to end)")
    
# Figure out how to make error check