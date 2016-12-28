import random

tip = set([23, 67, 53, 81, 33])

n = 1
while True:
    er, t = set(), 0
    while len(er) < 5:
        er.add(random.randrange(10, 91))

    for x in er:
        if x in tip: t+=1

    if t == 4:
        print(str(n)+".",t)
    elif t == 5:
        print(str(n)+".",t, "TELITALÁLAT!")

    n+=1

print ("\ndone")
