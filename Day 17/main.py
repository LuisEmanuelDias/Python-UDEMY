from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    m = Question(x["question"], x["correct_answer"])
    question_bank.append(m)

quizz = QuizBrain(question_bank)

state = True
score = 0
while quizz.still_has_questions():

    quizz.next_question()

print(f"You complete the quiz\nYour final score was {quizz.score}/{quizz.question_number}")


