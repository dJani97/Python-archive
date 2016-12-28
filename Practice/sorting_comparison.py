import random, time
all_tests = 5
total_time = 0
total_changes = 0
lenght = 20000000


print("Length of lists:", lenght)
"""
for _ in range(all_tests):

    
    a = list(range(lenght))
    random.shuffle(a)

    all_changes = 0

    starting = time.time()

    while True:
        changes = 0
        for x in range(lenght-1):
            if a[x] > a[x+1]:
                a[x],  a[x+1] =  a[x+1],  a[x]
                changes+=1

        if changes == 0:
            break
        all_changes += changes

    elapsed = time.time()-starting
    print("Time: {}\nChanges made: {}".format(elapsed, all_changes))

    total_time += elapsed
    total_changes += all_changes


print("\n_________________________\nAvg.time: {}\nAvg. changes: {}".format(total_time/all_tests, total_changes/all_tests))
"""

for _ in range(all_tests):

    a = list(range(lenght))
    random.shuffle(a)
    all_changes = 0
    starting = time.time()

    a.sort()

    elapsed = time.time()-starting
    print("Time: {}\nChanges made: unknown".format(elapsed))

    total_time += elapsed
    total_changes += all_changes


print("\n_________________________\nAvg.time: {}\nAvg. changes: {}".format(total_time/all_tests, total_changes/all_tests))
