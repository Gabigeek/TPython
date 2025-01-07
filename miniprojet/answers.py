from questions import *
from choices import *

class Answer:
    def __init__(self, question, user_answer):
        self.question = question
        self.user_answer = user_answer
        self.validity = is_correct(question, user_answer)
    def __str__(self):
        if self.validity == True:
            valid_str = "Oui"
        else:
            valid_str = "Non"
        return f"Question posée: {self.question.content}\nVotre réponse: {self.user_answer}\nEst-ce correcte: {valid_str}\n"
        


def is_correct(question: Question, user_answer):
    if user_answer == question.answer:
        return True
    else:
        return False
    

