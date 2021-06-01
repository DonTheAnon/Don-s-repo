# Donovan Carr
# Ch.10 Programming Exercise 2, Car Class.
# Algorithm Workbench question 2, Due November 10
# Quize due November 11th

# Create a car object that ask for year_model, make and speed
# then create methods for accelerate, brake and get_speed

class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
        
    def YearModel(self, year_model):
        self.__year_model = year_model
        
    def Make(self, make):
        self.__make = make
        
    def Speed(self, speed):
        self.__speed = int(speed)
        speed = 0
        
    def accelerate(self, speed):
        self.__speed = speed
        
    def brake(self, speed):
        self.__speed = speed
        
    def get_speed(self):
        return self.__speed
    
    def get_make(self):
        return self.__make
    
    def get_year_model(self):
        return self.__year_model
    
def main():
    year = (input('What year model is your car?: '))
    make = input('What make is your car?: ')
    speed = int(input('How fast were you going?: '))
    carinfo = Car(year, make, speed)
# it took me a while to learn that i need it to pass the values into carinfo and same with CarMovement
# add in input validation to keep the program from crashing    
    print('Here is the data you entered: ')
    print('Year Model:', carinfo.get_year_model())
    print('Make:', carinfo.get_make())
    print('Speed:', carinfo.get_speed())
# Figure out how to get it to constantly go down or up in speed
# You need the loop to iterate: which calls for a for loop to get the numbers to change
    Faster_Slower = 'a'
    CarMovement = Car(make, speed, Faster_Slower)
    while Faster_Slower == 'a' or Faster_Slower == 'b': # I tried to make it an option by pressing
        Faster_Slower = input('Go faster(a), go slower(b): ') # a or b for accelerate or brake
         
        if Faster_Slower == 'a':
            CarMovement.accelerate(speed + 5)
            print(CarMovement.get_speed())
            
        elif Faster_Slower == 'b':
            CarMovement.brake(speed - 5)
            print(CarMovement.get_speed())
        else:
            print(CarMovement.get_speed())
            exit()
    
main()
        
# it keeps adding and subtracting from the original value of speed instead of the new value
# after accelerating it or pressing brake.