from tkinter import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
import sqlite3



def sellitem():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="" or entry6.get()=="" or entry7.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("pharmacy.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM MEDICINE WHERE ID=? AND NAME=? ''',(entry1.get(),entry2.get()))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("ERROR","Medicine Not Registered In This System,Register First in ManageMedicine or Invalid Medicine Name or ID")
                root.destroy()
            else:
                if int(row[3])==0:
                    messagebox.showerror("Error","No Stock")
                    root.destroy()
                elif int(entry6.get())<=int(row[3]):
                    cur.execute('''CREATE TRIGGER IF NOT EXISTS DELETEQUANTITY AFTER INSERT ON SELLMEDICINE FOR EACH ROW BEGIN UPDATE MEDICINE SET QUANTITY=QUANTITY-new.QUANTITY WHERE ID=new.MEDICINE_ID ; END''')
                    cur.execute('''INSERT INTO SELLMEDICINE (MEDICINE_ID,MEDICINE_NAME,CUSTOMER_NAME,CONTACT,DATE,QUANTITY,AMOUNT) VALUES (?,?,?,?,?,?,?)''',(entry1.get(),entry2.get(),entry3.get(),entry4.get(),entry5.get(),entry6.get(),entry7.get()))
                    con.commit()
                    con.close()
                    fetch_data()
                    messagebox.showinfo("Success","Medicine Sold Successfully")
                    root.destroy()
                else:
                    messagebox.showerror("Error","No Sufficient Stock")
                    root.destroy()
        except Exception as es:
            messagebox.showerror("Error due to:{str(es)}")
            root.destroy()

def returnitem():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="" or entry6.get()=="" or entry7.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("pharmacy.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM MEDICINE WHERE ID=? AND NAME=? ''',(entry1.get(),entry2.get()))
            row=cur.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("ERROR","Medicine Not Registered In This System,Register First in ManageMedicine or Invalid Medicine Name or ID")
                root.destroy()
            else:
                cur.execute('''SELECT * FROM SELLMEDICINE WHERE MEDICINE_ID=? AND MEDICINE_NAME=? ''',(entry1.get(),entry2.get()))
                row=cur.fetchone()
                #print(row)
                cur.execute('''DELETE FROM SELLMEDICINE WHERE TRANSACTIONID=?''',((row[0]),))
                cur.execute('''UPDATE MEDICINE SET QUANTITY=QUANTITY+? WHERE ID=?''',(entry6.get(),entry1.get()))
                
                con.commit()
                con.close()
                fetch_data()
                messagebox.showinfo("Success","RETURNED Successfully")
                root.destroy()
        except Exception as es:
            messagebox.showerror("Error due to:{str(es)}")
            root.destroy()


    




    

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0,END)
    entry7.delete(0,END)

def search():
    try:
        con = sqlite3.connect('pharmacy.sqlite')
        cur = con.cursor()
        cur.execute("SELECT * FROM SELLMEDICINE WHERE "+str(combo_search.get())+" LIKE '%"+str(txt1.get())+"%' ORDER BY TRANSACTIONID DESC" )
        rows=cur.fetchall()
        if len(rows)!=0:
            SellMedicine_table.delete(*SellMedicine_table.get_children())
            for row in rows:
                SellMedicine_table.insert('',END,values=row)
                con.commit()
        con.close()
        clearsearch()
    except Exception as es:
        messagebox.showerror("Error Due To:{str(es)}")
        clearsearch()

def fetch_data():
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM SELLMEDICINE ORDER BY TRANSACTIONID DESC''')
    rows=cur.fetchall()
    if len(rows)!=0:
        SellMedicine_table.delete(*SellMedicine_table.get_children())
        for row in rows:
            SellMedicine_table.insert('',END,values=row)
            conn.commit()
    conn.close()

def get_cursor(ev):                              
    curosor_row=SellMedicine_table.focus()                      
    contents=SellMedicine_table.item(curosor_row)   
    row=contents['values']
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry1.insert(0, (row[1]))
    entry2.insert(0, (row[2]))
    entry3.insert(0, (row[3]))
    entry4.insert(0, (row[4]))
    entry5.insert(0, (row[5]))
    entry6.insert(0, (row[6]))
    entry7.insert(0, (row[7]))

def clearsearch():
    combo_search.current(0)
    txt1.delete(0,END)

def total():
    if  entry1.get()==""  or entry2.get()=="" or entry3.get()=="" or entry4.get()==""  or entry5.get()=="" or entry6.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
    else:
        try:
            conn = sqlite3.connect('pharmacy.sqlite')
            cur = conn.cursor()
            cur.execute('''SELECT PRICE FROM MEDICINE WHERE ID=? AND NAME=?''',(entry1.get(),entry2.get()))
            price=cur.fetchone()
            print(price)
            conn.commit
            conn.close()
    
            total=int(price[0])*int(entry6.get())
            entry7.delete(0,END)
            entry7.insert(0,str(total))
        except Exception as es:
            messagebox.showerror("Error Due To:{str(es)}")
            clearsearch()


def sellmedicine():
    global root,entry1,entry2,entry3,entry4,entry5,entry6,txt1,combo_search,SellMedicine_table,entry7
    conn = sqlite3.connect('pharmacy.sqlite')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS SELLMEDICINE(TRANSACTIONID INTEGER PRIMARY KEY AUTOINCREMENT,MEDICINE_ID NUMBER,MEDICINE_NAME TEXT,CUSTOMER_NAME TEXT,CONTACT NUMBER,DATE TEXT,QUANTITY NUMBER,AMOUNT NUMBER)''')
    conn.commit()
    conn.close()

    root = Tk()
    root.title("Sell Medicine Window")
    root.geometry("1300x700+0+0")
    root.configure(bg='BLACK')

    label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("Times", 30))
    label1=Label(root,text="MEDICINE ID",bg="red",relief="ridge",fg="white",font=("Times", 12),width=25)
    entry1=Entry(root , font=("Times", 12))
    label2=Label(root, text="MEDICINE NAME",bd="2",relief="ridge",height="1",bg="red",fg="white", font=("Times", 12),width=25)
    entry2= Entry(root, font=("Times", 12))
    label3=Label(root, text="CUSTOMER_NAME",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
    entry3= Entry(root, font=("Times", 12))
    label4=Label(root, text="CONTACT",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
    entry4= Entry(root, font=("Times", 12))
    label5=Label(root, text="DATE",bg="red",relief="ridge",fg="white", font=("Times", 12),width=25)
    entry5= DateEntry(root, font=("Times", 12),width=18)
    label6=Label(root, text="Quantity",bd="2",relief="ridge",bg="red",fg="white", font=("Times", 12),width=25)
    entry6= Entry(root, font=("Times", 12))

    button1= Button(root, text="SELL ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=sellitem)
    button2= Button(root, text="CLEAR SCREEN", bg="white", fg="black", width=20, font=("Times", 12),command=clearitem)
    button3= Button(root, text="RETURN ITEM", bg="white", fg="black", width=20, font=("Times", 12),command=returnitem)
    button4= Button(root, text="COMPUTE TOTAL", bg="white", fg="black", width=20, font=("Times", 12),command=total)

    label0.grid(columnspan=6, padx=10, pady=10)
    label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
    label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
    label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
    label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
    label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
    label6.grid(row=6,column=0, sticky=W, padx=10, pady=10)
    entry1.grid(row=1,column=1, padx=40, pady=10)
    entry2.grid(row=2,column=1, padx=10, pady=10)
    entry3.grid(row=3,column=1, padx=10, pady=10)
    entry4.grid(row=4,column=1, padx=10, pady=10)
    entry5.grid(row=5,column=1, padx=10, pady=10)
    entry6.grid(row=6,column=1, padx=10, pady=10)
    button1.grid(row=1,column=4, padx=40, pady=10)
    button2.grid(row=1,column=5, padx=40, pady=10)
    button3.grid(row=2,column=4, padx=40, pady=10)
    button4.grid(row=3,column=4, padx=40, pady=10)

    logout_btn=Button(root,text="Quit",command=root.destroy,bg="purple",relief="ridge",fg="white",bd=3,font=("Times", 12),width=20,cursor="hand2").place(x=1100,y=25)

    #-------Total Computation------
    label7=Label(root, text="Total",bd="2",relief="ridge",bg="green",fg="white", font=("Times", 12),width=29)
    entry7= Entry(root, font=("Times", 12))
    label7.grid(row=5,column=4, sticky=W, padx=10, pady=10)
    entry7.grid(row=6,column=4, padx=40, pady=10)

    




    #----------------------------Detail Frame-------------------
    detail_frame = Frame(root,bd=4,relief=RIDGE,bg="white")
    detail_frame.place(x=40,y=370,width=1220,height=330)

    lb1=Label(detail_frame,text="Search By",font=('times of roman',15,"bold"),bg="white",fg="BLACK").grid(row=0,column=1,padx=10,pady=10)
    combo_search=ttk.Combobox(detail_frame,width=10,font=('times of roman',15,"bold"),state="readonly")
    combo_search['values']=("","TRANSACTIONID","MEDICINE_ID","MEDICINE_NAME")
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
    SellMedicine_table=ttk.Treeview(table_frame,columns=("TRANSACTIONID","MEDICINE_ID","MEDICINE_NAME","CUSTOMER_NAME","CONTACT","DATE","QUANTITY","AMOUNT"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.configure(command=SellMedicine_table.xview)
    scroll_y.configure(command=SellMedicine_table.yview)
    SellMedicine_table.heading("TRANSACTIONID",text="TRANSACTIONID")
    SellMedicine_table.heading("MEDICINE_ID",text="MEDICINE_ID")
    SellMedicine_table.heading("MEDICINE_NAME",text="MEDICINE_NAME")
    SellMedicine_table.heading("CUSTOMER_NAME",text="CUSTOMER_NAME")
    SellMedicine_table.heading("CONTACT",text="CONTACT")
    SellMedicine_table.heading("DATE",text="DATE")
    SellMedicine_table.heading("QUANTITY",text="QUANTITY")
    SellMedicine_table.heading("AMOUNT",text="AMOUNT")
    

    SellMedicine_table['show']='headings'
    SellMedicine_table.column("TRANSACTIONID",width=100)
    SellMedicine_table.column("MEDICINE_ID",width=100)
    SellMedicine_table.column("MEDICINE_NAME",width=100)
    SellMedicine_table.column("CUSTOMER_NAME",width=100)
    SellMedicine_table.column("CONTACT",width=100)
    SellMedicine_table.column("DATE",width=100)
    SellMedicine_table.column("QUANTITY",width=100)
    SellMedicine_table.column("AMOUNT",width=100)
    SellMedicine_table.pack(fill=BOTH,expand=1)
    SellMedicine_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()


    root.mainloop()

#sellmedicine()