from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
ctr = 0

for text_number in range(0, len(question_data) - 1):
    question = Question(question_data[ctr]["text"], question_data[ctr]["answer"])
    question_bank.append(question)
    ctr += 1

'''
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

'''

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")