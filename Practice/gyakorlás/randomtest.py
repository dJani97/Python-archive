import random

also_hatar = 1
felso_hatar = 101



y = 0
max_x = also_hatar
min_x = felso_hatar
while y < 1000:
    x = random.randrange(also_hatar, felso_hatar)
    print (x)
    y += 1
    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x

print ("legkisebb:", min_x, "legnagyobb:", max_x)
input()
exit()
