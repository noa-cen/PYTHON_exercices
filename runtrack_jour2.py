# Job 1
print("Job 1")

for x in range(21):
    print(x)

# Job 2
print("Job 2")

for x in range(0, 21, 2):
    print(x)

# Job 3
print("Job 3")

for x in range (1, 21):
    print(x*x)

# Job 4
print("Job 4")

N = int(input("Entrez un entier supérieur à 0: "))
if N > 0 :
    for x in range(1, N+1):
        print(f"Table de multiplication de {x} :")
        for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            resultat = x * y
            print(f"{x} x {y} = {resultat}")
else:
    print("Erreur, N doit être un nombre entier supérieur à 0.")

# Job 5
print("Job 5")

N = 1
while N < 13 :
    print(N)
    N += 1

# Job 6 
print("Job 6")

N = int(input("Renseigner un nombre entier : "))
x = 1
while x <= N:
    resultat = x * 7
    print(f"{x} x 7 = {resultat}")
    x += 1

# Job 7
print("Job 7")

x = 1
while x < 13:
    resultat = 3 * x - 2
    print(f"Tour {x} : {resultat}")
    x += 1
print()
print("[Execution complete with exit code 0]")

# Job 8
print("Job 8")

N = 0
for x in range(12):
    N += 2
    print(f"Tour {x + 1}: {N}")
    x += 1

# Job 9
print("Job 9")

pair = []
impair = []
for x in range(1, 31):
    if x % 2 == 0:
        pair.append(x)
    else:
        impair.append(x)
print(f"Nombres pairs: {pair}")
print(f"Nombres impairs: {impair}")
