student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)): #convert each element to int
  student_scores[n] = int(student_scores[n])
print(student_scores)

#FIRST WAY: using for loop
maxScore = student_scores[0]
for score in student_scores:
    if score > maxScore:
        maxScore = score

#SECOND WAY: using max()
maxScore = max(student_scores)

print(f"The highest score in the class is: {maxScore}")
    




