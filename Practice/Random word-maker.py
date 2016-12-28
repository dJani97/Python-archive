import string, random

l = set([]) # Full list of words
current = ""
dictionary = "abcdefgh"
# "abcdefghijklmnopqrstuvwxyzaeiouaeiou  "
print(dictionary)

while len(l) < 100:
    current += random.choice(dictionary)
    #print (current)
    if current[-1] == " " or len(current) > 8:
        final = ""
        for x in current:
            if x != " ":
                final += x
        if len(final) > 3:
            l.add(final)
            current = ""
    

for x in l:
    print (""+x) #+random.choice(",."))
