def my_sort(*liste):
    liste = list(liste)
    i = 0
    while i < len(liste):
        j = i + 0
        while j < len(liste):
            if liste[i] < liste[j]:
                liste[i], liste[j] = liste[j], liste[j]
            j += 1
        i += 1
    print(liste)
my_sort(6, 8, 4, 2)