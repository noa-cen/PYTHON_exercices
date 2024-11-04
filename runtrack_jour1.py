# Job 3
print("Job3")
print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10%3)

# Job 4
print("Job 4")
import string
alphabet = string.ascii_lowercase
print(alphabet)

# Job 5
print("Job 5")
reverse_alphabet = alphabet[::-1]
print(reverse_alphabet)

# Job 6
print("Job 6")
ma_string = "Je suis une string"
print(ma_string)

# Job 7
print("Job 7")
num1 = 40
num2 = 2
print(num1 + num2)

# Job 8
print("Job 8")
num1 = 3
num2 = 14
print(num1 * num2)

# Job 9
print("Job 9")
inventaire = {"nom" : "téléphone", "prix_unitaire" : 349.99, "quantite_en_stock" : 32}
print(f"Nom: {inventaire['nom']}")
print(f"Prix unitaire: {inventaire["prix_unitaire"]}€")
print(f"Quantité en stock: {inventaire['quantite_en_stock']}")
ajout_produits = input("Ajoutez des produits au stock: ")
inventaire["quantite_en_stock"] += int(ajout_produits)
print(f"Nom: {inventaire['nom']}")
print(f"Prix unitaire: {inventaire["prix_unitaire"]}€")
print(f"Quantité en stock: {inventaire['quantite_en_stock']}")
quantite_souhaitee = input("Combien souhaitez-vous en acheter ?")
print(f"{int(quantite_souhaitee)} {inventaire['nom']} dans votre panier")
inventaire["quantite_en_stock"] = inventaire["quantite_en_stock"] - int(quantite_souhaitee)
print(f"Nom: {inventaire['nom']}")
print(f"Prix unitaire: {inventaire["prix_unitaire"]}€")
print(f"Quantité en stock: {inventaire['quantite_en_stock']}")
inventaire["prix_unitaire"] = inventaire["prix_unitaire"] * 1.1
print(f"Nom: {inventaire['nom']}")
print(f"Prix unitaire: {inventaire["prix_unitaire"]:.2f}€")
print(f"Quantité en stock: {inventaire['quantite_en_stock']}")

# Job 10
print("Job 10")
montant_investi = input("Combien souhaitez-vous investir ? (en€)")
taux_rendement_annuel = input("Quel est le taux de rendement annuel ? (en %)")
gain_annuel = (float(taux_rendement_annuel) * float(montant_investi))/100
print(f"Si vous investissez {montant_investi}€, avec un taux de rendement annuel de {taux_rendement_annuel}%, vous gagnerez {gain_annuel:.2f}€ en un an.")
montant_investi = float(montant_investi) + 5000
taux_rendement_annuel = float(taux_rendement_annuel) * 1.02
gain_annuel = (float(taux_rendement_annuel) * float(montant_investi))/100
print(f"L'investisseur augmente son capital de 5000€, son investissement est donc à présent de {montant_investi:.2f}€, avec un taux de rendement annuel actualisé de {taux_rendement_annuel:.2f}%, il gagnera alors {gain_annuel:.2f}€ en un an.")
montant_total = float(montant_investi) + float(gain_annuel)
montant_total = float(montant_total) - (float(montant_total)*10/100)
taux_rendement_annuel = float(taux_rendement_annuel) * 0.99
gain_annuel = (float(taux_rendement_annuel) * float(montant_investi))/100
print(f"L'investisseur décide de retirer 10% du montant total. Son investissement est donc à présent de {montant_total:.2f}€, avec un taux de rendement annuel actualisé de {taux_rendement_annuel:.2f}%, il gagnera alors {gain_annuel:.2f}€ en un an.")

# Pour aller plus loin
print("Pour aller plus loin :")
phrase = input("Ecrivez une phrase: ")
if "e" in phrase : 
    print(True)
else :
    print(False)

# link du QCM : 
# https://docs.google.com/forms/d/e/1FAIpQLSeIRtK65oU49SdJ_7K2UoPKBQ3MUrvD6L1x6KE3YAjmurtF0A/viewform?usp=pp_url&entry.1910084372=Un+conteneur+pour+stocker+une+valeur&entry.1719496140=print(my_str)&entry.1552474905=x+%3D+10&entry.858847196=variable_1&entry.1226125276=17&entry.149303964=Hello+World&entry.1240915853=tva+%3D+input(%22Saisissez+le+taux+de+TVA+:%22)&entry.893000223=nb_voitures+%3D+nb_voitures+%2B+2&entry.893000223=nb_voitures+%2B%3D+2&entry.453631737=total+*+1.1

