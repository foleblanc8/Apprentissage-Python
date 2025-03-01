def convertir_km_en_miles(km):
    return km * 0.621371

def convertir_kg_en_lbs(kg):
    return kg * 2.20462

def convertir_celsius_en_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Bienvenue dans le convertisseur d'unités !")
print("1: Kilomètres → Miles")
print("2: Kilogrammes → Livres")
print("3: Celsius → Fahrenheit")

choix = input("Choisissez une conversion (1, 2, ou 3) : ")

if choix == "1":
    km = float(input("Entrez la distance en kilomètres : "))
    print(f"{km} km = {convertir_km_en_miles(km):.2f} miles")

elif choix == "2":
    kg = float(input("Entrez le poids en kilogrammes : "))
    print(f"{kg} kg = {convertir_kg_en_lbs(kg):.2f} lbs")

elif choix == "3":
    celsius = float(input("Entrez la température en Celsius : "))
    print(f"{celsius}°C = {convertir_celsius_en_fahrenheit(celsius):.2f}°F")

else:
    print("Choix invalide. Veuillez redémarrer le programme.")

while True:
    print("\nConvertisseur d’unités (tapez 'q' pour quitter)")
    print("1: Kilomètres → Miles")
    print("2: Kilogrammes → Livres")
    print("3: Celsius → Fahrenheit")

    choix = input("Choisissez une conversion (1, 2, ou 3) : ")

    if choix == "q":
        print("Merci d’avoir utilisé le convertisseur !")
        break  # Sort de la boucle

    elif choix == "1":
        km = float(input("Entrez la distance en kilomètres : "))
        print(f"{km} km = {convertir_km_en_miles(km):.2f} miles")

    elif choix == "2":
        kg = float(input("Entrez le poids en kilogrammes : "))
        print(f"{kg} kg = {convertir_kg_en_lbs(kg):.2f} lbs")

    elif choix == "3":
        celsius = float(input("Entrez la température en Celsius : "))
        print(f"{celsius}°C = {convertir_celsius_en_fahrenheit(celsius):.2f}°F")

    else:
        print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
