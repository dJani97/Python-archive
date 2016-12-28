import threading

while True:
    mx = int(input("Max value:\n"))

    l = []
    for number in range(2, mx):
        local = 0
        for x in range (1, number+1):
            if number%x is 0:
                local += 1
        if local == 2:
            l.append(number)
           

    print("Count of primes:", len(l), "\n% of primes: "+str((len(l)/mx)*100)+"%")
    if len(l)< 200:
        print("Primes:", str(l)[1:-1])
    print ("_______________________________")
    print (threading.active_count())
    print ("_______________________________")

    input("\nPress enter")
