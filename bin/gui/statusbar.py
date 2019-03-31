from tkinter import *

def doNothing():
	print("Doing Nothing")


root = Tk()


# MENU 
menu = Menu(root)
root.config(menu=menu)

subMenu1 = Menu(menu)
menu.add_cascade(label="File",menu=subMenu1)

subMenu1.add_command(label="Open File",command=doNothing)
subMenu1.add_command(label="Open Folder",command=doNothing)
subMenu1.add_separator()
subMenu1.add_command(label="Open Recent",command=doNothing)

subMenu2 = Menu(menu)
menu.add_cascade(label="Edit",menu=subMenu2)

subMenu2.add_command(label="Undo",command=doNothing)
subMenu2.add_command(label="Redo",command=doNothing)

# TOOLBAR

toolbar = Frame(root,bg="blue")
insertButton = Button(toolbar, text="Insert Image", command=doNothing)
insertButton.pack(side=LEFT, padx=2, pady=2)

editButton = Button(toolbar, text="Edit Image", command=doNothing)
editButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)


# STATUS BAR

status = Label(root,text="Status goes here...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
