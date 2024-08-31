import random 

# game start
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("You have 10 attempts to guess the number.")
print("After each attempt, I'll tell you if your guess was greater or less than the number I'm thinking of.")
print("Let's begin!")

# computer picks a number
number = random.randint(1, 100)

# user guesses a number
for i in range(10):
    guess = int(input("Guess a number: "))
    if guess > 100 or guess < 1:
      print("Invalid guess. Please enter a number between 1 and 100.")
      continue
    if guess == number:
      print("Congratulations! You guessed the number in", i+1, "attempts.")
      break
    if guess > number:
      print("Your guess is greater than the number I'm thinking of.")
      i += 1
      continue
    if guess < number:
      print("Your guess is less than the number I'm thinking of.")
      i += 1

# game ending
if i > 10 and guess != number:
  print("Sorry, you ran out of attempts. The number I was thinking of was", number)
  print("GAME OVER")