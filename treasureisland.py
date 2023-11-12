print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision1 = input("You're at a crossroad, where do you want to go? Type 'left' or 'right'. \n").lower()

if decision1 == "right":
    print("You fell into a hole. Game Over.")
elif decision1 == "left":
    decision2 = input("Will you swim or wait? Type 'swim' or 'wait'. \n").lower()

    if decision2 == "swim":
        print("You got attacked by trout. Game Over")
    elif decision2 == "wait":
        decision3 = input("You have three doors before you. Which of the door will you open? Type 'blue' or 'red' or'yellow' \n").lower()

        if decision3 == "red": 
            print("You entered a room filled with fire and you got burned by fire. Game Over")
        elif decision3 == "blue":
            print("You You entered a room filled with beasts and got eaten by beasts. Game Over")
        elif decision3 == "yellow":
            print("Congratulations !!! You found the treasure. You have won!!!")
        else: 
            print("The option you have choosen does not exist!!! Game over....")

    else:
        print("The option you have choosen does not exist!!! Game over!!!")        

else:
    print("The option you have choosen does not exist!!! Game over!!!")

