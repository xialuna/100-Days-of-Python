import random
import os #for clearing screen
from time import sleep #for delay when clearing the screen
from hangman_words import movies, countries, randomWords, mixList
from hangman_ASCII import hangman, mainLogo, winLogo, loseLogo
gameOver = False
loseCount = 0
word = []
answerList = []

print(mainLogo)
print("Pick a category:\n\t[1] Movies\n\t[2] Countries\n\t[3] Random Words\n\t[4] Mix All Themes")
category = int(input("Enter choice: "))
os.system('cls')

if category == 1:
   wordChoice = random.choice(movies)
   categoryName = "Movies"
elif category == 2:
   wordChoice = random.choice(countries)
   categoryName = "Countries"
elif category == 3:
   wordChoice = random.choice(randomWords)
   categoryName = "Random Words"
else:
   wordChoice = random.choice(mixList)
   categoryName = "Mix All Themes"

keyWord = [letter for letter in wordChoice] #using List Comprehension
length = len(keyWord) 

for letter in keyWord: #assigning blank to every letter in keyWord
    if letter == " ": #if there's a space in the keyWord
       word.append(" ")
    else:
      word.append("_")

def printBlanks(word): #function to print blanks and spaces
    for letter in word:
        print(letter + " ", end="")
    print("\n")
   
while not gameOver:
  found = 0
  print(f"---------- Category: {categoryName} ----------\n")
  print("" + hangman[loseCount])
  printBlanks(word)
  answer = input("Guess a letter: ").lower()

  if answer in answerList:
    print(f"\033[36mYou've already guessed '{answer}'. Try Again!\033[0m")
    found = 1
    sleep(1)
  else:
    answerList.append(answer)

  for index in range(length):
     if answer == keyWord[index]:
        word[index] = answer
        answerList.append
        found = 1

  if not found:
     loseCount += 1
     print(f"\033[31m'{answer}' is not in the word. You lose a life!\033[0m")
     sleep(1)

  os.system('cls')
  if word == keyWord or loseCount == 6:
     gameOver = True
     if word == keyWord:
        print(winLogo)
     else:
        print(loseLogo)
        print(f"The word is: {wordChoice}\n")


