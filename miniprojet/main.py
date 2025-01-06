from questions import *


Question1 = question("Quelle est la capitale de la france ?", ["Londres", "Paris", "Berlin"], "b")

user_answer = Question1.ask()
if user_answer == Question1.answer:
  print("Bonne réponse")
else:
  print("Mauvaise réponse")