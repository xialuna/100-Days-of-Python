import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
max = (len(names)) - 1
index = random.randint(0,max)

winner =  names[index]
print(f"{winner} is going to buy the meal today!")