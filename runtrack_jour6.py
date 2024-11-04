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


# Job 5
print("Job 5")

def job5(marches, cm):
    result = 5 * 2 * 7 * marches * cm / 100
    print(f"Pour {marches} marches de {cm} centimètres, le gardien parcourt {result:.2f}m par semaine.")
job5(56, 25)

# Job 6
print("Job 6")




# Job 8
print("Job 8")