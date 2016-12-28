tomb = []

with open ("freedict", "r") as file:
    for line in file:
        tomb.append( line.strip() )


for elem in tomb:
    if elem[-3:] == "ész":
        print (elem)

print ("Kész")
