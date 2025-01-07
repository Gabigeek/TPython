from questions import *
from answers import *

#nombre de questions à poser
to_ask = 3

def score(answers):
    score = 0
    for answer in answers:
        if answer.validity == True:
            score += 1
    return score

answers = []

# [question, [choix possibles], réponse]
questions = [
    Question("Quelle est la capitale de la france ?", ["Londres", "Paris", "Berlin"], "b"),
    Question("Quelle est la couleur du soleil ?", ["Jaune", "violet", "Bleu"], "a"),
    Question("Combien y a-t-il de jours dans une semaine ?", ["2", "5", "7"], "c"),
    Question("Quelle planète est surnommée la planète bleue ?", ["Pluton", "Saturne", "La terre"], "c"),
    Question("Combien de côtés a un triangle ?", ["4", "3", "5"], "b"),
    Question("Quel est l'animal qui miaule ?", ["Le chien", "Le Chat", "La taupe"], "b"),
    Question("Dans quelle langue dit-on bonjour en France ?", ["anglais", "Basque", "Francais"], "c"),
    Question("Combien font 2 + 2 ?", ["4", "6", "8"], "a"),
    Question("Quel est la capitale du Portugal ?", ["Porto", "Lisbonne", "Faro"], "b"),
    Question("Quel est le mois de l'année qui contient Noël ?", ["décembre", "janvier", "juillet"], "a")
]

random.shuffle(questions)

for i in range(to_ask):
    answers.append(Answer(questions[i],questions[i].ask()))

## correction
for i in range(to_ask):
    print(answers[i], "\n")

print(f"Votre score est de {score(answers)} sur {to_ask}")

