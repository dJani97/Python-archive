

accounts = []

with open ("bank_data.txt", "r") as file:
    for line in file:
        line = line.strip().split()
        accounts.append([line[0], int(line[1])])


def write_data():
    with open ("bank_data.txt", "w") as file:
        for acc in accounts:
            file.write(acc[0]+" "+str(acc[1])+"\n")

def print_all():
    for acc in accounts:
                print (acc[0]+":", acc[1])

def bank_loop():
    while True:
        action = input("\nVálassz menüpontot:\n1-es gomb Adatok lekérése\n2-es gomb Pénzbefizetés\n3-as gomb Pénzkivétel\n4-es gomb Átutalás számlák közt\n9-es gomb Kilépés\n")
        if action == "1":
            print_all()


        if action == "2":
            szamla = input("Hová szeretne befizetni? " + "".join("\n"+x[0] for x in accounts) + "\n")
            mennyiseg = input("Mennyit fizet be?\n")
            for acc in accounts:
                if acc[0] == szamla:
                    acc[1] += int(mennyiseg)
                print (acc[0]+":", acc[1])


        if action == "3":
            szamla = input("Melyik számlát csökkentené? " + "".join("\n"+x[0] for x in accounts) + "\n")
            mennyiseg = input("Mennyivel?\n")
            for acc in accounts:
                if acc[0] == szamla:
                    acc[1] -= int(mennyiseg)
                print (acc[0]+":", acc[1])
            
        
        if action == "4":
            innen = input("Honnan szeretne utalni? " + "".join("\n"+x[0] for x in accounts) + "\n")
            ide = input("Melyik számlára szeretne utalni?\n")
            mennyiseg = int(input("Mennyi pénzt?"))
            for acc in accounts:
                if (acc[0] == innen) and acc[1] >= mennyiseg:
                    acc[1] -= int(mennyiseg)
                    for acc in accounts:
                        if acc[0] == ide:
                            acc[1] += int(mennyiseg)
                elif (acc[0] == innen) and acc[1] < mennyiseg:
                    print ("A számlán nem áll rendelkezésre elég pénz!\n")

            
                    
            print_all()


        
        if action == "9":
            quit()
        write_data()
            
            
        
    
print_all()

bank_loop()
