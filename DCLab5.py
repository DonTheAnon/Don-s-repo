# Donovan Carr
# Programming Exercise 13, Falling Distance
# Don't forget Ch.5 Algorithm Workbench
# questions 3, 5, 6, 8 and 9.
# Due September 29th, 2020

# Write a function named falling distance in
# have the program in a loop that passes the values
# 1 thourgh 10 as the argument for time and
# Displays the return value for each loop
# d = 1/2gt^2 the formula for distance

def falling_distance(): # Went with the for loop
    seconds = 1         # I bet there is another way to do it
    loop = 11           # but this felt easier
    gravity = 9.8
    for seconds in range(seconds, loop):   # I'am not sure if the target variable seconds changes 
        distance = 1/2*gravity*seconds**2  # when I pass it as one of the values in range or not
        print('###############')           # but it works
        print("Seconds:",seconds)
        print("Distance:", format(distance, '.1f'))
        print('###############')
                                               
                                               
                                               
def main():                                    
    print("We are going to show you")          
    print("how the falling_distance function") 
    print("works!")                            
    print('###############')                   
    falling_distance()
    print('###############')
    print("Yahooooooo, it works!")
    
main()