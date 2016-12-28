import sys
sys.setrecursionlimit(8000)


n = 7500


def valami(n):
    n -= 1
    if n > 0:
        n = valami(n)
    return n
print (valami(n))
