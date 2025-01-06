class question:
  def __init__(self, content, answers: list, valid_ans):
    self.content = content
    self.a_choice = answers[0]
    self.b_choice = answers[1]
    self.c_choice = answers[2]
    self.answer = valid_ans
    

  def ask(self):
    print(self.content)
    print("choix possibles: ")
    print("a) " + self.a_choice)
    print("b) " + self.b_choice)
    print("c) " + self.c_choice)
    user_input = input("Votre réponse: ")
    return user_input
  


# TODO / Check
def check_answer(user_answer, question):
  if user_answer == question.valid_ans:
    print("Bonne réponse")
  else:
    print("Mauvaise réponse")

