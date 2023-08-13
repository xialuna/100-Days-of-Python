import random
import os
from blackjackLogo import logo
choice = input("Do you want to play a game of blackjack?\n\t  [Y] Yes   [N] No\nEnter choice: ").upper()
 
def randomCard(score):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  if (card == 11) and (score + card > 21):
    card = 1
  return card

while choice == "Y":
    os.system('cls')
    print(logo)
    p1_cards = []
    p2_cards = []
    end = False
    for index in range(2):
      p1_cards.append(randomCard(0))
      p2_cards.append(randomCard(0))

    while not end:
      score1 = sum(p1_cards)
      score2 = sum(p2_cards)  
      if score1 == 21 or score2 == 21:
        result = "\033[32mBLACKJACK! YOU WIN\033[0m" if score1 == 21 else "\033[31mDEALER HAS A BLACKJACK! YOU LOSE\033[0m"
        break
      
      if score1 > 21:
          result = "\033[31mBUST! DEALER WINS\033[0m"
          break
      
      print(f"Your cards: {p1_cards}  ||  Current Score: {score1}")
      print(f"Dealer's first card: {p2_cards[0]}")
      choice = int(input("\n[1] Get another card\n[2] Pass\nEnter Choice: "))
         
      if choice == 1:
          p1_cards.append(randomCard(score1))
          continue
      else:
          if score1 == score2:
            result = "\033[34mPUSH! IT'S A DRAW\033[0m"
          else:
            while score2 < 17:
                p2_cards.append(randomCard(score2))
                score2 = sum(p2_cards)
            if score2 > 21 or score2 < score1:
                result = "\033[32mYOU WIN!\033[0m"

            else:
               result = "\033[31mYOU LOSE\033[0m"
          end = True
      
    print(f"\n\033[35mYour cards: {p1_cards}  ||  Total Score: {score1}")
    print(f"Dealer's cards: {p2_cards}  ||  Dealer's Score: {score2}\n\n{result}")
    choice = input("\nWould you like to play again?\n\t[Y] Yes   [N] No\nEnter choice: ").upper()