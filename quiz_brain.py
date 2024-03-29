class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q{self.question_number}. {question.text} True or False?: ")

        self.check_answer(question.answer, user_answer)

    def check_answer(self, correct_answer, user_answer):
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You are correct!")
        else:
            print("You are Wrong!")
        print(f"The correct answer was: {str(correct_answer)}")
        print(f"Your current score is {self.score}/{self.question_number}.")

