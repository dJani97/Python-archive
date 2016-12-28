A = 6
B = 3

def lnko(a, b):
    kozososzto = 1
    maradek = None
    
    while maradek!=0:
        maradek = a%b
        if maradek == 0:
            break
        else:
             kozososzto = maradek
        a, b = b, maradek

    return kozososzto

def main(a, b):
    eredmeny = lnko(a, b)
    lkkt = a*b / eredmeny
    print ("Szamok: {}, {}\nLNKO = {}\nEllenorzes: A/{} = {}, B/{} = {}\nLKKT = {}".format(A, B, eredmeny, eredmeny, A/eredmeny, eredmeny, B/eredmeny, lkkt))

main(A, B)
