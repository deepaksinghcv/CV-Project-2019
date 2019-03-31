from tkinter import *


class MyButtons:
	def __init__(self,master):
		frame = Frame(master)
		frame.pack()

		self.printButton = Button(frame,text="DOWNLOAD VIRUS ",command=self.printMessage)
		self.printButton.pack(side=LEFT)

		self.quitButton = Button(frame,text="QUIT",command=frame.quit)
		self.quitButton.pack(side=LEFT)

	def printMessage(self):
		print("A is shown")


root = Tk()

buttonsObj = MyButtons(root)

root.mainloop()