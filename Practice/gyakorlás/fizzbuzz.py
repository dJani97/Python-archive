#For loopal megvalósítva

number = int(input("Adj meg egy számot: "))

list = range (1, number+1)

for szam in list:
    if szam%3 is 0:
        print ("fizz")
    elif szam%5 is 0:
        print ("buzz")
    elif szam%3 is 0 and szam%5 is 0:
       print ("fizzbuzz")
    else:
        print (szam)

input("Nyomj entert a kilépéshez...")
exit()
