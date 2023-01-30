from tkinter import * 
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkcalendar import *
def managestaff():
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS STAFF (ID NUMBER PRIMARY KEY,NAME TEXT,CONTACT NUMBER,EMAIL TEXT,GENDER TEXT,QUESTION TEXT,ANSWER TEXT,PASSWORD TEXT)''')
    global root,txt1,txt2,txt3,txt4,txt7,txt8,cmb_gender,cmb_quest,combo_search,d_txt1,Manage_table
    root=Tk()
    root.title("Manage Staff Window")
    root.geometry("1350x700+0+0")
    root.maxsize(width=1350,height=700)

    #----------------Initial Heading-------------------------------

    title=Label(root,text="Staff Details",bd=10,relief=GROOVE,font=('times of roman',40,"bold"),bg="light green",fg="red")
    title.pack(side=TOP,fill=X)
    logout_btn=Button(root,text='QUIT',width=10,command=root.destroy,font=('times of roman',18,"bold"),bd=4,cursor="hand2",bg="grey",fg="white").place(x=1100,y=13)

    #-----------Entry Frame-----------
    manage_frame = Frame(root,bd=4,relief=RIDGE,bg="orange")
    manage_frame.place(x=20,y=100,width=500,height=590)
    m_title=Label(manage_frame,text="MANAGE STAFF",font=('times of roman',25,"bold"),bg="orange",fg="white")
    m_title.grid(row=0,columnspan=2,pady=10,sticky="w")

    lb1=Label(manage_frame,text="ID",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb1.grid(row=1,column=0,pady=5,padx=20,sticky="w")
    txt1=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt1.grid(row=1,column=1,pady=5,padx=20,sticky="w")

    lb2=Label(manage_frame,text="NAME",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb2.grid(row=2,column=0,pady=5,padx=20,sticky="w")
    txt2=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt2.grid(row=2,column=1,pady=5,padx=20,sticky="w")

    lb3=Label(manage_frame,text="CONTACT",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb3.grid(row=3,column=0,pady=5,padx=20,sticky="w")
    txt3=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt3.grid(row=3,column=1,pady=5,padx=20,sticky="w")

    lb4=Label(manage_frame,text="EMAIL",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb4.grid(row=4,column=0,pady=5,padx=20,sticky="w")
    txt4=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt4.grid(row=4,column=1,pady=5,padx=20,sticky="w")


    lb5=Label(manage_frame,text="GENDER",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb5.grid(row=5,column=0,pady=5,padx=20,sticky="w")
    cmb_gender=ttk.Combobox(manage_frame,font=("times new roman",15,"bold"),state='readonly',justify=CENTER)
    cmb_gender['values']=("","Male","Female","Others")
    cmb_gender.grid(row=5,column=1,pady=5,padx=20,sticky="w")
    cmb_gender.current(0)

    lb6=Label(manage_frame,text="QUESTION",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb6.grid(row=6,column=0,pady=5,padx=20,sticky="w")
    cmb_quest=ttk.Combobox(manage_frame,font=("times new roman",15,"bold"),state='readonly',justify=CENTER) 
    cmb_quest['values']=("","YOUR FAVOURITE PET","YOUR BIRTH PLACE","YOUR FRIEND NAME")
    cmb_quest.grid(row=6,column=1,pady=5,padx=20,sticky="w")
    cmb_quest.current(0)
        
    lb7=Label(manage_frame,text="ANSWER",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb7.grid(row=7,column=0,pady=5,padx=20,sticky="w")
    txt7=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt7.grid(row=7,column=1,pady=5,padx=20,sticky="w")

    lb8=Label(manage_frame,text="PASSWORD",font=('times of roman',20,"bold"),bg="orange",fg="white")
    lb8.grid(row=8,column=0,pady=5,padx=20,sticky="w")
    txt8=Entry(manage_frame,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    txt8.grid(row=8,column=1,pady=5,padx=20,sticky="w")
    #-------------------------------Manage Frame Buttons---------------------------

    addbtn=Button(manage_frame,text='Add',width=10,command=add_staff).place(x=20,y=550)
    delbtn=Button(manage_frame,text='Delete',width=10,command=delete_staff).place(x=140,y=550)
    updbtn=Button(manage_frame,text='Update',width=10,command=update_staff).place(x=260,y=550)
    clrbtn=Button(manage_frame,text='Clear',width=10,command=clear).place(x=380,y=550)



    #----------------------------Detail Frame-------------------
    detail_frame = Frame(root,bd=4,relief=RIDGE,bg="#3D3C3A")
    detail_frame.place(x=540,y=100,width=800,height=580)

    d_lb1=Label(detail_frame,text="Search By",font=('times of roman',15,"bold"),bg="#3D3C3A",fg="white").grid(row=0,column=1,padx=10,pady=10)
    combo_search=ttk.Combobox(detail_frame,width=10,font=('times of roman',15,"bold"),state="readonly")
    combo_search['values']=("","NAME","EMAIL","Contact")
    combo_search.grid(row=0,column=2,padx=10,pady=10)
    combo_search.current(0)
    d_txt1=Entry(detail_frame,width=12,bd=3,relief=GROOVE,font=('times of roman',15,"bold"))
    d_txt1.grid(row=0,column=3,padx=10,pady=10)

    #-----------------------------Detail Frame Buttons---------------

    search_btn=Button(detail_frame,text='Serach',command=search,width=15,height=1).grid(row=0,column=5,padx=10,pady=10)
    showall_btn=Button(detail_frame,text='Show All',command=fetch_staffdata,width=15,height=1).grid(row=0,column=6,padx=10,pady=10)

        #------------------------------Table Frame------------
    table_frame = Frame(detail_frame,bd=4,relief=RIDGE,bg="#3D3C3A")
    table_frame.place(x=10,y=70,width=760,height=470)

    scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    Manage_table=ttk.Treeview(table_frame,columns=("ID","NAME","CONTACT","EMAIL","GENDER","QUESTION","ANSWER","PASSWORD"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=Manage_table.xview)
    scroll_y.configure(command=Manage_table.yview)
    Manage_table.heading("ID",text="ID")
    Manage_table.heading("NAME",text="NAME")
    Manage_table.heading("CONTACT",text="CONTACT")
    Manage_table.heading("EMAIL",text="EMAIL")
    Manage_table.heading("GENDER",text="GENDER")
    Manage_table.heading("QUESTION",text="QUESTION")
    Manage_table.heading("ANSWER",text="ANSWER")
    Manage_table.heading("PASSWORD",text="PASSWORD")
    Manage_table['show']='headings'
    Manage_table.column("ID",width=100)
    Manage_table.column("NAME",width=100)
    Manage_table.column("CONTACT",width=100)
    Manage_table.column("EMAIL",width=100)
    Manage_table.column("GENDER",width=100)
    Manage_table.column("QUESTION",width=100)
    Manage_table.column("ANSWER",width=100)
    Manage_table.column("PASSWORD",width=100)
    Manage_table.pack(fill=BOTH,expand=1)
    Manage_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_staffdata()


    root.mainloop()
        

def add_staff():
    if txt1.get()=="" or txt2.get()=="" or txt3.get()=="" or txt4.get()=="" or cmb_gender.get()=="" or cmb_quest.get()=="" or txt7.get()=="" or txt8.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("pharmacy.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM STAFF WHERE EMAIL=?''',(txt4.get(),))
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","User already exists!")
                clear()
                root.destroy()
            else:
                cur.execute('''INSERT INTO STAFF VALUES (?,?,?,?,?,?,?,?)''',
                (txt1.get(), 
                txt2.get(), 
                txt3.get(),
                txt4.get(),
                cmb_gender.get(),
                cmb_quest.get(),
                txt7.get(),
                txt8.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Registered Sucessfully")
                fetch_staffdata()
                root.destroy()

        except Exception as es:
            messagebox.showerror("Error due to: {str(es)}")
            root.destroy()



def fetch_staffdata():
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM STAFF''')
    rows=cur.fetchall()
    if len(rows)!=0:
        Manage_table.delete(*Manage_table.get_children())
        for row in rows:
            Manage_table.insert('',END,values=row)
            conn.commit()
    conn.close()

def clear():
    txt1.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0,END)
    txt4.delete(0,END)
    txt7.delete(0,END)
    txt8.delete(0,END)
    cmb_gender.current(0)
    cmb_quest.current(0)

    combo_search.current(0)
    d_txt1.delete(0,END)
        
        

def update_staff():
    try:
        if (txt1.get()=="") or (txt2.get()=="") or (txt3.get()=="") or (txt4.get()=="") or (cmb_gender.get()=="") or (cmb_quest.get()=="") or (txt7.get()=="") or (txt8.get()=="") :
            messagebox.showerror("Error","All fields are required!!!")
            root.destroy()
        else:
            conn = sqlite3.connect('pharmacy.sqlite')
            cur = conn.cursor()
            cur.execute('''UPDATE STAFF SET ID=?,NAME=?,CONTACT=?,EMAIL=?,GENDER=?,QUESTION=?,ANSWER=?,PASSWORD=? WHERE ID=? AND EMAIL=?''',(txt1.get(),
                                                                        txt2.get(),
                                                                        txt3.get(),
                                                                        txt4.get(),
                                                                        cmb_gender.get(),
                                                                        cmb_quest.get(),
                                                                        txt7.get(),
                                                                        txt8.get(),
                                                                        txt1.get(),
                                                                        txt4.get(),
                                                                        ))
            conn.commit()
            fetch_staffdata()
            messagebox.showinfo("Upated","Record Updated Successfully")
            clear()
            conn.close()
            root.destroy()
    except Exception as es:
        messagebox.showerror("Error due to:{str(es)}")
        root.destroy()

def get_cursor(ev):                              
    curosor_row=Manage_table.focus()                        
    contents=Manage_table.item(curosor_row)   
    row=contents['values']
    txt1.delete(0,END)
    txt1.insert(0,row[0])
    txt2.delete(0,END)
    txt2.insert(0,row[1])
    txt3.delete(0,END)
    txt3.insert(0,row[2])
    txt4.delete(0,END)
    txt4.insert(0,row[3])
    cmb_gender.set(row[4])
    cmb_quest.set(row[5])
    txt7.delete(0,END)
    txt7.insert(0,row[6])
    txt8.delete(0,END)
    txt8.insert(0,row[7])
        

def delete_staff():
    try:
        conn = sqlite3.connect('pharmacy.sqlite')
        cur = conn.cursor()
        cur.execute('''DELETE FROM STAFF WHERE ID=? AND EMAIL=?''', (txt1.get(),txt4.get(),))
        conn.commit()
        fetch_staffdata()
        messagebox.showinfo("Deleted","Record Deleted Successfully")
        clear()
        conn.close()
        root.destroy()
    except Exception as es:
        messagebox.showerror("Error due to:{str(es)}")
        root.destroy()


def search():
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute("SELECT * FROM STAFF WHERE "+str(combo_search.get())+" LIKE '%"+str(d_txt1.get())+"%'" )
    rows=cur.fetchall()
    if len(rows)!=0:
        Manage_table.delete(*Manage_table.get_children())
        for row in rows:
            Manage_table.insert('',END,values=row)
            conn.commit()
    conn.close()
    clear()

#managestaff()