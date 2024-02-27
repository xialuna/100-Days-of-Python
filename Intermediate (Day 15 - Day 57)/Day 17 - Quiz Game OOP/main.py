from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.quiz_continue():
    quiz.next_question()

print("Congratulations! You've completed the quiz.")
print(f"Final Score: {quiz.score}/{len(question_bank)}")
