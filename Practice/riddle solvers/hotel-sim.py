import random
rooms = 12
goal = 0
all_cases = 0
while goal < 100:
    ho = [0]*rooms
    while True:
        ho[random.randrange(rooms)] += 1
        if 0 not in ho:
            goal += 1
            break
        elif 2 in ho:
            all_cases += 1
            break

print ("{}%".format(str((goal/all_cases)*100)))
            
        
