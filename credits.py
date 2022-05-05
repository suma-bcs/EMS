#Suma C_52045367

from tkinter import*
from tkinter import messagebox
import os, random

colors=["teal","plum","cadetblue"]
def click():
    cur_time=("©Suma C\n#52045367")
    label.config(text=cur_time,fg=random.choice(colors))
    label.after(1000,click)
win=Tk()
win.title("EMS - Done by")
win.config(bg="white")
win.resizable(0,0)
'''win.iconbitmap("logo.ico")'''
win.geometry("500x100")
label=Label(win,font=('Segoe Print',14,'bold'),bg='white')
label.pack()
click()
win.mainloop()
