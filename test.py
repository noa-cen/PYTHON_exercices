def job6(*note):
    i = 0
    while i < note[i]:
        if note[i] > 40/100:
            pass_exam = True
        i += 1
        x = 0
        while x < 3:
            if (note[i] + x) % 5 == 0:
                note[i] = note[i] + x
            x += 1
        else:
            pass_exam = False
job6(32, 40, 45)