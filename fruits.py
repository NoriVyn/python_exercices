
fruits=[]

try:
    nombre_fruits=int(input("Combien des fruits aimeriez vous ajouter a votre liste de fruits préférés?"))

    if nombre_fruits <= 0:
     print("Désolé mais votre nombre doit etre superieur a 0.")
    else:
     print(f"Ok, merci beaucoup, on va pouvoir ajouter {nombre_fruits} fruits a votre liste de fruits préférés")

     for i in range(nombre_fruits):
         fruits_user=input(f"Donnez moi {nombre_fruits} fruits que vous aimez de plus/préférés. comme par exemple n°{i+1}:")
         fruits.append(fruits_user)

    print(fruits)
except ValueError:
   print("Erreur:Entre un nombre valide s'il vous plait")

def fruits_user_choix(liste):
    print("\nVoici les fruits que vous aimez de plus:")
    for fruits_user  in liste:
        print(f"{fruits_user}")

if fruits:
    fruits_user_choix(fruits)