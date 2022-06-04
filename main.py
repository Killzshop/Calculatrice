# Projet VRAI calculatrice

# Variables

operation = input("Quel type de calcule veux tu faire (+, -, /, *) ?")
nombre1 = input("Quel es ton premier chiffre ?")
nombre2 = input("Quel es ton second chiffre ?")

nombre1 = int(nombre1)
nombre2 = int(nombre2)


if operation == "+":
    print(f"{nombre1} + {nombre2} = {nombre1 + nombre2}")
elif operation == "-":
    print(f"{nombre1} - {nombre2} = {nombre1 - nombre2}")
elif operation == "/":
    print(f"{nombre1} / {nombre2} = {nombre1 / nombre2}")
elif operation == "*":
    print(f"{nombre1} * {nombre2} = {nombre1 * nombre2}")
elif operation == "//":
    print(f"{nombre1} // {nombre2} = {nombre1 // nombre2}")
else:
    print("L'opération n'est pas valide.")