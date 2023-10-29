#Write an introductory message
print("Welcome to the tip calculator.")
#Input the bill
bill =  input("What was the total bill? ")
#Choose the percentage of tip you want to give
tip = input("What percentage tip will you like to give? ")
#Input the number of people to share the bill
people = input("How many people to split the bill? ")
#The number of people is given initially as a string. It needs to be converted to an integer. 
people_as_integer = int(people)
#The bill is given as a string. It should be converted to a float
bill_as_float = float(bill)
#The tip is given as a string and should be converted to an integer.
tip_as_integer = int(tip)
#Find the percentage of the tip to the bill
percent_of_tip = tip_as_integer / 100
tip_on_bill = bill_as_float * percent_of_tip
#Add the tip amount to the initial bill to give the total bill
bill_plus_tip = bill_as_float + tip_on_bill
#Split the bill among the friends
individual_bill = bill_plus_tip / people_as_integer
#Provide the final answer to the accuracy of two decimal point.
#This line of code will not work because the answer was not given in multiple decimal spaces. 
#Hence the need to format it with the code used.
#individual_bill_round = round(individual_bill, 2)
individual_bill_round ="{:.2f}".format(individual_bill)
#We add the print function to output the results. In addition we output the results with a sentence. 
print(f"Each person should pay ${individual_bill_round}")
