
list = range(10000, 11100)


for n in list:
    print(
    )
    print(n, "oszthatósága következik:")
    for m in range (2, 101):

        if n%m is 0:
            print("Osztható", m, "-es számmal")