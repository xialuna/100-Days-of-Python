print("SHARED BILL TIP CALCULATOR")
bill = float(input("Enter the total bill: ₱"))
tipPercent = int(input("Enter tip percentage to give: "))
personNum = int(input("Enter number of people to split the bill: "))

tipPercent /= 100
totalTip = bill * tipPercent
indivTip = totalTip/personNum
totalBill = (bill/personNum) + indivTip

print("\n------------ R E S U L T ------------")
print(f"\tTotal Tip ({int(tipPercent * 100)}%): ₱{totalTip:.2f}")
print(f"\tTip per Person: ₱{indivTip:.2f}")
print(f"\tTotal Bill Amount: ₱{(bill + totalTip):.2f}")
print(f"\tTotal Bill per Person: ₱{totalBill:.2f}")
