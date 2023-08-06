import random
import string

letter = []
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
passList = []
# store all lowercase and uppercase letters in a list
for char in string.ascii_letters: 
    letter.append(char)

print("\n-------- P A S S W O R D   G E N E R A T O R --------\n")
letterMax = int (input("How many LETTERS in you password: "))
symbolMax= int(input("How many SYMBOLS in your password: "))
numMax = int (input("How many NUMBERS in your password: "))

for num in range(0,letterMax):
    passList.append(random.choice(letter))

for num in range(0,symbolMax):
    passList.append(random.choice(symbol))

for num in range(0,numMax):
    passList.append(str(random.randint(0,9)))

random.shuffle(passList)
password = "" 
for char in passList:
    password += char
    
print(f"\nHere is your password: {password}\n")
    
    









