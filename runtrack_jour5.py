# Job 1
print("Job 1")

def job1():
    fruits = ["pomme", "cerise", "orange"]
    return fruits
print(job1())

# Job 2
print("Job 2")

def job2():
    fruits = ["pomme", "cerise", "orange"]
    print(fruits[1])
job2()

# Job 3
print("Job 3")

def job3():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("melon")
    return fruits
print(job3())

# Job 4
print("Job 4")

def job4():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "mangue")
    return fruits
print(job4())

# Job 5
print("Job 5")

def job5():
    L = [1, 2, 3, 4, 5]
    print(L)
    print(L[1])
    L[3] = L[2] + L[4]
    print(L)
    print(L[4])
job5()

# Job 6
print("Job 6")

L = input("Entrez une liste de nombres entre virgule: ")
L = L.split(",")
def job6(L):
    print(L)
    L[0], L[-1] = L[-1], L[0]
    print(L)
job6(L)

# Job 7
print("Job 7")

def job7():
    L = [8, 24, 48, 2, 16]
    l = []
    for i in L:
        if i % 3 == 0:
            l.append(i)
        else:
            pass
    print(f"Il y a {len(l)} multiples de 3 dans cette liste.")
job7()

# Correction du QCM:
def job7():
    L = [8, 24, 48, 2, 16]
    count = len([x for x in L if x % 3 == 0])
    print(count)
job7()

# Job 8
print("Job 8")

def job8():
    L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
    l = []
    for i in L:
        if i % 2 == 0:
            l.append(i)
    x = sum(l)
    print(x)
job8()

# Job 9
print("Job 9")

def job9():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    max_value = max(L)
    min_value = min(L)
    print(f"La valeur max est : {max_value}.")
    print(f"La valeur min est : {min_value}.")
job9()

# Job 10
print("Job 10")

def job10():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    x = 1
    for i in L:
        if i >= 25 and i <= 90:
            x *= i
    print(x)
job10()

# Job 11
print("Job 11")

def job11():
    L = [7, 11, 42, 39, 2]
    L = [x+1 for x in L]
    print(L)
job11()

# Job 12
print("Job 12")
def job12(*L):
    L = list(L)
    for i in range(len(L)):
        j = i + 1
        for j in range(len(L)):
            if L[i] < L[j]:
                L[i], L[j] = L[j], L[i]
    print(L)
job12(6, 8, 4, 2)

# Job 13
print("Job 13")

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
def job13():
    i = 0
    while i < len(L) - 1:
        j = i + 1
        while j < len(L):
            if L[i] == L[j]:
                L.pop(j)
            j += 1
        i += 1
    print(L)
job13()

# Correction du QCM:
def job13():
    L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    L = [x for i, x in enumerate(L) if x not in L[:i]]
    print(L)
job13()

# Job 14
print("Job 14")

def job14(n, s):
    return [word for word in s.split() if len(word) > n]
print(job14(3, "Bonjour je m'appelle Noa"))

# Job 15
print("Job 15")

def job15():
    L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    for i in range(len(L)): 
        L[i] = int(L[i] + 0.5)
    i = 0
    while i < len(L):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
            j += 1
        i += 1
    print(L)
job15()