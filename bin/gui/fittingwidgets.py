from tkinter import *

root = Tk()

one = Label(root, text="ONE", bg="red",fg="white")
one.pack(fill=X)

two = Label(root, text="TWO", bg="green",fg="yellow")
two.pack(side=RIGHT,fill=Y)

three = Label(root,text="THREE",bg="purple",fg="white")
three.pack(side=LEFT,fill=Y)


root.mainloop()