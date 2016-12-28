#While loop változat

number = int(input("Adj meg egy számot: "))
szam = 1

while szam <= number:
    if szam%3 is 0 and szam%5 is 0:
       print ("fizzbuzz")
    elif szam%3 is 0:
        print ("fizz")
    elif szam%5 is 0:
        print ("buzz")
    else:
        print (szam)

    szam += 1

input("Nyomj entert a kilépéshez...")
exit()
