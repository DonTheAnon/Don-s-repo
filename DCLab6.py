# Donovan Carr
# Programming Exercise 6, Average of Numbers
# Algorithm Workbench Ch.6, questions 1, 2, 3, 4, 5

# Assume a file containing a series of integers is named numbers.txt
# and exists on the computer's disk. Write a program that calculates the
# average of all the numbers stored in the file.

# idea of program: make it so you can either enter numbers to the file
# or it automaticly creates numbers for the file if there is nothing there
# when the file is opened or created. Also make a variable of how many numbers
# to average in the program

#import random

def NumAverage(): # I needed to write this function to figure out what Im doing.
    # will either open or create numbers.txt
    numbers_file = open('numbers.txt', 'a')
    # I append the file because it said to assume the file exist
    # which it does not on my computer originaly, but likely exist
    # on the professor's computer. So I need to create it if its not
    # present on mine and just read it because it is present on the professor's
    
#    for randnum in range(3):            # might comeback to this idea later
#        randnum = random.randint(1,100) # I'm going to try entering in the numbers instead
#    userInput = input('Would you like to added numbers?')
#    while userInput == 'n' or user == 'y':
    while True:
        userInput = input('Would you like to added numbers?\n (y for Yes and n for No): ')
        if userInput == '' or not userInput[0].lower() in ['y','n']: # .lower() turns capital
            print('Please answer yes or no')                         # letters into lowercase
#        else:                                                       # I got it from a forum
#            break
        if userInput[0].lower() == 'y':
            num1 = int(input('Enter a number: '))
            num2 = int(input('Enter another number: '))
            num3 = int(input('Enter another number: '))
    
#    num1 = numbers_file.readline()
#    num2 = numbers_file.readline()
#    num3 = numbers_file.readline()
            numbers_file.write(str(num1) + '\n')
            numbers_file.write(str(num2) + '\n')
            numbers_file.write(str(num3) + '\n')
        else:
            break
        # all i needed to do was move the else break underneath the yes statement    
        if userInput[0].lower() == 'n': # no will print out all the numbers
            continue
    numbers_file.close()
    
    # Add a skip option if there are already numbers in the file
    
def read_Numbers():
    NumAverage() # this part of the program might get ignored if the first three lines already exist
                 # so I ended up writing aditional numbers that won't get calculacted.
    numbers_file = open('numbers.txt', 'r')
    
#    num1 = int(numbers_file.readline())
#    num2 = int(numbers_file.readline())
#    num3 = int(numbers_file.readline())
    
    line = numbers_file.readline() # lines 50 to 55 I got from the book
                                   # I still need to figure out how to get it
                                   # to calculate all the numbers
    SumNum = 0
    for line in numbers_file: # at first I used a while loop that was in the book
        numbers = int(line)
        print(numbers)
        SumNum += numbers
#        line = numbers_file.readline()
    
    numbers_file.close()
    # this closes the file
    
    # the Exercise asked to calculate all the numbers
    print('This is the sum of all numbers', SumNum)
    AveNum = SumNum / 3         # not just three
    print('This is the average of all numbers: ',AveNum)
# I was able to solve it    
read_Numbers()
    