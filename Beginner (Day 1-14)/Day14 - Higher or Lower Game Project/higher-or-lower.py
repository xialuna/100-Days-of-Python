from game_data import data
from art import logo, versus, borderTop, borderBottom
import random
import os #for clearing screen
from time import sleep #for delay when clearing the screen
def getData(compareData):
  '''randomly selects an info from data and assigns it to a variable'''
  info = random.choice(data)
  while compareData == info: #Avoid having the same choices
    info = random.choice(data)
  return info

def printData(data, letter):
  '''Format data and prints it'''
  print(borderTop)
  print(f'\t     Compare {letter}:\n\n\t{data["name"]}\n\tA {data["description"]}\n\tFrom {data["country"]}')
  print(borderBottom)

def checkGuess(answer,follows_a,follows_b):
  '''check which data has the more followers, returns true or false based on if answer is equal to the data with more followers'''
  if follows_a > follows_b:
    return answer == "A" 
  else:
    return answer == "B"

data_a= ""
play = True
points = 0
data_a = getData(data_a)

while play:
  print(logo)
  data_b = getData(data_a)
  follows_a = data_a['follower_count']
  follows_b = data_b['follower_count']

  printData(data_a,"A")
  print(versus)
  printData(data_b,"B")
  print(f"\033[35mCURRENT SCORE: {points}\033[0m")
  answer = input(f'Who has more followers (A or B)?\nEnter choice: ').upper()

  if checkGuess(answer,follows_a,follows_b):
    data_a = data_b
    points += 1
    print(f"\n\033[32mYOU WERE RIGHT!\033[0m")
    sleep(1)
    os.system('cls')
  else:
    print(f"\n\033[31mGAME OVER! You entered the wrong answer\033[0m\nFinal Score: {points}\n")
    play = False
