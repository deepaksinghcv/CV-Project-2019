import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog

def clicked():
	res = "the msg is :"+txt.get()
	lbl1.configure(text=res)

window = tk.Tk()

window.title("Welcome to UI")
window.geometry('350x200')

lbl1 = tk.Label(window,text='Hello',font=("Arial Bold",12))
lbl1.grid(column=0,row=0)

btn = tk.Button(window,text="click me",bg="orange",fg="red",command=clicked)
btn.grid(column=1,row=0)


txt = tk.Entry(window,width=10,state='disabled')
txt.grid(column=1,row=1)
txt.focus()

# scrollTxt = scrolledtext.ScrolledText(window,width=20,height=10)
# scrollTxt.insert(INSERT,"Logs will go here!")
# scrollTxt.grid(column=2,row=2)

file = filedialog.askopenfilename()


window.mainloop()