class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return (len(self.question_list)>len(self.question_number))
         
        
    def nextquestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}:{current_question.text}(True/False):")
        self.checkanswer(current_question.answer,answer)

    def checkanswer(self,current_answer,answer):
        if current_answer.lower() == answer.lower():
            self.score += 1
            print("You got correct answer!")
        else:
            print("You got wrong answer!")
        print(f"The correct answer is {current_answer}")
        print(f"Your current Score is :{self.score}/{self.question_number}")
        print("\n")