import time
import csv

health = 10
position = "Alap"
bread = 1
def game_events(health, position, bread):
    while health > 0:
        if position == "Alap":
            answer = input("Egy erdőben vagy, már alkonyodik. Találsz egy házat. Bemész az ajtón? \n 1)Igen!  /  2)Nem, inkább kint alszom.\n\n\t")
            if answer == "1":
                print("\nBeléptél az ajtón!")
                position = "Előszoba"
            elif answer == "2":
                print("Gratulálok, kint aludtál és rádtámadt a medve.")
                position = "Alap"
                health -= 2
                print(str(health) + " életed maradt!")
            elif answer == "9":
                savegame(health, position, bread)
        elif position == "Előszoba":
            answer = input("Most az előszobába léptél. Merre szeretnél tovább menni?  \n 1)Jobbra  /  2)Balra  /  3)Vissza a ház elé.\n\n\t")
            if answer == "1":
                print("A jobb oldali ajtó zárva van.")
                position = "Előszoba"
            elif answer == "2":
                print("\nBementél az ajtón!")
                position = "Konyha"
            elif answer == "3":
                print("Vissza mentél a szabadba.")
                position = "Alap"
            elif answer == "9":
                savegame(health, position, bread)
        elif position == "Konyha":
            answer = input("\nEgy konyhába érkeztél, az asztalon egy kenyér van. Mit teszel?\n 1)Megeszem!  /  2)Visszamegyek az aulába.\n\n\t")
            if answer == "1":
                if bread == 1:
                    health += 5
                    print("\nA kenyér 5 életerőt adott.")
                    print(str(health) + " életed van!")
                    bread = 0
                else:
                    print("\nMár megetted a kenyeret!")
            elif answer == "2":
                position = "Előszoba"
            elif answer == "9":
                savegame(health, position, bread)
def savegame (health, position, bread):
    name = input("Adj nevet a mentésednek!")
    file = open(name+".csv", "w")
    file.write("health,"+str(health)+"\n")
    file.write("position,"+position+"\n")
    file.write("bread,"+str(bread)+"\n")
    file.close()
    print("Sikeres mentés!")

while 1 is 1:
    load = input("Üdvözöllek a játékban! \nBe szeretnél tölteni egy korábbi mentést? \n  1)Igen  / 2)Új játékot kezdek.\n(a játék során bármikor elmentheted állásod a 9-as gomb lenyomásával.)")
    if load == "1":
        name = input("Mi a mentésed neve?")
        name_full = name+".csv"
        with open(name_full, "r") as saveFile:
            content = csv.reader(saveFile)
            for x in content:
                if x[0] == "health":
                    health = int(x[1])
                if x[0] == "position":
                    position = str(x[1])
                if x[0] == "bread":
                    bread = int(x[1])
        print ("\n\tMentés sikeresen betöltve!\n")
    game_events(health, position, bread)
    print("Vége a játéknak!")
    retry = input("Újra szeretnéd kezdeni?\n 1)Igen  /  2)Nem\n\t")
    if retry == "1":
        continue
    elif retry == "2":
        print("\n @ValamiEgyszerűVacak made by #DJani - 2015")
        time.sleep(1)
        quit()
