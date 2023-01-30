from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from managemedicine import *
from buymedicine import *
from sellmedicine import *



def staffpage():
    global root
    root=Tk()
    root.title("Staff Window")
    root.geometry("1350x700+0+0")
    root.maxsize(width=1350,height=700)

    #-------Headings-------
    main_title=Label(root,text="STAFF PAGE FOR PHARMACY MANAGEMENT",font=("times new roman",25,"bold"),bg="brown",fg="white").place(x=0,y=0,width=1350)

    #-----log out Button-----
    logout_btn=Button(root,text="LOG OUT",font=("times new roman",20,"bold"),command=root.destroy,bd=3,bg="purple",fg="white",cursor="hand2")
    logout_btn.place(x=1100,y=90,width=150,height=50)

    #-------buttons-------
    mng_btn=Button(root,text="MANAGE MEDICINE",font=("times new roman",20,"bold"),command=mngmed_func,bd=3,bg="red",fg="white",cursor="hand2")
    mng_btn.place(x=470,y=200,width=450,height=40)

    sell_btn=Button(root,text="BUY MEDICINE",font=("times new roman",20,"bold"),command=buymed_func,bd=3,bg="red",fg="white",cursor="hand2")
    sell_btn.place(x=470,y=250,width=450,height=40)

    transaction_btn=Button(root,text="SELL MEDICINE",font=("times new roman",20,"bold"),command=sellmed_func,bd=3,bg="red",fg="white",cursor="hand2")
    transaction_btn.place(x=470,y=300,width=450,height=40)

    root.mainloop()

def mngmed_func():
    managemedicine()

def sellmed_func():
    sellmedicine()

def buymed_func():
    buymedicine()

#staffpage()