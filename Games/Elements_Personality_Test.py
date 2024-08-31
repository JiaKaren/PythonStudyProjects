# intro
print("Welcome to the elements personality test!")
print("This test will determine what element you are based on your answers. According to the Chinese taoist belief, there are four elements: water, earth, metal, and fire.")
print("There will be a few multiple-choice questions for you to respond to. No answer is better than the other- just type the letter of your answer.")

# setting answer variables
'''
A = water
B = earth
C = metal
D = fire
'''

A_count = 0
B_count = 0
C_count = 0
D_count = 0

# question 1
print("1. In a group of people/friends, which position do you take on?")
print("A. Emotional supporter\nB. Honest advisor\nC. Event organizer\nD. Passionate motivator\n")
question_1 = input("\nYour answer: ").upper()

if question_1 == "A":
  A_count += 1
elif question_1 == "B":
  B_count += 1
elif question_1 == "C":
  C_count += 1
elif question_1 == "D":
  D_count += 1
else:
  print("Sorry, I don't understand that answer.")

# question 2
print("\n2. How do you complete a task/assignment?")
print("A. I collaborate and communicate with others\nB. I lock in during the last few days before the due date\nC. I make an organized plan for study sessions to work on a little each day\nD. I prefer to complete the task right away/as soon as possible")
question_2 = input("\nYour answer: ").upper()

if question_2 == "A":
  A_count += 1
elif question_2 == "B":
  B_count += 1
elif question_2 == "C":
  C_count += 1
elif question_2 == "D":
  D_count += 1
else:
  print("Sorry, I don't understand that answer.")

# question 3
print("\n3. What type of writing do you prefer?")
print("A. Writing a realistic story from my personal experiences\nB. A research paper on a scientific subject\nC. An analysis of a literary text\nD. A strong argumentative essay")
question_3 = input("\nYour answer: ").upper()

if question_3 == "A":
  A_count += 1
elif question_3 == "B":
  B_count += 1
elif question_3 == "C":
  C_count += 1
elif question_3 == "D":
  D_count += 1
else:
  print("Sorry, I don't understand that answer.")

# question 4
print("\n4. Which activity do you enjoy the most?")
print("A. Reading a book\nB. Being in nature/moving my body\nC. Organizing/journaling/planning \nD. Meeting up with friends")
question_4 = input("\nYour answer: ").upper()

if question_4 == "A":
  A_count += 1
elif question_4 == "B":
  B_count += 1
elif question_4 == "C":
  C_count += 1
elif question_4 == "D":
  D_count += 1
else:
  print("Sorry, I don't understand that answer.")

# question 5
print("\n5. What is your biggest weakness?")
print("A. My indecisiveness\nB. Prioritizing others before myself\nC. My stubornness\nD. My impulsiveness")
question_5 = input("\nYour answer: ").upper()

if question_5 == "A":
  A_count += 1
elif question_5 == "B":
  B_count += 1
elif question_5 == "C":
  C_count += 1
elif question_5 == "D":
  D_count += 1
else:
  print("Sorry, I don't understand that answer.")

# question 6
print("\n6. Which value is the most important to you?")
print("A. Family/Friendship\nB. Loyalty\nC. Discipline\nD. Passion")
question_6 = input("\nYour answer: ").upper()

if question_6 == "A":
  A_count += 1
elif question_6 == "B":
  B_count += 1
elif question_6 == "C":
  C_count += 1
elif question_6 == "D":
  D_count += 1

# giving results
if A_count == max(A_count, B_count, C_count, D_count):
  print("\nYou are water! 💧💧💧")
elif B_count == max(A_count, B_count, C_count, D_count):
  print("\nYou are earth! 🌲🌲🌲")
elif C_count == max(A_count, B_count, C_count, D_count):
  print("\nYou are metal! 💎💎💎")
elif D_count == max(A_count, B_count, C_count, D_count):
  print("\nYou are fire! 🔥🔥🔥")