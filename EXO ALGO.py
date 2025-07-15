# Demande d'informations à l'utilisateur
prenom = input("Entrez votre prénom : ")
age = int(input("Entrez votre âge : "))
ville = input("Entrez votre ville : ")
metier = input("Entrez votre métier : ")

# Approximation des jours vécus
jours_vecus = age * 365

# Affichage formaté
print("\n== PROFIL UTILISATEUR ==")
print(f"Prénom : {prenom}")
print(f"Âge : {age} ans ({jours_vecus} jours vécus environ)")
print(f"Ville : {ville}")
print(f"Métier : {metier}")
# Définition des variables
nom_produit = input("Nom du produit : ")
prix = float(input("Prix initial (€) : "))
stock = int(input("Quantité en stock : "))
remise = float(input("Remise (%) : "))

# Calcul du prix final
prix_final = prix * (1 - remise / 100)

# Affichage
print("\nFICHE PRODUIT")
print("-" * 30)
print(f"Produit : {nom_produit}")
print(f"Prix initial : {prix:.2f} €")
print(f"Remise : {remise}%")
print(f"Prix final : {prix_final:.2f} €")
print(f"Stock disponible : {stock} unités")
print(f"Économie : {prix - prix_final:.2f} €")
# Entrée utilisateur
heures = int(input("Nombre d'heures : "))
minutes = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))

# Conversion
total_secondes = heures * 3600 + minutes * 60 + secondes

# Résultat
print(f"\nDurée convertie : {heures}h {minutes}min {secondes}s = {total_secondes} secondes")
# Demander la note
note_20 = float(input("Note sur 20 : "))

# Conversion
note_100 = (note_20 / 20) * 100

# Affichage
print(f"Note sur 100 : {note_100:.1f}")