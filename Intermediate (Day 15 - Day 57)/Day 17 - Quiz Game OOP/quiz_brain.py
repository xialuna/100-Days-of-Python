class QuizBrain:
    def __init__(self, q_list):
        self.ques_num = 0  # keeps track which question the user is on
        self.ques_list = q_list
        self.score = 0

    def quiz_continue(self):  # if it still has a question it will go on
        return self.ques_num < len(self.ques_list)

    def check_answer(self, answer, correct_ans):
        if answer.lower() == correct_ans.lower():
            print("CORRECT!")
            self.score += 1
        else:
            print("WRONG!")
        print(f"The correct answer is: {correct_ans}.")
        print(f"Current score: {self.score}/{self.ques_num}\n")

    def next_question(self):
        question = self.ques_list[self.ques_num]
        self.ques_num += 1
        print(f"Q{self.ques_num}: {question.text} (True or False)")
        user_ans = input("Enter answer: ")
        self.check_answer(user_ans, question.answer)
