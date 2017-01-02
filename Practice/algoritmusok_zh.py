import random
import time

length, lim = 20, 100

a1 = [random.randrange(lim) for _ in range(length+1)]
a2 = [random.randrange(lim) for _ in range(length+1)]
a1.sort()
a2.sort()

b = []
i1, i2 = 0, 0

print ("a1:", a1, "\na2:", a2)

while (i2 < length) and (i1 < length):
    if (a1[i1] < a2[i2]) and i1<length:
        b.append(a1[i1])
        if i1 < length:
            i1 += 1
    else:
        b.append(a2[i2])
        if i2 < length:
            i2 += 1
        if i1==length:
            while i2<=length:
                b.append(a2[i2])
        else:
            while i1<=length:
                b.append(a1[i1])

print ("a1:", a1, "\na2:", a2, "\nb:", b, len(b))
