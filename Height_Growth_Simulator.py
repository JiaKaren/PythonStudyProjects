# obtaining user input
print("Hi, welcome to the height growth simulator! This is a program that determines a child's height from from 2 to 20 years old.")
gender = input("Enter male or female: ")
age = input("Enter age: ")
current_height = input("Enter current height: ")
mother_height = input("Enter mother's height in cm: ")
father_height = input("Enter father's height in cm: ")

# height calculator
def percentile_calculator(gender, age, mother_height, father_height):
  #male percentiles
  if gender == "male" and age == "2":
    if currrent_height <= 81:
      percentile = 5
    elif current_height > 81 and current_height <= 82:
      percentile = 10
    elif current_height > 82 and current_height <= 84:
      percentile = 15
    elif current_height > 84 and current_height <= 86:
      percentile = 25
    elif current_height > 86 and current_height <= 89:
      percentile = 50
    elif current_height > 89 and current_height <= 91:
      percentile = 75
    elif current_height > 91 and current_height <= 93:
      percentile = 90
    elif current_height > 93:
      percentile = 95
  if gender == "male" and age == "3":
    if currrent_height <= 89:
      percentile = 5
    elif current_height > 89 and current_height <= 90:
      percentile = 10
    elif current_height > 90 and current_height <= 92:
      percentile = 15
    elif current_height > 92 and current_height <= 95:
      percentile = 25
    elif current_height > 95 and current_height <= 97:
      percentile = 50
    elif current_height > 97 and current_height <= 100:
      percentile = 75
    elif current_height > 100 and current_height <= 102:
      percentile = 90
    elif current_height > 102:
      percentile = 95
  if gender == "male" and age == "4":
    if currrent_height <= 95:
      percentile = 5
    elif current_height > 97 and current_height <= 99:
      percentile = 10
    elif current_height > 99 and current_height <= 84:
      percentile = 15
    elif current_height > 84 and current_height <= 101:
      percentile = 25
    elif current_height > 101 and current_height <= 105:
      percentile = 50
    elif current_height > 105 and current_height <= 107:
      percentile = 75
    elif current_height > 107 and current_height <= 109:
      percentile = 90
    elif current_height > 109:
      percentile = 95
  if gender == "male" and age == "5":
    if currrent_height <= 101:
      percentile = 5
    elif current_height > 81 and current_height <= 82:
      percentile = 10
    elif current_height > 82 and current_height <= 84:
      percentile = 15
    elif current_height > 84 and current_height <= 86:
      percentile = 25
    elif current_height > 86 and current_height <= 89:
      percentile = 50
    elif current_height > 89 and current_height <= 91:
      percentile = 75
    elif current_height > 91 and current_height <= 93:
      percentile = 90
    elif current_height > 93:
      percentile = 95

  #female percentiles
  return percentile

if gender == "male":
  mid_parental_height = (float(mother_height) + float(father_height) + 13) / 2
elif gender == "female":
  mid_parental_height = (float(mother_height) + float(father_height) - 13) / 2

# user output
#- current percentile
#- mid parental height
#- predicted height
#- ways to grow taller 
print(str(mid_parental_height) + "cm")