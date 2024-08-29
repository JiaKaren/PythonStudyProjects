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

#variables
if forest_color == "black":
  white_death_rate = random.randint(20, 30) * 0.01
  black_death_rate = random.randint(10, 20) * 0.01
elif forest_color == "white":
  black_death_rate = random.randint(20, 30) * 0.01
  white_death_rate = random.randint(10, 20) * 0.01

reproduction_rate = random.randint(10, 50) * 0.01

remaining_white_moths = int(white_moth_percentage - white_moth_percentage * white_death_rate)

remaining_black_moths = int(black_moth_percentage - black_moth_percentage * black_death_rate)

generation = 1

#simulation

def generation_simulator(forest_color, generation, white_moth_percentage, black_moth_percentage):
  print("Generation", str(generation))
  int("Forest color: ", forest_color)
  print("Starting white moths: ", white_moth_percentage)
  print("Starting black moths: ", black_moth_percentage)
  print("Remaining white moths: ", remaining_white_moths)
  print("Remaining black moths: ", remaining_black_moths)
  print("The reproduction rate is", reproduction_rate)
  return 

generation_simulator(forest_color, generation, white_moth_percentage, black_moth_percentage)