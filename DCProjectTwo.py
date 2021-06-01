# Donovan Carr
# Project 2: Blood Alcohol Level
# math equation: B = -0.015 * t +(2.84*N/W * g)

def Gender_Function():
    gender = float(input("What gender are you(m for Male, f for female):"))
    if gender == 'm':     # I could not figure out how to get to where
        m = 0.68          # You can enter a letter and it takes it
        male = float(m)   # as a float, I could not convert it to a float
    if gender == 'f':
        f = 0.55
        female = float(f)
    else:
        print("Sorry we do not have any data on that gender")
        gender = float(input("What gender are you(m for Male, f for female):"))
    return gender
        
def BAC_Test():
#    Gender_Function()
    weight = float(input("How much do you weight in pounds?: "))
    NumOfDrinks = float(input("How many drinks have you had?: "))
    TimeOfDrinks = float(input("How long many hours since your first drink?: "))
    Gender_Function()
    # math equation: B = -0.015 * t +(2.84*N/W * g) | I place this here to remind my self of the equation
    BACLevel = -0.015 * TimeOfDrinks + 2.84 * NumOfDrinks / weight * gender
    print(BACLevel)
    
BAC_Test()