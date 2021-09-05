import random

top_range = input("Type a number: ")

if top_range.isdigit():
  top_range = int(top_range)
  if top_range <= 0:
    print("Please type a number larget than 0 next time.")
    quit()
else:
  print("Please type a number next time!")
  quit()

random_number = random.randint(0, top_range)

print(f"Try to guess a number between 0 and {top_range}")

guesses = 0

#while user_guess != random_number:
while True:
  guesses += 1
  user_guess = input("Make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("Please type a number next time!")
    continue

  if user_guess == random_number:
    print("You got it!")
    break
  elif user_guess > random_number:
    print("You where above the number!")
  else:
    print("You where below the number!")

print("You got it in", guesses, "guesses!")