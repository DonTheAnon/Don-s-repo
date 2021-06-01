# Donovan Carr
# Programming Exercise 10, Tuition Increase.
# Do Ch.4 Algorithm WorkBench questions
# 2, 3, 4, and 6.
# Due Sep 22 and Ch.4 quiz due Sep 23

Start_Year = 1
End_Year = 6
# I could probably use these to control which year starts with 8000
# the increase after
print('Year\tTuition')
print('---------------')
# maybe use a while loop to help start the year at 8000
for year in range(Start_Year, End_Year):
    # I would get confused and think if I add a third variable it would skip that year
    Tuition = 8000    
    increase = year*0.03
    Tuition_increase = increase * Tuition
    TuitionCost = Tuition_increase + Tuition
#    while year == 1:
#        TuitionCost = 8000
    # I solved the tuition increase but I don't know how
    # to get it to skip year 1 and add to the rest of the years
    print(year, '\t', TuitionCost)