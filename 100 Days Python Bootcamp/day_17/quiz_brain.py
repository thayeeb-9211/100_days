
class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def correct_answer(self, player_answer, answer):
        return player_answer == answer

    def check_answer(self, player_answer, answer):

        if self.correct_answer(player_answer, answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number +1}\n")
        self.question_number +=1

    def next_question(self):
        question = self.question_list[self.question_number]
        player_answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)?: ")\
            .capitalize()
        self.check_answer(player_answer,question.answer)

    def play_quiz(self):

        num_of_questions = len(self.question_list)
        print("Welcome to the Big Quiz!")
        while self.question_number < num_of_questions:
            self.next_question()
        print(f"That's the end of the quiz! Your final score is {self.score}/{num_of_questions}")

