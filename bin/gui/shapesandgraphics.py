from tkinter import *

root = Tk()

canvas = Canvas(root, width = 200,height=100)
canvas.pack()

blackLine = canvas.create_line(0,0,50,50)
redLine = canvas.create_line(50,50,0,50,fill='red')

blueRect = canvas.create_rectangle(50,50,100,100,fill='green')

canvas.delete(redLine)

canvas.delete(ALL)

root.mainloop()