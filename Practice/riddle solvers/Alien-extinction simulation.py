import random

# bugos

a = 1
steplist = []

for all_tests in range(20):
    for c in range(1000):
        if a>0:
            p = random.choice(("a-=1", "pass", "a+=1", "a+=2"))
            exec(p)
            print(a)
        
    steplist.append(c)

print (steplist)
