lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
count = 0
list2 = []
for x in lista:
    if x>5 and x<15:
        list2.append(x)

print (list2)

for nev in list2:
    if nev in lista:
        index = lista.index(nev)
        '''
        print (index)
        lista[index: index+1] = []
        '''
        # del(lista[nev-1:20-nev])
        lista.pop(index)        # <--- töröl, index alapján, visszatér a törölt értékkel
        #lista.remove(nev)     # <--- töröl, név szerint

print (lista)
lista.reverse()
print (lista, " - revered")
lista.sort()
print (lista, " - sorted")
