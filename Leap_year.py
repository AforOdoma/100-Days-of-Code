# Which year do you want to check?
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

divisible_by_4 = year % 4 
divisible_by_100 = year % 100
divisible_by_400 = year % 400

if divisible_by_4 != 0:
  print("Not leap year")
else:
  if divisible_by_100 != 0:
    print("Leap year")

  else: 
    if divisible_by_400 != 0:
      print("Not Leap year")
    else:
      print("Leap year")