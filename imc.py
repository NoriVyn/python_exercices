poids=float(input("Quelle est votre poids? (kg)"))
taille=float(input("Quelle est votre taille? (m)"))


if taille < 0:
    print("Votre taille n'est pas correcte, elle doit etre superieur a 0")
else:
    imc= poids/(taille**2)

if imc < 18.5:
    print("Insuffisance pondérale")
elif imc < 25:
    print("poids normal")
elif imc < 30:
    print ("Surpoids")
else:
    print("Obésité")

print(f"Vous étes donc en {imc:.2f}")