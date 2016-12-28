x = []
with open ("list_of_all_games.txt", "r") as file:
    for line in file:
        line = line.strip().replace("(", "|$|", 1)
        line = line[::-1].replace("(","|$|", 1)[::-1]
        line = line.replace("(", "").replace(")", "")
        
        x. append (line.split("|$|"))
        
c = 1
for y in x:
    print (y)
    if c > 200:
        break
    c+=1

