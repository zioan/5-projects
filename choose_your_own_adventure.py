name = input("Type your name: ").capitalize()
print("Welcome", name, "to the adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around or swim accross? walk or swim? ").lower()

  if answer == "swim":
    print("You swam across and were eaten by an alligator.")
  elif answer == "walk":
    print("You walked for many miles, ran out of water and you lost the game!")
  else:
    print("Not a valid option. You lose.")

elif answer == "right":
  print("You wan the game!")
else:
  print("Not a valid option. You lose.")