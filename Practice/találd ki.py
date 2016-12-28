import random

print ("Gondoltam egy számra 1 és 15 között, próbáld meg kitalálni!")
titkos = random.randrange(1, 15)
count, guess = 1, 0

while guess is not titkos:
    guess = int(input("Tipp:"))
    if guess is titkos:
        print ("Gratulálok, a szám: ", titkos, "\nPróbálkozások száma: ", count)
        input()
        exit()
    else:
        count += 1

input()
exit()