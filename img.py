# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 21:06:42 2019

@author: mypc
"""

from tkinter import *
from PIL import ImageTk, Image
import wSelect


#initialise
window=Tk()

window.title("Hangman.exe")
window.configure(bg='cyan')

img = ImageTk.PhotoImage(Image.open("1.gif"))
panel = Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


window.mainloop()