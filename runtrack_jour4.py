# Job 1
print("Job 1")

def my_printhello():
    print("Hello_world")
my_printhello()

# Job 2
print("Job 2")

def my_print_name(name = "Noa"):
    print(name)
my_print_name()
my_print_name("Maeva")
my_print_name("Adeline")

# Job 3
print("Job 3")

def add(a = 1 , b = 2):
    print(a + b)
add()
add(4, 8)
add(654, 9854)

# Job 4
print("Job 4")

def GetHello():
    return "Hello la Plateforme"
print(GetHello())

# Job 5
print("Job 5")

def calcul(num1, operator, num2):
    match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                if num2 == 0:
                    return "Il n'est pas possible de diviser par 0."
                else:
                    return num1 / num2
            case _:
                return "Erreur d'opérateur."
print(calcul(1, "+" , 5))
print(calcul(2, "/", 0))
print(calcul(3, "-", 0))

# Job 6
print("Job 6")

def positif_or_negatif(nombre = int(input("Ecrivez un nombre: "))):
    if nombre > 0:
        print("Nombre positif")
    elif nombre < 0:
        print("Nombre négatif")
    else:
        print("Zéro")
positif_or_negatif()

# Job 7
print("Job 7")

def function(langage = input("En quel langage codes-tu: ")):
    match langage:
        case "Javascript":
            print("Tu es un développeur web.")
        case "Python":
            print("Tu es un développeur IA.")
        case "Java":
            print("Tu es un développeur logiciel.")
        case "Reactjs":
            print("Tu es un développeur mobile.")
        case _:
            print("Un jour, je serai le meilleur développeur.")
function()

# Job 8
print("Job 8")

def de_saison(type = input("fruit ou légume: "), saison = input("été ou hiver: ")):
    if type == "fruit" and saison == "hiver":
        print("Les fuits de saison en hiver sont l'orange, la mandarine et le kiwi.")
    elif type == "fruit" and saison == "été":
        print("Les fruits de saison en été sont la poire, la fraise et le cassis.")
    elif type == "légume" and saison == "hiver":
        print("Les légumes de saison en hiver sont la carotte, le topinambour et l'endive.")
    elif type == "légume" and saison == "été":
        print("Les légumes de saison en été sont l'artichaut, l'aubergine et le navet.")
    else:
        print("Je ne connais pas cette information.")
de_saison()

# Job 9
print("Job 9")

def moyenne(note1 = float(input("Première note: ")), note2 = float(input("Deuxième note: ")), note3 = float(input("Troisième note: "))):
    moyenne_etudiant = (note1 + note2 + note3) / 3
    if moyenne_etudiant <= 20 and moyenne_etudiant >= 15:
        print(f"Moyenne: {moyenne_etudiant:.2f}. Très bon élève.")
    elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11:
        print(f"Moyenne: {moyenne_etudiant:.2f}. Bon élève.")
    elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8:
        print(f"Moyenne: {moyenne_etudiant:.2f}. Elève moyen.")
    elif moyenne_etudiant <= 7 and moyenne_etudiant >= 0:
        print(f"Moyenne: {moyenne_etudiant:.2f}. Elève devant faire des efforts.")
moyenne()


# Job 10
print("Job 10")

def even_odd(n):
    if type(n) != int:
        print("Ce nombre n'est pas un entier.")
    else:
        if n % 2 == 0 and n > 0:
            print("Ce nombre est un nombre pair.")
        elif n % 2 != 0 and n > 0:
            print("Ce nombre est un nombre impair.")
        else:
            print("Ce nombre n'est pas positif.")
even_odd(3)
even_odd(4)
even_odd(-2)
even_odd(2.6)

# Job 11
print("Job 11")

def time_to_text(n):
    x = n // 60
    y = n % 60
    print(f"{x} heures et {y} minutes")
time_to_text(78)
time_to_text(6)
time_to_text(120)

# Pour aller plus loin
print("Pour aller plus loin")

def reverse_string(x):
    return x[::-1]
print(reverse_string("nikana"))
