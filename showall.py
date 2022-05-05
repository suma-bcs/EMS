﻿#Suma C_52045367

from tkinter import *
import csv

global canvas
win1=Tk()
win1.title("EMS - Show all Employees")
win1.geometry("450x360")
win1.config(bg="teal")
win1.resizable(0,0)
'''win1.iconbitmap("logo.ico")'''
frame=Frame(win1)
frame.pack()
yscrollbar = Scrollbar(frame, orient='vertical',command=lambda *args: onscroll('y-axis', *args))
yscrollbar.pack(side="right",anchor="w",fill="both")
canvas=Canvas(frame,bg="white",width="450",height="300",scrollregion=(0, 0, 0, 2050),yscrollcommand=yscrollbar.set)
canvas.pack()
main_frame=Frame(canvas,bg="white")
canvas.create_window((0,0),window=main_frame,anchor="nw")
canvas.yview_scroll(100, "units")
canvas.xview_scroll(100, "units")
Label(main_frame,text="SAP Code",bg="teal",fg="white",font=("Georgia",12)).grid(row=0,column=0)
Label(main_frame,text="Name",bg="teal",fg="white",font=("Georgia",12)).grid(row=0,column=1,padx=30)
Label(main_frame,text="Qualification",bg="teal",fg="white",font=("Georgia",12)).grid(row=0,column=2,padx=30)
Label(main_frame,text="Certification",bg="teal",fg="white",font=("Georgia",12)).grid(row=0,column=3)
with open("records.csv") as file:
    read=csv.reader(file)
    row_value=1
    for i in read:
        Label(main_frame,text=i[0],bg="white",fg="teal",font=("Georgia",12)).grid(row=row_value,column=0)
        Label(main_frame,text=i[1],bg="white",fg="teal",font=("Georgia",12)).grid(row=row_value,column=1)
        Label(main_frame,text=i[2],bg="white",fg="teal",font=("Georgia",12)).grid(row=row_value,column=2)
        Label(main_frame,text=i[3],bg="white",fg="teal",font=("Georgia",12)).grid(row=row_value,column=3)
        row_value+=1
   
win1.mainloop()
