import random, os
while True:
    talalat = 0
    n = 1
    list_a = []
    print ("Uss be 5 darab szamot 1 es 90 kozott, mindegyik utan uss entert!")
    while n<6:
        x = int(input(str(n)+". szam: "))
        list_a.append(x)
        n+=1
    print ("Jatekos szamai:", list_a)
    list_b = random.randrange(1, 91), random.randrange(1, 91), random.randrange(1, 91), random.randrange(1, 91), random.randrange(1, 91)
    print ("Sorsolas eredmenye:", list_b)

    for x in list_a:
        if x in list_b:
            talalat += 1

    print ("Talalatok szama: ", talalat)
    input("\nNyomj le egy gombot a folytatashoz...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nUJ JATEK!\n")
