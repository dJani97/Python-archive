import time

a = 0	#előző szám
b = 1	#jelenlegi szám
c = 0	#számláló
j = "."	#jelölő

maximum = int(input("Meddig irjam ki a szamokat?"))

while c < maximum:
    a, b, c = b, a+b, c+1
    print (str(c)+". pár:  \t" + str(b) + " / " + str(a) + " =  " + str(b/a))
