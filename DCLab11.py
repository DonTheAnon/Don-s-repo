# Donovan Carr
# Due November 24
# Programming Exercise 1, Employee and ProductionWorker Classes
# Algorithm Workbench Ch. 11 questions 1, 2 and 3.
# Write an Employee class that keeps data attributes for the Employee's name and number
# Next write a class named ProductionWorker that is a subclass of the Employee class.
# its data attributes is shift number as integers and hourly pay rate.
# Day shift is shift 1, night shift is shift 2.
# Write a program that has you enter in data for the ProductionWorker

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
    def set_name(self, name):
        self.__name = name
        
    def set_number(self, number):
        self.__number = number
        
    def get_name(self):
        return self.__name
    
    def get_number(self):
        return self.__number
    
class ProductionWorker(Employee): # I almost forgot to add the first class into the sub
    def __init__(self, name, number, shift, wage):
        Employee.__init__(self, name, number)
        self.__shift = shift
        self.__wage = wage
        
    def set_shift(self, shift):
        self.__shift = shift
        
    def set_wage(self, wage):
        self.__wage = wage
        
    def get_shift(self):
        return self.__shift
    
    def get_wage(self):
        return self.__wage
        
def main():
    EmpName = input('Enter your name: ')
    EmpIDNum = int(input('Enter your ID number: '))
    EmpShift = int(input('Enter your shift number(1 for Day or 2 for Night): '))
    while EmpShift < 1 or EmpShift > 2: # I learned that it lets you try once for integer input first and will
        try:                            # raise a ValueError if you put in some thing alse that is not an int first
            EmpShift = int(input('Enter your shift number(1 for Day or 2 for Night): '))
        except ValueError:
            print('that is not an option')
    if EmpShift == 1:
        EmpShift = 'Day'
            
    elif EmpShift == 2:
        EmpShift = 'Night'
        
    else:
        print('That is not an option!')
        EmpShift = int(input('Please type whats on the menu: '))
        
# I tried puting EmpShift into its own function
# I did not try to figure out why it broke my code
# I need to figure out how to prevent the from entering a
# String for Shift and hourly pay.
    
#    while True: # this only lets you make an error once
#        try:
#            EmpShift = int(input('Enter your shift number(1 for Day or 2 for Night): '))
#            break
#        except ValueError:
#            EmpShift = int(input('Please type whats on the menu: '))
#            continue
#        else:
#            break
   
# try isalpha()            
            
    HourlyPay = float(input('Enter your hourly wage: '))
    
    EmployeeInfo = ProductionWorker(EmpName, EmpIDNum, EmpShift, HourlyPay)
    
    print('Name: ', EmployeeInfo.get_name())
    print('Number: ', EmployeeInfo.get_number())
    print('Shift:', EmployeeInfo.get_shift())
    print('Hourly Payment: $', format(EmployeeInfo.get_wage(),',.2f')) # format the hourly pay to $0.00
    
main()