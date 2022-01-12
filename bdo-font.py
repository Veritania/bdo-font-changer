from tkinter import *
from tkinter.ttk import *  # Overrides tk default ui to instead match OS
from tkinter import filedialog
import tkinter as tk
from tkinter import font


def browseFiles():
    game_dir = filedialog.askdirectory(
        initialdir="/", title="Select BDO install folder")
    # Change label contents
    game_dir_entry.delete(0, END)
    game_dir_entry.insert(0, game_dir)


# -- UI --
root = Tk()
root.geometry('500x250')
root.title("BDO Font Patcher")


# Game Directory
game_directory_label = Label(root, text="Game Directory")
game_directory_label.place(x=40, y=10)

default_dir = tk.StringVar(root, "C:/Pearlabyss/BlackDesert")
game_dir_entry = Entry(root, width=50, textvariable=default_dir)
game_dir_entry.place(x=40, y=30)

browse_button = Button(root, text="Browse...", command=browseFiles)
browse_button.place(x=370, y=30)


# Font Selection
font_label = Label(root, text="Select custom font")
font_label.place(x=40, y=60)

fonts = list(font.families())

# TODO: Filter fonts to only get .ttf (TrueType Fonts)
# TODO: Fetch fonts manually via C:\Windows\Fonts and check if they're .ttf
font_collection = StringVar(root)
font_collection.set(fonts)

font_dropdown = OptionMenu(root, font_collection, *font.families())
font_dropdown.place(x=40, y=80)

for item in range(0, int(font_dropdown['menu'].index('end'))):
    font_dropdown['menu'].entryconfig(
        item, font=font.Font(family=font.families()[item]))


# Patch Font Button (Temporarily just exits application)
patch_font_button = Button(root, text='Patch font', command=root.destroy)
patch_font_button.place(x=40, y=130)
root.mainloop()
