from choices import *

class Question():
  def __init__(self, content, choices: Choice):
    self.content = content
    #super().__init__(choices.possible_choices, choices.valid_choice)
    self.a_choice = choices.possible_choices[0]
    self.b_choice = choices.possible_choices[1]
    self.c_choice = choices.possible_choices[2]
    self.answer = choices.valid_choice

    

  def ask(self):
    print(self.content)
    print("choix possibles: ")
    print("a) " + self.a_choice)
    print("b) " + self.b_choice)
    print("c) " + self.c_choice)
    while True:
      try:
        user_input = input("Votre réponse: ")
        user_input = user_input.lower()
        if user_input not in ["a", "b", "c"]:
                raise ValueError('saisie utilisateur invalide')
      except ValueError:
        print("Veuillez saisir une réponse correcte")
      else:
        break
    return user_input