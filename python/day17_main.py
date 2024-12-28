from day17_question_model import Question
from day17_data import question_data
from day17_quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    question_bank.append(Question(question_text,question_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.nextquestion()

print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{quiz.question_number}")