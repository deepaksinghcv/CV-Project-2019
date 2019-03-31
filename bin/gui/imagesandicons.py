from tkinter import *
from PIL import ImageTk, Image

root = Tk()

openedImage = Image.open("mmts.jpg")
openedImage = openedImage.resize((250, 250), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(openedImage)  

label = Label(root,image=photo,width=480,height=320)
label.pack()

root.mainloop()