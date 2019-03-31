from tkinter import *

root = Tk()

usernameLabel = Label(root,text="Name:")
passwordLabel = Label(root,text="Password:")

usernameEntry = Entry(root)
passwordEntry = Entry(root)

usernameLabel.grid(row=0,sticky=E)
passwordLabel.grid(row=1,sticky=E)
usernameEntry.grid(row=0,column=1)
passwordEntry.grid(row=1,column=1)

loggedInCheckBox = Checkbutton(root,text="Save Password")
loggedInCheckBox.grid(columnspan=2)

root.mainloop()