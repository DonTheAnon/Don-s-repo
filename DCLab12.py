# Donovan Carr
# Assignment 12
# Due December 1st 2020

import boto3
import credentials
import statistics

print('DEFINING S3 RESOURCE.')

s3 = boto3.client('s3',
    aws_access_key_id = credentials.AWS_ACCESS_KEY_ID,
    aws_secret_access_key = credentials.AWS_SECRET_ACCESS_KEY)

print('BEGINNING DOWNLOAD.')

s3.download_file('nlc-data-files', 'numbers.txt', 'C:/Data/numbers.txt')

print('FINISHED')

def main():
    numbers_file = open("C:/Data/numbers.txt", 'r')

    Population = numbers_file.readlines()
    
    numbers_file.close()
# I don't think i really needed to print the list but I got it    
    index = 0
    while index < len(Population):
        Population[index] = float(Population[index].rstrip('\n'))
        index += 1
        
    print(Population) # the list is too long to show whole thing in the shell
    
    totalNums = len(Population)
    print('The amount of numbers in the file is', totalNums)
    SumOfPop = sum(Population)
    print(format(SumOfPop, '.3f'),'is the sum of the Population.')
    PopAvg = SumOfPop / totalNums
    print('The average population is', format(PopAvg, '.3f'))
    popStdev = statistics.pstdev(Population)
    print('The standard deviation of the whole population is', format(popStdev, '.3f'),'\n')

# I gave the sum of the population and sample not the average, work on the average next
# use the number you got from len() to divid the real sum(all numbers added together in the list)

    print('Here is the sample list of every third number in the file:')
    sample = Population[::3]
    print(sample)
    totalSamp = len(sample)
    print('There are', totalSamp, 'numbers in the sample.')
    SumOfSamp = sum(sample)
    print(format(SumOfSamp, '.3f'), 'is the sum of the sample')
    SampAvg = SumOfSamp / totalSamp
    print('The average of the sample is',format(SampAvg, '.3f'))
    SampStdev = statistics.stdev(sample)
    print('The standard deviation of the sample is',format(SampStdev, '.3f'),'\n')
    
    # solve for the difference between the two standard deviations
    Difference = SampStdev - popStdev
    # I could have subtracted with the population first then the sample
    # and write additional code to turn the negative number to a positive
    print('This is the difference between the population and the sample:', format(Difference, '.3f'))
    # It took me a day to realise that that was all I had to do to solve for the difference
    
main()