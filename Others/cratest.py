import tkinter
import tkinter.font as font
from tkinter import *
window = Tk()
window.title("My New Project")

#fonts
font_1 = font.Font(family='Bauhaus 93')

bt_1 = Button(window, text = "button 01", padx = 10, pady = 50, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10)
bt_1.grid(row = 0, column = 0, padx = 25, pady = 25)
bt_1['font'] = font_1 

bt_2 = Button(window, text = "button 02")
bt_2.grid(row = 0, column = 1, padx = 5, pady = 25)


window.mainloop()