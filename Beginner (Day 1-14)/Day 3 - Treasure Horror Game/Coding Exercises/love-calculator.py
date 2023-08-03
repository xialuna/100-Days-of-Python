# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
keyWord1 = "true"
keyWord2 = "love"
nameCombine = name1.lower() + name2.lower()

trueCount = 0
loveCount = 0

for index in range(4):
    count = nameCombine.count(keyWord1[index])
    trueCount += count

for index in range(4):
    count = nameCombine.count(keyWord2[index])
    loveCount += count

score = int(str(trueCount) + str(loveCount)) #typecasting to concatenate int 

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")