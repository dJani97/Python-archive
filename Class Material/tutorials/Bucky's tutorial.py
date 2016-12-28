"""
Alap matematikai műveletek, matematikai operátorok
"""
3 + 5
5 - 2
3 * 20
(3 + 2) * 5 == 25 # a zárójelek és a műveleti sorrend ugyan az, mint a matematikában
18 / 4 == 4.5 # az osztás eredménye mindig float azaz tört szám!
18 // 4 == 4  # lefelé kerekít, int azaz egész számmal tér vissza
18%2 == 2 # Kiírja az egész osztás maradékát, neve: modulo operátor
5%2 == 1
5 ** 3 == 125 # négyzetre emelés


"""
Változók (alapok)
"""
tonhal = 5 # a "tonhal" nevű változónak értékül adtuk az 5-öt
20 + tonhal == 25

bacon = 18
bacon / tonhal == 3.6


"""
STRING változótípus, alapok
"""
"tonhal" # string azaz szöveg változó típus, jele: " " vagy ' '
'Azt mondta, hogy "A tonhalnak jó íze van" ' # néha jól jön ez a két féle jelölés
"I'm John"
"\"" # Egy szövegben a \ (backslash) használata kihagyja a következő karaktert
" \"Finom volt a leves\", mondta Tibi"

print() # Kiír valamit a képernyőre
print("Hello mindenkinek!")
print('C:\Felhasználók\Jancsika\Asztal\napos_képek') # a sorban található \n karakter kombináció entert jelent, új sorba ugrott
"\n" # Enter, új sorba ugrik
print(r'C:\Felhasználók\Jancsika\Asztal\napos_képek') # r-t téve a teljes string elé: raw string, nem fogja figyelembe venni a benne lévő parancsokat, az előbb leírt probléma kiküszöbölhető
vezetéknév = "Kocsis"
keresztnév = "József"
keresztnév2 = "McLovin"
print (vezetéknév + " " + keresztnév) # eredményként megjelenik akét név összefűzve, közéjök érdemes szóközt beszúrni  egy üres " " string-el
print (vezetéknév + " " + keresztnév + " " + keresztnév2)
print (vezetéknév * 5) # stringeket szorozhatunk is

felhasználó = "Petőfi Sándor"
print (felhasználó[0]) # [ ] közé írt számmal férhetünk hozzá egy biznyos karakterhez az INDEXE alapján. 0-val kezdünk!
print (felhasználó[-1]) # -1 mindig az utolsó karakter, -2 az utolsó előtti, stb...
print (felhasználó[2:9]) # szeletelés, "SLICING" [kezdőpont : végpont]
print (felhasználó[:9]) # ha szeletelés során a kezdő vagy végpontot kihagyjuk, akkor automatikusan az elejétől/végéig fog menni
print (felhasználó[:]) # emiatt ha mindkettőt kihagyjuk, az elejétől kezd és a végéig kiírja

len(felhasználó) # megadja a string (vagy lista!) hosszúságát


"""
LIST változótípus, azaz lista vagy tömb
"""
játékosok = [29, 58, 66, 71, 87] # lista létrehozása. Több elemet tárol, jele mindig [ ]
példa_lista = ["Alma", 69, "Befőttesgumi", [1, 2, 3, 4], 3.14] # Egy lista elemei akár lehetnek akár kölönböző típusúak is.
másik_példa_lista = [példa_lista, játékosok] # egy listába beletehetjük akár előzőleg létrehozott változók értékeit is
játékosok[2] = 11 # egy lista bizonyos eleméhez hozzárendelhetünk egy másik értéket, kicseréljük azt

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1 + lista2 == [1, 2, 3, 4, 5, 6] # listák összeadása is lehetséges. Az eredet listák NEM VÁLTOZNAK
lista1.append(120) # ezzel az első listát kibővítettük a zárójelben megadott értékkel, hozzáadtuka zt. A lista MEGVÁLTOZOTT
print ( lista1[:2] ) # a SLICING azaz szeletelés listákon is alkalmazható
lista1[:2] = [0, 0] # a SLICING használható elemek cseréjére, hozzárendelésre is
print ( lista1 )
lista1[:2] = [] # ha üres listával teszünk egyenlővé egy szeletet, az törlődik
print ( lista1 )














































