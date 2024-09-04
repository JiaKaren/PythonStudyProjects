import random

#intro
print("The peppered moth is usually white with black speckles. However, sometimes there may be genetic mutations that cause the moth to have almost black wings. The white moth is better camouflaged in the forest.")
print("In the 1800s, pollution from industrial smoke and soot killed off lichens and darkened tree trunks and walls in towns and cities. This made the paler moths more visible to predators, while the darker variety became more camouflaged. As a result, the black form of the peppered moth rapidly took over in industrial parts of the UK, and by the end of the nineteenth century, the original wild type was almost lost in some areas.\n")

#first generation
print("Now it's time for you to design an environment! Fill in the blanks to create your first generation of moths.")

forest_color = input("Black or white forest? ")
white_moth_percentage = int(input("White moth percentage (enter integer from 1 to 100): "))
black_moth_percentage = int(100-white_moth_percentage)
print("Black moth percentage: ", str(black_moth_percentage))
input("I'm ready to start the simulation! Press enter to begin.\n")

#fixed variables
if forest_color == "black":
  white_survival_rate = random.randint(70, 80) * 0.01
  black_survival_rate = random.randint(80, 90) * 0.01
elif forest_color == "white":
  black_survival_rate = random.randint(70, 80) * 0.01
  white_survival_rate = random.randint(80, 90) * 0.01
generation = 1
mutation_rate = random.randint(0, 10) * 0.01
reproduction_rate = random.randint(10, 50) * 0.01

# repeating variables
remaining_white_moths = int(white_moth_percentage * white_survival_rate)
remaining_black_moths = int(black_moth_percentage * black_survival_rate)

#simulation
def simulation(starting_white_moths, starting_black_moths):  
  print("GENERATION", generation)
  print("Forest color: ", forest_color)
  print("Starting white moths: ", starting_white_moths)
  print("Starting black moths: ", starting_black_moths)
  print("Remaining white moths: ", remaining_white_moths)
  print("Remaining black moths: ", remaining_black_moths)

simulation(white_moth_percentage, black_moth_percentage)