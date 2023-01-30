from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3



def additem():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("pharmacy.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM MEDICINE WHERE ID=? ''',(entry1.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","Medicine with ID="+str(entry1.get())+" Already Exists")
                root.destroy()
            else:
                cur.execute('''INSERT INTO MEDICINE VALUES (?,?,?,?,?)''',(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get()))
                con.commit()
                con.close()
                fetch_data()
                messagebox.showinfo("Success","Medicine Added Successfully")
                root.destroy()
        except Exception as es:
            messagebox.showerror("Error due to:{str(es)}")
            root.destroy()



def deleteitem():
    try:
        con=sqlite3.connect("pharmacy.sqlite")
        cur=con.cursor()
        cur.execute('''SELECT * FROM MEDICINE WHERE ID=?''',(entry1.get(),))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("ERROR","Medicine With ID="+str(entry1.get())+" Does'nt Exists")
            root.destroy()
        else:
            cur.execute('''DELETE FROM MEDICINE WHERE ID=?''',(entry1.get(),))
            messagebox.showinfo("Success","Book Deleted Successfully")
            con.commit()
            con.close()
            fetch_data()
            root.destroy()
    except Exception as es:
        messagebox.showerror("Error due to:{str(es)}")
        root.destroy()
    


def updateitem():
    try:
        if (entry1.get()=="") or (entry2.get()=="") or (entry3.get()=="") or (entry4.get()=="") or (entry5.get()==""):
            messagebox.showerror("Error","All fields are required!!!")
            root.destroy()
        else:
            con = sqlite3.connect('pharmacy.sqlite')
            cur = con.cursor()
            cur.execute('''UPDATE MEDICINE SET ID=?,NAME=?,PRICE=?,QUANTITY=?,CATEGORY=? WHERE ID=? AND QUANTITY=?''',(entry1.get(),
                                                                        entry2.get(),
                                                                        entry3.get(),
                                                                        entry4.get(),
                                                                        entry5.get(),
                                                                        entry1.get(),
                                                                        entry4.get()))
            con.commit()
            messagebox.showinfo("Upated","Member Details Updated Successfully")
            fetch_data()
            con.close()
            root.destroy()
    except Exception as es:
        messagebox.showerror("Error Due To:{str(es)}")
        root.destroy()

    

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

def search():
    try:
        con = sqlite3.connect('pharmacy.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM MEDICINE WHERE "+str(combo_search.get())+" LIKE '%"+str(txt1.get())+"%'" )
        rows=cur.fetchall()
        if len(rows)!=0:
            Medicine_table.delete(*Medicine_table.get_children())
            for row in rows:
                Medicine_table.insert('',END,values=row)
                con.commit()
        con.close()
        clearsearch()
    except Exception as es:
        messagebox.showerror("Error Due To:{str(es)}")
        clearsearch()

def fetch_data():
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM MEDICINE''')
    rows=cur.fetchall()
    if len(rows)!=0:
        Medicine_table.delete(*Medicine_table.get_children())
        for row in rows:
            Medicine_table.insert('',END,values=row)
            conn.commit()
    conn.close()

def get_cursor(ev):                              
    curosor_row=Medicine_table.focus()                      
    contents=Medicine_table.item(curosor_row)   
    row=contents['values']
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry1.insert(0, str(row[0]))
    entry2.insert(0, str(row[1]))
    entry3.insert(0, str(row[2]))
    entry4.insert(0, str(row[3]))
    entry5.insert(0, str(row[4]))

def clearsearch():
    combo_search.current(0)
    txt1.delete(0,END)


def managemedicine():
    global root,entry1,entry2,entry3,entry4,entry5,txt1,combo_search,Medicine_table
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS MEDICINE(ID NUMBER PRIMARY KEY,NAME TEXT,PRICE NUMBER,QUANTITY NUMBER,CATEGORY TEXT)''')
    conn.commit()
    conn.close()

    root = Tk()
    root.title("Manage Medicine Window")
    root.geometry("1300x700+0+0")
    root.configure(bg='BLACK')

    label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("Times", 30))
    label1=Label(root,text="ENTER ITEM ID",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
    entry1=Entry(root , font=("Times", 12))
    label2=Label(root, text="ENTER ITEM NAME",bd="2",relief="ridge",height="1",bg="red",fg="white", font=("Times", 12),width=25)
    entry2= Entry(root, font=("Times", 12))
    label3=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
    entry3= Entry(root, font=("Times", 12))
    label4=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
    entry4= Entry(root, font=("Times", 12))
    label5=Label(root, text="ENTER ITEM CATEGORY",bg="red",relief="ridge",fg="white", font=("Times", 12),width=25)
    entry5= Entry(root, font=("Times", 12))

    button1= Button(root, text="ADD ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=additem)
    button2= Button(root, text="DELETE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=deleteitem)
    button3= Button(root, text="UPDATE ITEM", bg="white", fg="black", width =20, font=("Times", 12),command=updateitem)
    button4= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)

    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
    label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
    label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
    entry1.grid(row=1,column=1, padx=40, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    entry3.grid(row=3,column=1, padx=10, pady=10)
    entry4.grid(row=4,column=1, padx=10, pady=10)
    entry5.grid(row=5,column=1, padx=10, pady=10)
    button1.grid(row=1,column=4, padx=40, pady=10)
    button2.grid(row=1,column=5, padx=40, pady=10)
    button3.grid(row=2,column=4, padx=40, pady=10)
    button4.grid(row=2,column=5, padx=40, pady=10)

    logout_btn=Button(root,text="Quit",command=root.destroy,bg="purple",relief="ridge",fg="white",bd=3,font=("Times", 12),width=20,cursor="hand2").place(x=1100,y=25)

    #----------------------------Detail Frame-------------------
    detail_frame = Frame(root,bd=4,relief=RIDGE,bg="white")
    detail_frame.place(x=40,y=350,width=1220,height=330)

    lb1=Label(detail_frame,text="Search By",font=('times of roman',15,"bold"),bg="white",fg="BLACK").grid(row=0,column=1,padx=10,pady=10)
    combo_search=ttk.Combobox(detail_frame,width=10,font=('times of roman',15,"bold"),state="readonly")
    combo_search['values']=("","ID","NAME")
    combo_search.grid(row=0,column=2,padx=10,pady=10)
    combo_search.current(0)
    txt1=Entry(detail_frame,width=12,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt1.grid(row=0,column=3,padx=10,pady=10)

    #-----------------------------Detail Frame Buttons---------------

    search_btn=Button(detail_frame,text='Serach',command=search,width=15,height=1).grid(row=0,column=5,padx=10,pady=10)
    showall_btn=Button(detail_frame,text='Show All',command=fetch_data,width=15,height=1).grid(row=0,column=6,padx=10,pady=10)

    #------------------------------Table Frame------------
    table_frame = Frame(detail_frame,bd=4,relief=RIDGE,bg="#3D3C3A")
    table_frame.place(x=10,y=50,width=1190,height=260)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    Medicine_table=ttk.Treeview(table_frame,columns=("ID","NAME","PRICE","QUANTITY","CATEGORY"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Medicine_table.xview)
    scroll_y.configure(command=Medicine_table.yview)
    Medicine_table.heading("ID",text="ID")
    Medicine_table.heading("NAME",text="NAME")
    Medicine_table.heading("PRICE",text="PRICE")
    Medicine_table.heading("QUANTITY",text="QUANTITY")
    Medicine_table.heading("CATEGORY",text="CATEGORY")

    Medicine_table['show']='headings'
    Medicine_table.column("ID",width=100)
    Medicine_table.column("NAME",width=100)
    Medicine_table.column("PRICE",width=100)
    Medicine_table.column("QUANTITY",width=100)
    Medicine_table.column("CATEGORY",width=100)
    Medicine_table.pack(fill=BOTH,expand=1)
    Medicine_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()


    root.mainloop()

#managemedicine()