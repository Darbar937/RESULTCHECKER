
import pandas as pd
from tkinter import*
from PIL import Image, ImageTk
import openpyxl
r=Tk()
r.geometry("500x500")
f=Frame(r,width=5000,height=5000,bg="Light blue")
img=ImageTk.PhotoImage(file="C:\\Users\\shaik\\Downloads\\mk.png")
la1=Label(f,image=img)
f.propagate(0)
f.pack()
la1.pack()
def tab1():
    def tab2():
        d=pd.read_excel("C:\\Users\\shaik\\Desktop\\marks2.xlsx")
        df=pd.DataFrame(d)
        str=e1.get()
        M1=Label(f,text=df[["ROLL NUMBER"]][df["ROLL NUMBER"]==str],font=("AERIAL",13,"bold"),width=100,borderwidth=20)
        M1.place(x=300,y=200)
        M2=Label(f,text=df[["STUDENT NAME"]][df["ROLL NUMBER"]==str],font=("AERIAL",13,"bold"),width=100,borderwidth=20)
        M2.place(x=300,y=300)
        M3=Label(f,text=df[["DSSM"]][df["ROLL NUMBER"]==str],font=("AERIAL",13,"bold"),width=100,borderwidth=20)

        M3.place(x=300,y=400)
        M4=Label(f,text=df[["SE"]][df["ROLL NUMBER"]==str],font=("AERIAL",13,"bold"),width=100,borderwidth=20)

        M4.place(x=300,y=500)
        M5=Label(f,text=df[["OS"]][df["ROLL NUMBER"]==str],font=("AERIAL",13,"bold"),width=100,borderwidth=20)

        M5.place(x=300,y=600)
        b1.destroy()
        m2.destroy()
        l2.destroy()
        e1.destroy()
        def back():
            d.destroy()
            str.destroy()
            M1.destroy()
            M2.destroy()
            M3.destroy()
            M4.destroy()
            M5.destroy()
            tab1()
        b2=Button(text="BACK >",borderwidth=5,command=back)
        b2.bind("<Button-1>")
        b2.place(x=700,y=750)
    m2=Label(r,text="SVCK RESULT",font=("Times of roman",30,"bold"))
    m2.place(x=600,y=50)
    l2=Label(f,text="ROLL NO",font=("sans",20,"italic"),width=10)
    l2.place(x=500,y=300)
    e1=Entry(f,width=50,borderwidth=10)
    e1.place(x=700,y=300)
    b1=Button(f,text="CLICK HERE >",borderwidth=5,command=tab2)
    b1.bind("<Button-1>")
    b1.place(x=700,y=450)
tab1()
r.mainloop()