import os #for clearing screen
auction = {}
addBidders = True
print("\n\033[35m---- WELCOME TO SECRET AUCTION PROGRAM! ----\033[0m")
while addBidders:
  name = input("\nEnter your name: ")
  bid = int(input("Enter your bid: $"))
  auction[name] = bid
  addBidders = input("Are there any other bidders?\n\t[Y] Yes\n\t[N] No\nEnter Choice: ").upper()

  if addBidders == "N":
    addBidders = False
  os.system('cls')

bid = 0
winner = ""
for name in auction:
  currentBid = auction[name]
  if currentBid > bid:
    bid = currentBid
    winner = name

print(f"\033[32mThe winner is {winner} with a bid of ${auction[winner]}\033[0m\n")

    
    


