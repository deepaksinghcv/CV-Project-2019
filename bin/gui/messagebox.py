from tkinter import *
import tkinter.messagebox

root =  Tk()

tkinter.messagebox.showinfo('Window Title',"do you want to save it!")

answer = tkinter.messagebox.askquestion("Question 1","do you like it?")

if answer == 'yes':
	print("so you like it!")

else:
	print("so you don't like it!")


root.mainloop()