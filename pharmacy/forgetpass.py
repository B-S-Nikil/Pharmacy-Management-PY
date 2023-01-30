from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox


def forgetpass():
    global root,txt_email,cmb_quest,txt_answer,txt_password,txt_cpassword
    root=Tk()
    root.configure(bg="brown")
    root.title("Forgot Password Window")
    root.geometry("1350x700+0+0")
    root.maxsize(width=1350,height=700)


    main_title=Label(root,text="Forgot Password Page",font=("times new roman",25,"bold"),bg="white",fg="red").place(x=0,y=0,width=1350)

    title=Label(root,text="Pharmacy Management",font=("times new roman",25,"bold"),bg="brown",fg="yellow").place(x=510,y=55)

        
    #===Entry Frame===
    frame1=Frame(root,bg="white")
    frame1.place(x=350,y=130,width=700,height=500)

        #-----Entry Fields-----
    title=Label(frame1,text="Enter The Required Details To Change Password",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
       
    email=Label(frame1,text="EMAIL ADDRESS:",font=("times new roman",15,"bold"),bg="white",fg="brown").place(x=100,y=100)
    txt_email=Entry(frame1,font=("times new roman",15),bd=2,relief=RIDGE,bg="light gray")
    txt_email.place(x=340,y=100,width=250)

    question=Label(frame1,text="SECURITY QUESTION:",font=("times new roman",15,"bold"),bg="white",fg="brown").place(x=100,y=150)
        
    cmb_quest=ttk.Combobox(frame1,font=("times new roman",15),state='readonly',justify=CENTER) 
    cmb_quest['values']=("","YOUR FAVOURITE PET","YOUR BIRTH PLACE","YOUR FRIEND NAME")
    cmb_quest.place(x=340,y=150,width=250)
    cmb_quest.current(0)

    answer=Label(frame1,text="ANSWER:",font=("times new roman",15,"bold"),bg="white",fg="brown").place(x=110,y=200)
    txt_answer=Entry(frame1,font=("times new roman",15),bd=2,relief=RIDGE,bg="light gray")
    txt_answer.place(x=340,y=200,width=250)

    password=Label(frame1,text="NEW PASSWORD:",font=("times new roman",15,"bold"),bg="white",fg="brown").place(x=100,y=250)
    txt_password=Entry(frame1,font=("times new roman",15),bd=2,relief=RIDGE,bg="light gray")
    txt_password.place(x=340,y=250,width=250)

    cpassword=Label(frame1,text="CONFIRM PASSWORD:",font=("times new roman",15,"bold"),bg="white",fg="brown").place(x=100,y=300)
    txt_cpassword=Entry(frame1,font=("times new roman",15),bd=2,relief=RIDGE,bg="light gray")
    txt_cpassword.place(x=340,y=300,width=250)

        #--------Button--------
    btn=Button(frame1,text="CONFIRM",font=("times new roman",20,"bold"),command=change_pass,bd=3,bg="green",fg="white",cursor="hand2")
    btn.place(x=200,y=350,width=300,height=50)

    btn=Button(frame1,text="QUIT",font=("times new roman",20,"bold"),command=root.destroy,bd=3,bg="grey",fg="white",cursor="hand2")
    btn.place(x=200,y=420,width=300,height=50)

    root.mainloop()


def change_pass():
    if  txt_email.get()==""  or cmb_quest.get()=="" or txt_answer.get()=="" or txt_password.get()=="" or txt_cpassword.get()=="":
        messagebox.showerror("ERROR","All Fields Are Required")
        root.destroy()
    elif txt_password.get()!=txt_cpassword.get():
        messagebox.showerror("ERROR","Password and Confirm Password Must Be Same")
        root.destroy()
    else:
        try:
            con=sqlite3.connect("pharmacy.sqlite")
            cur=con.cursor()
            cur.execute('''SELECT * FROM STAFF WHERE EMAIL=?''',(txt_email.get(),))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("ERROR","Invalid E-mail Address")
                clear()
                root.destroy()
            else:
                if row[5]==cmb_quest.get() and row[6]==txt_answer.get():
                    cur.execute('''UPDATE STAFF SET PASSWORD=? WHERE EMAIL=?''',
                    ( 
                    txt_password.get(),
                    txt_email.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Password Changed Sucessfully")
                    clear()
                    root.destroy()
                else:
                    messagebox.showerror("ERROR","Incorrect Security Question and Answer")
                    clear()
                    root.destroy()

        except Exception as es:
            messagebox.showerror("Error due to: {str(es)}")
            root.destroy()
               

def clear():
    txt_email.delete(0,END)
    cmb_quest.current(0)
    txt_answer.delete(0,END)
    txt_password.delete(0,END)
    txt_cpassword.delete(0,END)


#forgetpass()