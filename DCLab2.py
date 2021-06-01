# Donovan Carr
name = input("What is your name Mr. Farmer: ")
print("Hello Farmer", name)
print("Nice to meet you")
# Remember to do Algorithm Workbench Ch.2
# Questions 1, 3, 5, 6 and 11
# Progrmaing Exercise 13, planting Grapevines.
# V = (R - 2E)/S

 Length = float(input("How many feet in length?: "))
 AreaSpace = float(input("How many feet of space for the end-post?: "))
 SpaceBetweenVines = float(input("How many space between the vines?: "))

 NumOfVines = Length - 2*AreaSpace / SpaceBetweenVines

 print(format("So you will be planting "NumOfVines,'.0f'))
# I told it to round the decimal place