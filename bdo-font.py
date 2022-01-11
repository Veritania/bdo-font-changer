from tkinter import *
from tkinter.ttk import * # Overrides tk default ui to instead match OS
import os

root = Tk()

root.geometry('500x250')


game_directory = Label(root, text = "Game Install Location").place(x = 40, y = 10)

patch_font_btn = Button(root, text = 'Patch font', command = root.destroy).place(x = 40, y = 130) 


root.mainloop()

    