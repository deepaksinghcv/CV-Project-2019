import tkinter as tk
import PIL
from PIL import ImageTk, Image
window = tk.Tk()

window.title("Display Image")
window.geometry('300x300')
window.configure(background='grey')

path = './bestsimas om.png'

img = ImageTk.PhotoImage(Image.open(path))

panel = tk.Label(window,image=img)

panel.pack(side='bottom',fill='both',expand='yes')

window.mainloop()