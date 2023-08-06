student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#FIRST WAY: without using sum() or len()
aveHeight = 0
studentCount = 0

for height in student_heights:
    aveHeight += height
    studentCount += 1
aveHeight /= studentCount

print(round(aveHeight))

#SECOND WAY: using sum() and len()
aveHeight = sum(student_heights) / len(student_heights)
print(round(aveHeight))