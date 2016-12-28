from tkinter import *



class My_tkinter_class:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Sg", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMessage(self):
        print("K")



#
root = Tk()
b = My_tkinter_class(root)
root.title("My first GUI app")
#



# Mouse events
"""
def left_click(event):
    print ("Left")
def middle_click(event):
    print ("Mid")
def right_click(event):
    print ("Right")

frame = Frame(root, width=300, height=250)
frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()
"""

# Button function
"""
def my_function(event):
    print("Hi")

#button1 = Button(root, text="command", command=my_function)
button1 = Button(root, text="command")
button1.bind("<Button-1>", my_function)
button1.pack()
"""

# Label, entry, checkbox
"""
label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root)
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E) # == East. [N, E, S, W]
label_2.grid(row=1)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")
c.grid(columnspan=2)
"""

# LABELS
"""
one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()
two = Label(root, text = "Two", bg = "yellow", fg = "green")
two.pack(fill=X)

three = Label(root, text = "Three", bg = "blue", fg = "black")
three.pack(side = LEFT, fill = Y)
"""

# BUTTONS
"""
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text =  "First Button", fg = "red")
button2 = Button(topFrame, text =  "Second Button", fg = "blue")
button3 = Button(topFrame, text =  "Third Button", fg = "green")

button4 = Button(bottomFrame, text =  "Last Button", fg = "purple")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)
"""

root.mainloop()
