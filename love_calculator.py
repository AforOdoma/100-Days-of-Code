print("The Love Calculator is calculating your score...")
name1 = input(" What is your name?\n")
name2 = input("What is their name? \n")


both_names = name1 + name2
names_in_lowercase = both_names.lower()

t = names_in_lowercase.count("t")
r = names_in_lowercase.count("r")
u = names_in_lowercase.count("u")
e = names_in_lowercase.count("e")

first_num = t + r + u + e

l = names_in_lowercase.count("l")
o = names_in_lowercase.count("o")
v = names_in_lowercase.count("v")
e = names_in_lowercase.count("e")

second_num = l + o + v + e

love_score = str(first_num) + str(second_num)
int_lovescore = int(love_score) 

if int_lovescore < 10 or int_lovescore > 90:
    print(f"Your score is {int_lovescore}, you go together like coke and mentos.")
elif int_lovescore >= 40 and int_lovescore <= 50:
    print(f"Your score is {int_lovescore}, you are alright together.")
else: 
    print(f"Your score is {int_lovescore}.")