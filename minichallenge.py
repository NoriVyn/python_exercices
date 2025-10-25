
"""
Structure générale (sans code pour l’instant)

Importer random x
Générer un nombre secret avec random.randint(1, 20) x
Initialiser un compteur d’essais à 0
Démarrer une boucle while :
Demander une réponse à l’utilisateur
Incrémenter le compteur

Vérifier :
Si c’est le bon nombre → victoire
Si c’est trop grand → message “plus petit”
Si c’est trop petit → message “plus grand”
"""

import random

nombre_aleatoire=random.randint(1,20)

compteur=0

while True:
    try:
        devinette=int(input("Devinez le nombre de 1 à 20: "))
        compteur+=1
        if devinette == nombre_aleatoire:
             print(f"Bravo! Vous avez trouvé le nombre en {compteur} essais")
             break
        elif devinette < nombre_aleatoire:
            print("Le nombre choisi est trop petit! Vous êtes chaud ! Continuez....")
        else:
            print("Le nombre choisi est trop grand! Vous êtes chaud ! Continuez....")
    except ValueError:
        print("Erreur:Entrez un nombre valide s'il vous plait")


