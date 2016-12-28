









lst = [1, 4, 9, 10, 12, 15, 16, 17, 18, 19, 26,
       34, 37, 38, 39, 42, 43, 51, 57, 58, 63, 64]







print (len(lst))

while True:
    new = int(input("New number: "))
    if new not in lst:
        lst.append(new)
    else:
        print ("Already in list!")
    lst.sort()
    print (lst, "\tlen =", len(lst))
