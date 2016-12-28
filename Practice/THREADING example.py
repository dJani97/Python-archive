import threading

def add_to_x():
    global kill, x
    while not kill:
        x += 0.001
    print (str(x)+", ")

def subt_from_x():
    global kill, x
    while not kill:
        x -= 0.001

def main():
    global kill, x
    kill = False
    x = 0
    our_thread = threading.Thread( target = subt_from_x , name = "sub")
    our_thread.start()
    sec_thread = threading.Thread( target = add_to_x , name = "add")
    sec_thread.start()
    
    print (threading.active_count())
    print (threading.enumerate())
    print (our_thread.is_alive())

    input("Enter to kill")
    kill = True

if (__name__ == "__main__"):
    main()
