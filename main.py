from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzlerGui
question_bank = []

for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))

user = QuizBrain(question_bank)
gui = QuizzlerGui(user)
# while user.still_has_qs():
#     user.next_qs()

print("You have completed the quiz!")
print(f"Your final score was: {user.score}/{user.qs_num}")