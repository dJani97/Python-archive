import math

while True:
    q = int(input("Add meg a \"normális\" horcsogok szamat: ")) #AA és Aa
    p = int(input("Add meg a sunyi homozigota recessziv mutans gecik szamat: ")) #aa

    effectieve_p = (math.sqrt(p/(p+q)))
    effectieve_q = 1-effectieve_p

    homo_dom = (effectieve_q**2)*(q+p)
    homo_rec = (effectieve_p**2)*(q+p)
    hetero = 2*(effectieve_q*effectieve_p)*(q+p)

    print ("\n","_"*8, "EREDMENYEK:", "_"*8)
    print ("Homozigota dominans:", int(homo_dom))
    print ("Homozigota recessziv mutans gecik:", int(homo_rec))
    print ("Heterozigita hordozo gecik:", int(hetero))

    input ("\nUss entert az ujrakezdeshez!\n")
