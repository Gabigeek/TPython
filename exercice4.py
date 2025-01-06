def saisie():
    saisie1 = input("1er nombre: ")
    saisie2 = input("2ème nombre: ")
    operateur = input("Opérateur: ")
    return [operateur, int(saisie1), int(saisie2)]

def calcul(saisie: list):
    operateur = saisie[0]
    saisie1 = saisie[1]
    saisie2 = saisie[2]
    if operateur == "/" and (saisie2 == 0 or saisie1 == 0):
        print("division par 0 interdite")
    else:
        match operateur:
            case "+":
                resultat = int(saisie1) + int(saisie2)
            case "-":
                resultat = int(saisie1) - int(saisie2)
            case "*":
                resultat = int(saisie1) * int(saisie2)
            case "/":
                resultat = int(saisie1) / int(saisie2)
            case _:
                print("Opérateur inconnu")
        print("Le resultat du calcul est ", resultat) 

calcul(saisie())
