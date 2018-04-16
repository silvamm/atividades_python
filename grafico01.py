from tkinter import *

def Cumprimente():
    hello.set("Olá, você!")

gui = Tk()

gui.title("Galgo v0.1")
gui.geometry("200x30")


btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()