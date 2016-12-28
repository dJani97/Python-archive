l = []
count = 0
SEARCH_FOR = "megtekintés"

with open ("keresnivalo.txt", "r") as file:
    for line in file:
        line = line.split()
        #print (line)
        
        for word in line:
            l.append(str(word))
        
print ("Reading done...")

for word in l:
    if word[:len(SEARCH_FOR)] == SEARCH_FOR:
        #print (word)
        count += 1


print ("Found:", count)
