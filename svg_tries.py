from tkinter import *

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "")


def myClick():
    hello = "Your input: " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


myButton = Button(root, text="Big Button", command=myClick)
myButton.pack()

root.mainloop()