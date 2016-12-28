
def input_vizsgalo ():
    while True:
        a = input("")
        b = input("")
        try:
            a, b = int(a), int(b)
            return [a, b]
        except:
            print ("1. A művelet ezekre a számokra nem értelmezhető: {}, {}".format(a, b))

def varazslat (a, b):
    if a+b>=0:
        return int("{}{}".format(a-b, a+b))
    else:
        return "2. A művelet ezekre a számokra nem értelmezhető: {}, {}".format(a, b)


a, b = input_vizsgalo()

print (varazslat(a, b))

