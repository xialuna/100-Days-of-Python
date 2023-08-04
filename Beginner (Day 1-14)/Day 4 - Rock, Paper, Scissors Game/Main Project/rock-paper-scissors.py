import random
print ("------ Welcome to 🪨📄✂️ GAME! ------")
choice= int(input("Play against:\n\t[1] Another Player\n\t[2] Computer\nEnter Choice: "))
round = int(input ("How many rounds would you like to play? "))

if choice == 1:
  name1 = input ("\nPlayer 1 Name: ")
  name2 = input ("Player 2 Name: ")
  from getpass import getpass as input #prevents players from seeing each other's choice
else:
  name1 = "Computer"
  name2 = input("\nEnter your name: ")
  gameOption = ["R","P","S"]

invalid = 0
count = 0
p1_score = 0
p2_score = 0

while count != round:
  count += 1
  print ("\n\033[0m----------- ROUND",count,": FIGHT! -----------")
  print ("Select your move: R, P, or S")
  if choice == 1:
    p1 = input (f"{name1}'s Turn > ")
    p1 = p1.upper()
  else:
    compChoice = random.randint(0,2)
    p1 = gameOption[compChoice]
  p2 = input (f"{name2}'s Turn > ")
  p2 = p2.upper()
  if p1 == "R":
    if p2 == "S":
      p1_score += 1
      print (f"\033[35m{name1}'s Rock beats {name2}'s Scissors!")
    elif p2 == "P":
      p2_score += 1
      print (f"\033[35m{name2}'s Paper beats {name1}'s Rock!")
    elif p2 == "R":
      print ("\033[31mIt's a TIE! You have both used Rock")
    else:
      invalid = 1
      
  elif p1 == "P":
    if p2 == "S":
      p2_score += 1
      print (f"\033[35m{name2}'s Scissors beats {name1}'s Paper!")
    elif p2 == "R":
      p1_score += 1
      print (f"\033[35m{name1}'s Paper beats {name2}'s Rock!")
    elif p2 == "P":
      print ("\033[31mIt's a TIE! You have both used Paper")
    else:
      invalid = 1
  
  elif p1 == "S":
    if p2 == "R":
      p2_score += 1
      print (f"\033[35m{name2}'s Rock beats {name1}'s Scissors!")
    elif p2 == "P":
      p1_score += 1
      print (f"\033[35m{name1}'s Scissors beats {name2}'s Paper!")
    elif p2 == "S":
      print ("\033[35mIt's a TIE! You have both used Scissors")
    else:
      invalid = 1
      
  else:
    invalid = 1
  if invalid == 1:
    print ("\033[31mInvalid Input. Try Again")
    count -= 1
    invalid = 0
    continue

  print(f"\n\033[33mCurrent Points:\n\t{name1}'s Score: {p1_score}\n\t{name2}'s Score: {p2_score}\033[0m")
  if count == round:
    if p1_score > p2_score:
      if choice == 1:
        print (f"\n\033[32mCongratulations {name1},YOU WON!\n\033[0m")
      else:
        print("\n\033[31mYou Lost! Better luck next time\n\033[0m")
    elif p2_score > p1_score:
        print (f"\n\033[32mCongratulations {name2},YOU WON!\n\033[0m")
    else:
      print ("\n\033[31mIT'S a TIE, play a tie breaker \n\033[0m")
      count-=1
      
        
      
  
  
