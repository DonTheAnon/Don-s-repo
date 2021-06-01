# Donovan Carr
# Ch.8 Programming Exercise 6, Average Number of Words
# Algorithm Workbench questions 2, 3, 5, 8 and 9
# Quiz due Oct. 21, 2020

# text.txt has one sentence per line. Write a program that reads the file's contents
# and calculates the average number of words per sentence.

# Try String slicing # turns out I did not need String slicing

def Text_File_Open(): # the len() function is extremly helpful, split() is too
    read_text = open('text.txt', 'r')
    
    lines = read_text.read()
    
    read_text.close()
    
    count = 0
    
    Sentence = lines.split("\n") # it splits at every new line, I looked at the file and counted it
                                 # to see if the result was true, new line began after every period.
#    read_text.close()
    
    for ch in Sentence: # this part was demonstrated in the begining of the chapter
        if ch:          # but I did not know how to implament it until
            count += 1  # I looked it up on the web at geeksforgeeks.org
    
    print(lines) # prints whats in the text file
    
    print('There are', count, 'sentences in the file.') # this prints how many sentances
#    print('there are', len(lines), 'string characters in the file.')
    
#    for sentence in read_text:
#        print(len(sentence))
    
    words_in_lines = lines.split()
    
    Words = len(words_in_lines) # Helps get the number of words through len() function
    
    print('there are', Words, 'words in the file.')
    
    AvgWord = Words / count
    
    print('There is on average',format(AvgWord, '.0f'), 'words per sentence.')
    
#    read_text.close()

Text_File_Open()