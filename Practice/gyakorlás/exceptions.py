print("What's your fav number?")

while True:
    try:
        number = float(input())
        print(10/number)
        break
    except ValueError:
        print("Well, that's not a number... \nTry again:")
    except ZeroDivisionError:
        print("Don't enter Zero")

input()
exit()