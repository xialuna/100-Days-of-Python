import string, cipherLogo
alphabet = []
for char in string.ascii_lowercase: # store all lowercase letters in a list
    alphabet.append(char)

def cipher(message, shift, action):
    translated = ""
    for letter in message:
        if letter in alphabet:
          if action == 1: #ENCODE MESSAGE
            index = (alphabet.index(letter)) + shift
            if index >= 26: #if index exceeds letter 'z' it goes back to the start
              index = abs(index - 26)
          else: #DECODE MESSAGE
            index = (alphabet.index(letter)) - shift
          translated += alphabet[index]
        else: # if special characters or numbers
          translated += letter
    print(f"\033[32mTranslated Message: {translated}\033[0m")
        
end = False
print(cipherLogo.logo)   
while not end:
  choice = int(input("\t\t [1] Encode Message\n\t\t [2] Decode Message\n\nEnter Choice: "))
  message = input("Enter message: ")
  shift = int(input("Enter shift number: "))
  shift = shift % 26
  cipher(message, shift, choice)

  choice = input("\nWould you like to try again?\n\t[Y] Yes\n\t[N] No(Exit)\nEnter Choice: ").upper()
  print("\n-------------------------------------------------------------\n")
  if choice == 'N':
     end = True

print("\t   Thank you for using my program!\n")


