
szamok = list(range(-5, 6))
for szam in szamok:
    print (szam, "pozitív" if szam>=0 else "negatív")

print ("\n_____________________________\n")

tomb = [1, 3, 34, 43, 64, 84, 3, 67, 0, "asd"]
print( 55 in tomb )
print( tomb.index(3) )
tomb.remove("asd")
print( sum(tomb) )
print( min(tomb) )
print( max(tomb) )

print ("\n_____________________________\n")

szoveg = "most begepelek valami tok veletlenszeru karaktersorozatot fjsalfsaldfhsadfgshafklsaf djshflsaf slkjfhks djf skljdkfl"
import string
print( string.ascii_lowercase)

for betu in string.ascii_lowercase:
    print ("{} száma:{}".format(betu, szoveg.count(betu)))

print( "\n", szoveg.find("g"), sep="")
print( szoveg.rfind("g"))

print ("\n_____________________________\n")

print( list(szoveg) )
print( szoveg.split(" ") )
print( "".join(szoveg.split(" ")))

print ("\n_____________________________\n")
"""
with open ("fajlnev.txt", "a") as fájl:
a=append, r=read, w=újraír elejétől

fájl.read()
fájl.readline()
fájl.readlines()




https://youtu.be/qZRpxMHX2Qo?t=25m1s

"""




#__________________________________________________________________________________________________________________________________________
"""
7. VIDEÓ:
"""

# string.replace("mit", "mire", hányszor)
string = "asdasdasdasdasdasd dsa"
print( string.replace("asd", "pizzáscsiga ", 3) )
















