#import packges

import tkinter
from tkinter import *

#other_varibles
pie = (22/7)

#basic window Settings
window = Tk()
window.title("My New Project")
window.geometry("500x300")

#label(01)
lab_1 = Label(window, text = "Enter Your Number", font = (45))
lab_1.pack(pady = 10)

#entry(01)
ent_1 = Entry(window, width = "40", font = (30))
ent_1.pack(pady = 5)


#definicatios
def bt_com_1():
    global lab_2

    ent_1.get()
    imp_int = int(ent_1.get())

    math_1 = 2*pie*imp_int
    math_1_int = int(math_1)

    lab_1_5 = Label(window, text = "Your Anser is :").pack(pady = 15)

    lab_2 = Label(text = math_1_int, font = 30)
    lab_2.pack(pady = 10)

def delete_cmd():
    lab_2.pack_forget()
    ent_1.delete(0,END)

#buttons
bt_1 = Button(window, width = 30, text = "Click To Calculate", command = bt_com_1)
bt_1.pack(pady = 15, padx = 10)

deleteBt = Button(window, width = 30, text = "Delete", command = delete_cmd)
deleteBt.pack()

window.mainloop()