# Basic GUI/TKINTER

from tkinter import *

gui = Tk()
gui.geometry('500x500')
l = Label(gui, text='Basic GUI via TKINTER', font=(None, 30))
l.pack()
gui.mainloop
