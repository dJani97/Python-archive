import random, time
start = time.time()

dic = set()
with open ("eng-germ dict.txt", "r") as file:
    for sor in file:
        dic.add(sor.strip().split("\t")[0].split()[0])
dic = list(dic)
dic.sort()

i = "next".lower()    # we are looking for this

need = list(set(i))
final = [[] for x in range(len(need))]
for word in dic:
    c = 0
    for needed_word in need:
        if needed_word == word[0]:
            final[c].append(word)
            break
        c+=1

output = set()
for _ in range(10000000):
    final_word = ""
    for word in i:
        for collection in final:
            if collection[0][0] == word:
                final_word += random.choice(collection)+" "
    output.add(final_word)

output = list(output)
output.sort()
#print ("\n".join(x for x in output))
print (len(output))

with open (str(i).upper()+"-dict.txt", "w") as file:
    file.write("\n".join(x for x in output))

print (time.time()-start)
