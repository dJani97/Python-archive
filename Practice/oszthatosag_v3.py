
number = int(input("Adj meg egy számot: "))

print ("\n",number,"osztható a következő számokkal:\n")
for x in (range (2, number-1)):
    if number%x is 0:
        print(" ", x)

input("\nÜss entert a kilépéshez...")