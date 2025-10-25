compteur=1

while compteur <= 10:
     
     print(f"Compteur: {compteur}")
     compteur+=1

print("Fin de boucle")


while True:
     letters=input("Choisissez un mot, si vous voulez arreter dites stop:")
     if letters=="stop":
          print("Votre programme est terminé, merci")
          break