import random

"""
FIX BUG: When does loop stop looping?
"""

print("Welcome to the Rock, Paper, Scissors Game!")
print("You will have five matches with the computer.")
print("With each turn, you may enter one of the following: ROCK, PAPER, SCISSORS. A tie will result in a point for both players. Remember: ROCK beats SCISSORS, SCISSORS beats PAPER, and PAPER beats ROCK.\n")

#setting variables
player_name = input("What is your name? ")
player_score = 0
computer_score = 0
player = False

a = ["ROCK", "PAPER", "SCISSORS"]
computer = random.choice(a)

for i in range(5):
  while player == False:
  #set player to True
      player = input("ROCK, PAPER, SCISSORS?")
      if player == computer:
          print("Tie!")
          i += 1
          player_score += 1
          computer_score += 1
      elif player == "ROCK":
          if computer == "PAPER":
              print("You lose!", computer, "covers", player)
              i += 1
              computer_score += 1
          else:
              print("You win!", player, "smashes", computer)
              i += 1
              player_score += 1
      elif player == "PAPER":
          if computer == "SCISSORS":
              print("You lose!", computer, "cut", player)
              i += 1
              computer_score += 1
          else:
              print("You win!", player, "covers", computer)
              i += 1
              player_score += 1
      elif player == "SCISSORS":
          if computer == "ROCK":
              print("You lose...", computer, "smashes", player)
              i += 1
              computer_score += 1
          else:
              print("You win!", player, "cut", computer)
              i += 1
              player_score += 1
      else:
          print("That's not a valid play. Check your spelling!")
          continue
      #player was set to True, but we want it to be False so the loop continues
      player = False
      computer = random.choice(a)
  if i > 5:
    continue

if computer_score > player_score:
  print("The computer won!")
  print("Computer score: ", str(computer_score))
  print("Player score: ", str(player_score))
elif computer_score < player_score:
  print(player_name, "won!")
  print("Computer score:", str(computer_score))
  print("Player score:", str(player_score))