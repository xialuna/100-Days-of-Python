import random
print("GENERATE A BAND NAME")
print("Tell us a bit about your band!")
adj1 = input("\t\033[32m Positive adjective to describe your band: \033[0m") #\033[33m adds color to the text
adj2 = input("\t\033[32m Negative adjective to describe your band: \033[0m")
petName = input("\t\033[33m First pet's name: \033[0m")
celebName = input("\t\033[33m Favorite celebrity's name: \033[0m")
place1 = input("\t\033[34m Name of the city you grew up in: \033[0m")
place2 = input("\t\033[34m Country you would like to visit: \033[0m")

#Store variables in a list to randomize later on
adjList = [adj1, adj2] 
nameList = [petName,celebName]
placeList = [place1, place2]

print("\nYour band name can be: ")
for index in range(3):
  #Randomly pick between the variables inside the list
  adjective = random.choice(adjList)
  name = random.choice(nameList)
  place = random.choice(placeList)
  #use comma instead of '+' to concatenate to add space in between the variables
  print("\tOption",index + 1, ":", adjective, name , place)

print("\n")






