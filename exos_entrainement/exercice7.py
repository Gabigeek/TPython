def saisie():
    saisies = []
    is_valid = False
    while not is_valid:
        try:
            for x in range(2):
                is_valid = False
                saisies.append(int(input(f"saisie numéro {x+1} :")))
                is_valid = True
        except ValueError:
            print("Veuillez saisir un nombre entier correct")
    is_valid = False
    while not is_valid:
        try:
            operateur = input("Opérateur: ")
            is_valid = True
        except ValueError:
            print("Veuillez saisir un opérateur correct")

    return [operateur, saisies[0], saisies[1]]


def calcul(saisie: list):
    operateur = saisie[0]
    saisie1 = saisie[1]
    saisie2 = saisie[2]
    while True:
        try:
            if operateur not in ["+", "-", "*", "/"]:
                raise ValueError('Opérateur invalide')
            match operateur:
                case "+":
                    resultat = int(saisie1) + int(saisie2)
                    break
                case "-":
                    resultat = int(saisie1) - int(saisie2)
                    break
                case "*":
                    resultat = int(saisie1) * int(saisie2)
                    break
                case "/":
                    resultat = int(saisie1) / int(saisie2)
                    break
        except (ZeroDivisionError):
            print("division par 0 interdite")
            break
        except (ValueError):
            print("opérateur incorrect")
            break
        print("Le resultat du calcul est ", resultat)

calcul(saisie())
