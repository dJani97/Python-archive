
import math


while True:
    a = input("Add meg xx egyutthatojat! ")
    b = input("Add meg x egyutthatojat! ")
    c = input("Add meg c-t ")
    a, b, c = float(a), float(b), float(c)

    gyok_alatt = b**2 -(4*a*c)

    if gyok_alatt > 0 and a != 0:
        x1 = (-(b) + math.sqrt(gyok_alatt)) / 2*a
        x2 = (-(b) - math.sqrt(gyok_alatt)) / 2*a
        print(x1)
        print(x2)
    elif gyok_alatt == 0 and a != 0:
        x = -b / 2*a
        print (x)
    else:
        print("\nNincs valos gyok")
    
    kilep = input("\nNyomj 1-et az ujrakezdeshez, 2-t a kilepeshez! ")
    if kilep is "1":
        pass
    print ("\n")
    if kilep is "2":
        break

exit()
