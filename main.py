from questions import *
from answers import *
from choices import *

#nombre de questions à poser, max 10
to_ask = 3

def score(answers):
    score = 0
    for answer in answers:
        if answer.validity == True:
            score += 1
    return score

answers = []

choices = [
    Choice(["Londres", "Paris", "Berlin"], "b"),
    Choice(["Jaune", "violet", "Bleu"], "a"),
    Choice(["2", "5", "7"], "c"),
    Choice(["Pluton", "Saturne", "La terre"], "c"),
    Choice(["4", "3", "5"], "b"),
    Choice(["Le chien", "Le Chat", "La taupe"], "b"),
    Choice(["anglais", "Basque", "Francais"], "c"),
    Choice(["4", "6", "8"], "a"),
    Choice(["Porto", "Lisbonne", "Faro"], "b"),
    Choice(["décembre", "janvier", "juillet"], "a")
]


# [question, [choix possibles], réponse]
questions = [
    Question("Quelle est la capitale de la france ?", choices[0]),
    Question("Quelle est la couleur du soleil ?", choices[1]),
    Question("Combien y a-t-il de jours dans une semaine ?", choices[2]),
    Question("Quelle planète est surnommée la planète bleue ?", choices[3]),
    Question("Combien de côtés a un triangle ?", choices[4]),
    Question("Quel est l'animal qui miaule ?", choices[5]),
    Question("Dans quelle langue dit-on bonjour en France ?", choices[6]),
    Question("Combien font 2 + 2 ?", choices[7]),
    Question("Quel est la capitale du Portugal ?",choices[8]),
    Question("Quel est le mois de l'année qui contient Noël ?", choices[9])
]

random.shuffle(questions)

for i in range(to_ask):
    answers.append(Answer(questions[i],questions[i].ask()))

## correction
for i in range(to_ask):
    print(answers[i], "\n")

print(f"Votre score est de {score(answers)} sur {to_ask}")

