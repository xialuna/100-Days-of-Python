evenTotal = 0
# FIRST WAY:
for even in range(1,101):
    if even % 2 == 0:
        evenTotal += even

#SECOND WAY:
for even in range(2,101,2):
    evenTotal += even

print(evenTotal)