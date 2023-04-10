import random
import keyboard

file = open("passwords.txt", "w")


while True:
    n1  = [
        3,
        4,
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9)
    ]
    n2  = [
        1,
        random.randint(0,9),
        random.randint(0,9),
        random.randint(0,9)
    ]
    x = sum(n1)
    d = x*7
    y = sum(n2)
    z  = d + y
    w = z % 10
    k = x + w
    f = k + z
    f = f % 10
    file.write(str(n1[0]))
    file.write(str(n2[0]))
    file.write(str(n1[1]))
    file.write(str(n2[1]))
    file.write(str(n1[2]))
    file.write(str(n2[2]))
    file.write(str(n1[3]))
    file.write(str(n2[3]))
    file.write(str(n1[4]))
    file.write(str(w))
    file.write(str(f) + "\n")