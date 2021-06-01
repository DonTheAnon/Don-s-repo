# Donovan Carr
# Ch.7 Programming Exercise 9, Population Data
# and Algorithm Workbench questions: 1, 2, 3, 5 and 6
# Ch.7 quiz due Oct. 14th

# Write a program that reads the file USPopulation.txt containts into a list.
# The program should display the following data:
# The average annual change in population during the time period.
# The year with the greatest increase in population during the time period.
# The year with the smallest increase in population during the time period.
# Years 1950 to 1990

def Pop_List_History():
    View_History = open('USPopulation.txt', 'r')
    
    Pop_List = View_History.readlines() # I learned the hard way that read() and readlines()
                                        # are two different things, read() will either print
    View_History.close()                # one item and/or assigns it as a string
    # convert numbers from text file to integers
    # inorder to do math with them and to display
    index = 0
    while index < len(Pop_List):               # I forgot that len() can give you the total
        Pop_List[index] = int(Pop_List[index]) # number of elements or items in a file
        index += 1                             # this while loop converts the list elements into integers
        
    print(Pop_List)
    PopSum = sum(Pop_List) # Im not sure if I skiped over the part of the book where it
                           # mentioned that sum() function will solve for sum, I found it online.
    print('This is the sum of all Population years:', format(PopSum, ',.0f'))
    print('This is the amount of numbers:',(len(Pop_List)))
    PopNums = len(Pop_List)
    AvgPop = PopSum / PopNums
    print('This is the average of the list:', format(AvgPop, ',.0f'))
#    print(index)
#   print(Pop_List[5]) # will give you number that is assigned 5 which is the sixth number in the list.       
#    print(Pop_List[0 : 5]) # start from 0 give five numbers: 0, 1, 2, 3, 4
    PopIncrease = Pop_List[40] - Pop_List[0]
    print('This is how much the population increase since 1950 to 1990:',format(PopIncrease, ',.0f'))
    PopIncresPerc = PopIncrease / Pop_List[0]
#    print(PopIncresPerc)
    PopIncresPercInt = PopIncresPerc * 100
    print('This is the percentage of population increase:', format(PopIncresPercInt,'.0f'),'%')
    
    
# Increase = latest Increase - Original Number, then take the increase answer
# divide it by the Original Number then Divide it by 100 to get the percentage
def main():
    Pop_List_History()
main()