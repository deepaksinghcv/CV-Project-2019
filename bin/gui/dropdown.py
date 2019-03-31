from tkinter import *

class doNothing():
	print("doing nothing")




root = Tk()

menu = Menu(root)
root.config(menu=menu) #tk has built in configuration of where to place menu bar

subMenu1 = Menu(menu)
menu.add_cascade(label="File",menu=subMenu1)
subMenu1.add_command(label="New",command=doNothing)
subMenu1.add_command(label="Open",command=doNothing)
subMenu1.add_separator()
subMenu1.add_command(label="Save",command=doNothing)

subMenu2 = Menu(menu)
menu.add_cascade(label="Edit",menu=subMenu2)
subMenu2.add_command(label="Edit As",command=doNothing)
subMenu2.add_command(label="Save As",command=doNothing)
subMenu2.add_separator()
subMenu2.add_command(label="Undo",command=doNothing)
subMenu2.add_command(label="Redo",command=doNothing)


root.mainloop()