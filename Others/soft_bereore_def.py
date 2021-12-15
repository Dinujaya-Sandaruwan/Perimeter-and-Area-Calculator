#import packges
import tkinter
from tkinter import *
from PIL import ImageTk, Image

#window_settings
window = Tk()
window.title("Circle Calculator")
window.geometry("1080x670")
window.resizable(False,False)
window.iconbitmap('ball_icon.ico')
window.configure(bg='#1D1C1C')

#title
tit_label = Label(window, text = "Calculate Area and Perimeter \n using Radius", bg = '#1D1C1C', fg = '#4CF49C')
tit_label.config(font=('Bauhaus 93', 40))
tit_label.grid(pady = 10, padx = 200, row = 0, column = 0, columnspan = 2)

#label(Enter Radius)
lab_1 = Label(window, text = "Enter Radius", bg = '#1D1C1C', fg ='#FDFBFB')
lab_1.config(font=('Arial Black', 20))
lab_1.grid(pady = 20, row = 1, column = 0)

#Main Entry
ent_1 = Entry(window, width = 20)
ent_1.config (font=('Arial Black', 20))
ent_1.grid(pady = 20, row = 1, column = 1,)

#Buttons
area_bt = Button(window, text = "Calculate Area", padx = 30, pady = 10, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10,)
area_bt.config (font=('Courgette', 10))

rad_bt = Button(window, text = "Calculate Radius", padx = 30, pady = 10, bg='#0052cc', fg='#ffffff', activebackground='black',activeforeground = 'white', borderwidth = 10)
rad_bt.config (font=('Courgette', 10))

#create delete button
del_bt_img = Image.open("del_bt.png")
resized = del_bt_img.resize((120,100), Image.ANTIALIAS)
new_dil = ImageTk.PhotoImage(resized)

del_bt = Button(window, image = new_dil, bg='#1D1C1C',activebackground='#1D1C1C', borderwidth = 0)


#button posisionig
area_bt.grid(row = 2, column = 1)
rad_bt.grid(row = 3, column = 1, pady = 10 )
del_bt.grid(row = 3, column = 0)

#Answer(print)
ans_label = Label(window, text = "According to your Radius, The answer is", bg='#1D1C1C', fg = '#ffffff')
ans_label.config(font = ('Cabin Sketch', 40))

ans_label.grid(pady =30, row = 4, column = 0, columnspan = 2)

final_ans = Label(window, text = "68.589", bg ='#1D1C1C', fg ='#ffffff')
final_ans.config(font = ('Lemon', 45))

final_ans.grid(row = 5, column = 0, columnspan = 2)



#mainloop
window.mainloop()

