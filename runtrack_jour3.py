# Job 1
print("Job 1")
valeur1 = int(input("Ecrivez un nombre: "))
valeur2 = int(input("Ecrivez un nombre: "))
if valeur1 == valeur2:
    print("Valeur 1 est égale à valeur 2.")
else:
    print("Les deux valeurs ne sont pas égales.")

# Job 2
print("Job 2")
age = input("Quel est votre âge ? ")
if int(age) >= 18:
    print("Tu peux voter.")
else:
    print("Tu ne peux pas voter.")

# Job 3
print("Job 3")
for x in range(101):
    if x == 26 or x == 37 or x == 88:
        pass
    else:
        print(x)

# Job 4
print("Job 4")
for x in range(1, 101):
    if x % 3 == 0 and x % 5 != 0:
        print("Fizz")
    elif x % 5 == 0 and x % 3 != 0:
        print("Buzz")
    elif x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else :
        print(x)

# Job 5
print("Job 5")
prime_numbers = []
for n in range(2, 1001):
    is_prime = True
    i = 0
    while i < len(prime_numbers) - 1 and is_prime == True:
        if n % prime_numbers[i] == 0:
            is_prime = False
        i += 1
    if is_prime:
        prime_numbers.append(n)
for y in prime_numbers:
    print(y)

# Correction nombres premiers
def prime_numbers():
    i = 2
    is_prime = True
    while i < 1001:
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime == True:
                print(i)
        i += 1
        is_prime = True
prime_numbers()

# Job 6
print("Job 6")
N = int(input("Ecrivez un nombre: "))
if N % 2 == 0:
    print(f" Le nombre {N} est pair.")
else:
    print(f"Le nombre {N} est impair.")

# Job 7
print("Job 7")
alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
x = 1
while x < len(alphabet) - 1:
    letter = alphabet[0:x]
    print(letter)
    x += 2

# Job 8
print("Job 8")
def is_triangle():
    a = int(input("Déterminez une longeur a: "))
    b = int(input("Déterminez une longeur b: "))
    c = int(input("Déterminez une longeur c: "))

    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            if a == b or a == c or b == c:
                print("Ce triangle est un triangle rectangle et isocèle.")
            else:
                print("Ce triangle est un triangle rectangle.")
    elif a == b == c:
        print("Ce triangle est un triangle équilatéral.")
    elif a == b or a == c or b == c:
        print("Ce triangle est un triangle isocèle.")
    elif a < b + c or b < a + c or c < a + b:
        print("Ce triangle est un triangle quelconque.")
    else:
        print("Erreur, ces valeurs ne peuvent pas construire un triangle.")
is_triangle()
    

