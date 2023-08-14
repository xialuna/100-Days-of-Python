import random
from logo import logo
EASY = 10
HARD = 5
guess = 0

def randomNum():
  choice = int(input("\nPick the range you would like to guess from:\n\t[1] 1 to 10\n\t[2] 1 to 100\nEnter Choice: "))
  range = 10 if choice == 1 else 100
  return random.randint(1,range)

print(logo)
difficulty = int(input("Choose level of difficulty:\n\t[1] Easy\n\t[2] Hard\nEnter Choice: "))
limit = EASY if difficulty == 1 else HARD
tries = limit
answer = randomNum()
while answer != guess and tries > 0:
  print(f"\n-- You have {tries} turns left --")
  guess = int(input("Guess the mystery number: "))
  tries -= 1
  if guess < answer:
    print ("\033[35mThat's too low!\033[0m")
  elif guess > answer:
    print ("\033[35mThat's too high!\033[0m")

if guess == answer:
  print (f"\n\033[32mYOU WON! It took you {limit - tries} tries to guess {answer}\033[0m")
else:
   print (f"\n\033[31mYOU LOSE! The number was {answer}\033[0m")