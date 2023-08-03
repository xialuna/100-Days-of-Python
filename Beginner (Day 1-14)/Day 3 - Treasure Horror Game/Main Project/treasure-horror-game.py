print("\033[0m\t--------------------  T H E  H A U N T I N G  Q U E S T  --------------------")
print('''\nYou are a child trapped in another dimension, with other-worldly creatures as your parents.
Your only way to escape this creepy realm is by finding a treasure chest.
      \tRules:
      \t1.) You shouldn't go to the attic past 10 PM; mother will be out to get you.
      \t2.) You shouldn't go to the basement; father will be angry.
      \t3.) You shouldn't go outside; they will be angry.''')

print("\n\033[35mIt's currently 3 PM and you woke up to the sound of crying in the attic.\033[0m")
print('''\t[1] Investigate the crying sound and go to the attic.
      \t[2] Better safe than sorry, ignore the sound and sleep again.
      \t[3] Ignore the sound and try to escape.''')

choice = int(input("What should you do? "))

if (choice == 1) or (choice == 2):
    print("\n\033[35mThe sound was too loud to let you sleep.\nYou decide to investigate the attic.\nYou saw a door with weird symbols.\033[0m")
    print("\t[1] Go and open the door.\n\t[2] Leave and go back to your room.")
    choice = int(input("What should you do? "))
    if (choice == 1):
      print("\n\033[35mUpon entering, you saw an empty room with 2 doors.\nInside the 1st door was a child that looks like you, crying.\nThe 2nd door contains a porcelain doll with the message 'Help Me'\033[0m")
      print("\t[1] Go to the 1st door (crying child)\n\t[2] Go to the 2nd door (porcelain doll)")
      choice = int(input("What should you do? "))
      if(choice == 1):
         print("\n\033[35mThe child stopped crying and smiled eerily at you.\nChild: \"The treasure you are finding is in the basement\"\033[0m")
         print("\t[1] Trust it and go back to the basement\n\t[2] Go to the second room with the porcelain doll")
         choice = int(input("What should you do? "))
         if(choice == 1):
            print("\n\033[32mYou decided to trust it and found the treasure and escape! [SAFE ENDING]\033[0m")
      if(choice == 2):
         print("\n\033[31mIt was a trap! The doll turned into mother and killed you [GAME OVER]\033[0m")
    else:
      print("\n\033[31mYou met mother on your way back and she killed you [GAME OVER].\033[0m")
        
else:
    print("\n\033[31mYou met father in the living room and he killed you [GAME OVER]\033[0m.")
    
