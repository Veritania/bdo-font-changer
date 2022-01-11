from tkinter import *
from tkinter.ttk import * # Overrides tk default ui to instead match OS
from tkinter import filedialog
import tkinter as tk


def browseFiles():
    game_dir = filedialog.askdirectory(initialdir = "/", title = "Select BDO install folder")
    # Change label contents
    print("Game dir selected: " + game_dir)

# -- UI --
root = Tk()
root.geometry('500x250')
root.title("BDO Font Patcher")
#root.config(background = "black")


# Game Directory Label
game_directory_label = Label(root, text = "Game Directory").place(x = 40, y = 10)

default_dir = tk.StringVar(root, "C:\Pearlabyss\BlackDesert")
game_dir_entry = Entry(root, width=50, textvariable=default_dir).place(x = 40, y = 30)


# Browse Game Dir Button
browse_button = Button(root, text = "Browse...", command = browseFiles).place(x = 370, y = 30)


# Patch Font Button
patch_font_btn = Button(root, text = 'Patch font', command = root.destroy).place(x = 40, y = 130) 
root.mainloop()

    