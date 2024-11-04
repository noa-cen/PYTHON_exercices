# Job 1
print("Job 1")

def draw_rectangle(width, height):
    if height > 2:
        print("|", "-" * width, "|")
        height = height - 2
        n = 0
        while n < height:
            print("|", " " * width, "|")
            n += 1
        print("|", "-" * width, "|")
    elif height == 2:
        print("|", "-" * width, "|")
        print("|", "-" * width, "|")
    else:
        print("|", "-" * width, "|")
draw_rectangle(5, 7)
draw_rectangle(7, 2)
draw_rectangle(3, 1)

# Job 2
print("Job 2")

def job2(height):
    print(" "* height, "/\\")
    n = 0
    m = height - 1
    while n < height -2:
        print(" "* m, "/", " "* n * 2, "\\")
        m -= 1
        n += 1
    print(" "* m, "/", "_"* n * 2, "\\")
job2(5)
job2(7)

# Job 3
print("Job 3")

def job3(n):
    print("+", "-" * (n + 1), "+")
    x = 0
    y = n
    while x < n + 1:
        print("|", "#"*(n-x), "", "#"*(n-y), "|")
        x += 1
        y -= 1
    print("+", "-" * (n + 1), "+")
job3(10)

# Job 4
print("Job 4")

def job4(message, n):
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digit = string.digits
    punctuation = string.punctuation
    message = list(message)
    new_message = []
    for letter in message:
        if letter == " ":
            new_message.append(" ")
        elif letter in uppercase:
            x = uppercase.index(letter)
            x = x + n
            new_message.append(uppercase[x])
        elif letter in lowercase:
            x = lowercase.index(letter)
            x = x + n
            new_message.append(lowercase[x])
        elif letter in digit:
            x = digit.index(letter)
            x = x + n
            new_message.append(digit[x])
        elif letter in punctuation:
            x = punctuation.index(letter)
            new_message.append(punctuation[x])
    print("".join(new_message))
job4("Ceci est un test.", 3)
job4("Ca fonctionne !", 6)

# Job 5
print("Job 5")

def job5(marches, cm):
    result = 5 * 2 * 7 * marches * cm / 100
    print(f"Pour {marches} marches de {cm} centimètres, le gardien parcourt {result:.2f}m par semaine.")
job5(56, 25)

# Job 6
print("Job 6")

def job6(*note):
    note = list(note)
    note_arrondi = []
    for n in note:
        if n < 0 or n > 100:
            print("Erreur, la note doit être comprise entre 0 et 100.")
        elif n >= 40 and n < 100:
            for x in range(3):
                if (n + x) % 5 == 0:
                    n = n + x
            print(f"Examen réussi avec une note de {n} sur 100.")
            note_arrondi.append(n)
        else:
            print(f"Echec à l'examen avec une note de {n} sur 100.")
            note_arrondi.append(n)
    print(note_arrondi)
job6(34, 40, 82, 83)

# Job 8
print("Job 8")