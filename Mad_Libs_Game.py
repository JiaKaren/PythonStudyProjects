# introduction
print("Welcome to Travel Mad Libs!")
print("You will be asked to enter a series of words based on the theme chosen.")
print("These words will then be used to create a fun story!")
print("Let's begin!")
print("\n")

# game function
def mad_libs():
  #word bank
  name = input("name: ")
  adjective = input("adjective: ")
  age = input("age: ")
  country = input("country: ")
  country2 = input("another country: ")
  relative = input("relative: ")
  number = input("number: ")
  transportation = input("transportation: ")
  number2 = input("number: ")
  noun = input("noun: ")
  noun2 = input("noun: ")
  adjective2 = input("adjective: ")
  food = input("food: ")
  adjective3 = input("adjective: ")

  print("\n")
  
  final_story = name + " is a(n) " + adjective + " " + age + " year old who is visiting " + country + " with their " + relative + ". Once they arrived after a " + number + " hour ride on the " + transportation + ", they were astounded by the difference between " + country + " and " + country2 + ". " + name + " and their " + relative + " had booked a stay at a " + number2 + "-star hotel, known for its " + noun + " and " + noun2 + ". Apart from these amenities, " + name + " was able to enjoy a wonderful breakfast including the native dish of " + food + ". " + name + " returned from their trip feeling more " + adjective3 + " than ever before."
  
  return print(final_story + "\n")

# replay function
def replay():
  replay = input("Do you want to play again? ")
  if replay == "yes":
    mad_libs()
  if replay == "no":
    print("Thanks for playing!")

mad_libs()
replay()