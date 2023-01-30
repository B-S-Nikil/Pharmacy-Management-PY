from tkinter import*
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from adminpage import *
from staffpage import *
from forgetpass import *
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login page")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="orange")

        self.role_var=StringVar()
    
        #==left bg colour==========
        left_lbl=Label(self.root,bg="blue",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        
        #====Frame=============
        login_Frame=Frame(self.root,bg="cyan")
        login_Frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_Frame,text="LOGIN",font=("Helvetica",35,"bold"),bg="cyan",fg="purple").place(x=20,y=50)
        
        role_lb=Label(login_Frame,text="LOGIN AS:",font=('arial',20,"bold"),bg="cyan",fg="dark blue")
        role_lb.place(x=20,y=150)
        self.combo_role=ttk.Combobox(login_Frame,textvariable=self.role_var,font=('verdena',20,"bold"),state="readonly")
        self.combo_role['values']=("Admin","Staff")
        self.combo_role.place(x=250,y=150,width=270,height=35)

        email=Label(login_Frame,text="EMAIL ADDRESS",font=("arial",20,"bold"),bg="cyan",fg="dark blue").place(x=20,y=200)
        self.txt_email=Entry(login_Frame,font=("times new roman",13),bg="white",fg="black")
        self.txt_email.place(x=250,y=200,width=280,height=35)

        
        pass_=Label(login_Frame,text="PASSWORD",font=("arial",20,"bold"),bg="cyan",fg="dark blue").place(x=20,y=250)
        self.txt_pass_=Entry(login_Frame,font=("times new roman",13),bg="white",fg="black")
        self.txt_pass_.place(x=250,y=250,width=280,height=35)

                                                    #==Button=========
        #===Signup button==
        btn_reg=Button(login_Frame,text="Login",command=self.login,font=("times new roman",18,"bold"),bg="#B00857",fg="cyan",cursor="hand2")
        btn_reg.place(x=260,y=350,width=180,height=40)
        #===Login button===
        btn_reg=Button(login_Frame,text="Forget Password",command=self.forget_pass,font=("times new roman",18,"bold"),bg="green",fg="cyan",cursor="hand2")
        btn_reg.place(x=260,y=400,width=180,height=40)
        #===Login button===
        btn_reg=Button(login_Frame,text="Quit",command=self.root.destroy,font=("times new roman",18,"bold"),bg="red",fg="cyan",cursor="hand2")
        btn_reg.place(x=260,y=450,width=180,height=40)

    def login(self):
        if self.role_var.get()=="" or self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                if self.role_var.get()=="Admin":
                    if self.txt_email.get()=="admin123@gmail.com" and self.txt_pass_.get()=="1234":
                        messagebox.showinfo("Success","Welcome Admin")
                        self.root.destroy()
                        adminpage()
                        
                    else:
                        messagebox.showerror("Error","Invalid E-mail or Password")
                if self.role_var.get()=="Staff":
                    con=sqlite3.connect("pharmacy.sqlite")
                    cur=con.cursor()
                    cur.execute('''SELECT * FROM STAFF WHERE EMAIL=? and PASSWORD=?''',(self.txt_email.get(),self.txt_pass_.get(),))
                    row=cur.fetchone()
                    if row==None:
                        messagebox.showerror("ERROR","Invalid E-mail or Password")
                    else:
                        messagebox.showinfo("Success","Welcome To Pharmacy Management System "+str(self.txt_email.get()))
                        self.root.destroy()
                        staffpage()
                       
            except Exception as es:
                messagebox.showerror("Error Due to:{str(es)}",parent=self.root)
        
   
 


    def forget_pass(self):
        forgetpass()


root=Tk()
obj=login_window(root)
root.mainloop()   


