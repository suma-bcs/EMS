#Suma C_52045367

from multiprocessing.pool import CLOSE
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
import csv, os

global uno,name,clas,persent,win
def update():
    global uno,name,clas,persent,win
    u=uno.get()
    n=name.get()
    c=clas.get()
    p=persent.get()
    data=[]
    file=open("records.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        if row[0]==u:
            data.append([row[0],n,c,p])
        else:
            data.append(row)
    file.close()
    file=open("records.csv","w")
    write=csv.writer(file,delimiter=",",lineterminator="\n")
    write.writerows(data)
    file.close()
    messagebox.showinfo("CSV","Data Updated Sucessfully")
    win.geometry("350x80")
    uno.set("Select SAP Code")
def find():
    global uno,name,clas,persent
    u=uno.get()
    if u=="Select SAP Code":
        messagebox.showinfo("CSV","Please Select SAP Code")
    elif len(u)>0 :
        file=open("records.csv")
        reader=csv.reader(file,delimiter=",")
        for row in reader:
            if int(u)==int(row[0]):
                win.geometry("350x250")
                name.set(row[1])
                clas.set(row[2])
                persent.set(row[3])
        file.close()
def press(e):
    global uno,name,clas,persent
    u=uno.get()
    if u=="Select SAP Code":
        messagebox.showinfo("CSV","Please Select SAP Code")
    if repr(e.keycode)==67:
        CLOSE()
    elif len(u)>0 :
        if repr(e.keysym)=="'Return'":
            find()
    else:
        messagebox.showinfo("CSV","Please Select SAP Code")
def main():
    global uno,name,clas,persent,win
    win=Tk()
    win.title("EMS - Update Record")
    win.geometry("350x80")
    win.config(bg="teal")
    win.resizable(0,0)
    '''win.iconbitmap("logo.ico")'''
    uno=StringVar()
    name=StringVar()
    clas=StringVar()
    persent=StringVar()
    data=[]
    Label(win,text="Update Record",bg="teal",fg="white",font=("Georgia",16)).place(x=120,y=2)
    Label(win,text="SAP Code",bg="white",fg="teal",font=("Georgia",12)).place(x=30,y=50)
    Label(win,text="Name",bg="white",fg="teal",font=("Georgia",12)).place(x=30,y=90)
    Label(win,text="Qualification",bg="white",fg="teal",font=("Georgia",12)).place(x=30,y=130)
    Label(win,text="Certification",bg="white",fg="teal",font=("Georgia",12)).place(x=30,y=170)
    file=open("records.csv")
    read=csv.reader(file,delimiter=",")
    for row in read:
        data.append(row[0])
    e0=OptionMenu(win,uno,"Select SAP Code",*data)
    e0.place(x=140,y=50)
    e0.focus()
    e1=Entry(win,textvariable=name,state="normal")
    e1.place(x=140,y=90)
    e1.focus()
    e2=Entry(win,textvariable=clas,state="normal")
    e2.place(x=140,y=130)
    e3=Entry(win,textvariable=persent,state="normal")
    e3.place(x=140,y=170)
    Button(win,text="Find",bg="white",fg="teal",font=("Georgia",9),command=find).place(x=290,y=47)
    Button(win,text="Update",bg="white",fg="teal",font=("Georgia",9),command=update).place(x=150,y=200)
    win.bind("<Key>",press)
    win.mainloop()
if __name__=="__main__":
    main()
