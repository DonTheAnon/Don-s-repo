# Donovan Carr
# October 23rd, 2020
# Creat a program that searches the text file for the names of foot ball teams
# and shows how many times they won; along with the year
# date years from lines in the text file from 1967 to 2020
# Due October 25th

def Open_Teams_File():
    Search_Teams = open('SuperBowlWinners.txt', 'r')

    Teams = Search_Teams.readlines()
#    Teams = Search_Teams.read()
    
    Search_Teams.close()
# I though the data in the file will be easier to handle in a list    
    index = 0
    while index < len(Teams):
        Teams[index] = Teams[index].rstrip('\n')
        index += 1       
        
    years = ['1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
             '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988',
             '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999',
             '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010',
             '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
# This is the list of dates to pull for each team
    print(Teams)
# Use dictionary to give dates to every win
# Create loop
    again = 'y'
    while again == 'y' or again == 'Y':
        
        LookForTeam = (input('Search for a Football Team:'))
        if LookForTeam == 'n' or LookForTeam == 'N':
            exit()
# I could not solve to stop a exception error for winyear if the search is not in list
        winyear = Teams.index(LookForTeam)  # I used index, even though it only gives the first occurance
        WinCount = Teams.count(LookForTeam) # it took me forever to realise I could just do this
        if LookForTeam not in Teams:        # count() method, instead of a for loop then if statement
            print('We do not have data on that team')
            print('or you misspelled it?')
        else:
            print(LookForTeam,'won the Superbowl', WinCount, 'times.')
            print('They won their first game in', years[winyear])
            
        DoAgain = input('Would you like to search again?(Yes(y) or No(n)):')
        if DoAgain == 'n' or DoAgain =='N': # I should have figured out that if I gave the loop
            exit()                          # input a differnt variable name it will create an infinate
                                            # loop unless i create an exit input
        
Open_Teams_File()