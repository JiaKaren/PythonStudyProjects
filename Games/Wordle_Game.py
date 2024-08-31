import random

# word library
five_letter_words = ["depth", "flesh", "frost", "gloom", "haste", "beach", "guard" , "horse", "house", "judge", "knife", "light", "money", "night", "order", "party", "queen", "radio", "scale", "taste", "under", "video", "woman", "youth", "zebra", "apple", "beard", "chair", "dream", "eagle", "fence", "grape", "honey", "image", "jolly", "kneel", "lemon", "mango", "noble", "ocean", "pizza", "rider", "sugar", "tiger", "uncle", "virus", "waste", "xenon", "yacht", "abuse", "baker", "chase", "drain", "eager", "fable", "giant", "happy", "peach", "quail", "quilt", "juice", "knock", "leash", "melon", "nurse", "oasis", "punch", "quake", "ruler", "sweat", "tulip", "umbra", "vague", "waltz", "xerox"]

word = random.choice(five_letter_words)

# game starts
print("Welcome to Hangman!")
print("Guess the five-letter word in ten tries.")
print("With each guess, all occurrences of that letter will be revealed.")
print("Let's begin! \n")

# player guesses
blank_word = ["_", "_", "_", "_", "_"]

for i in range(10):
  print(blank_word)
  guess = input("Guess a letter: ")
  if guess in word:
    print("This letter appears " + str(word.count(guess)) + " time(s) in the word. \n")
    i += 1
    for w in range(len(word)):
      blank_word[word.index(guess)] = guess
      w += 1
  if guess not in word:
    print("This letter is not in the word. \n")
    i += 1
  if blank_word[0] + blank_word[1] + blank_word[2] + blank_word[3] + blank_word[4] == word:
    print("Congratulations! You guessed the word: " + word)
    break

# game ends
if i > 0 and blank_word[0] + blank_word[1] + blank_word[2] + blank_word[3] + blank_word[4] != word:
  print("You have used all your guesses. The word was " + word + ".")
print("Thanks for playing!")
print("GAME OVER")