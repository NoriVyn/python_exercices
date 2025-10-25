"""
Challenge : “Mini-liste secrète”
Objectif :

L’utilisateur va choisir combien de nombres il veut ajouter à une liste secrète.
Ensuite, il entre chaque nombre un par un.
Le programme génère un nombre aléatoire entre 1 et 20.
Pour chaque nombre de la liste, le programme lui dit si le nombre de la liste est trop grand, trop petit, ou correct par rapport au nombre aléatoire.
À la fin, il affiche la liste complète avec les indications.
"""
import random
compteur=0
nombres_aleatoires=random.randint(1,20)
print(nombres_aleatoires)
liste_user=[]

while True:
    try:
        nombres=int(input("Combien de nombres voulez vous ajouter a une liste secrete?"))
        if nombres <= 0:
            print("Le nombre doit etre superieur à 0")
        else:
            break
    except ValueError:
        print("Erreur:  Entrez un nombre entier valide, s'il vous plait.")

for i in range(nombres):
        while True:
            try:
                nombres_user=int(input(f"Donnez moi les {nombres} que vous avez choisi n°{i+1}:"))
                liste_user.append(nombres_user)
                break
            except ValueError:
                print("Erreur: Entrez un nombre entier valide")
        
for nombres in liste_user:
        if nombres < nombres_aleatoires:
            print(f"{nombres} --> Trop petit")
        elif nombres > nombres_aleatoires:
            print(f"{nombres} --> Trop grand")
        else:
            print(f"{nombres} --> Correct! Bravo!")
