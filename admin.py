# ==============Importing Packages =================
# ==============Importing Packages =================

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk,  ImageDraw
import os 
import webbrowser
import sys
import sqlite3
from datetime import datetime
import smtplib
from email.message import EmailMessage
from validate_email import validate_email
from datetime import datetime
import random
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code


        

class win1:
    def __init__(self, root):
            self.root = root
            root.geometry("1360x768+0+0")
            root.config(bg="#6ACD32")
            root.title("Login Form".center(420))
            root.resizable(False, False)
            photo = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
            root.iconphoto(False, photo)
            #root.iconbitmap('Pics/bakeryicon.ico')

# ====================== Icons ==============================
# ====================== Icons ==============================
# ====================== Icons ==============================
# ====================== Icons ==============================

            self.bg = ImageTk.PhotoImage(file="Pics/x1r4Ao.png") 
            self.icon = ImageTk.PhotoImage(file="Pics/Bakery.jpg")
            self.icon2= ImageTk.PhotoImage(file="Pics/baker.png")
            self.logo= ImageTk.PhotoImage(file="Pics/logo.jpeg")
            self.fb_icon = ImageTk.PhotoImage(file="Pics/facebook.jpg")
            self.insta_icon = ImageTk.PhotoImage(file="Pics/instagram.jpg")
            self.gmail_icon = ImageTk.PhotoImage(file="Pics/gmail.jpg")
            self.twitter_icon = ImageTk.PhotoImage(file="Pics/twitter.png")
            self.email_icon = ImageTk.PhotoImage(file="Pics/email.png")
            self.pass_icon = ImageTk.PhotoImage(file="Pics/unlock-128.png")
            self.name_icon = ImageTk.PhotoImage(file="Pics/namecard-128.png")
            self.me_icon = ImageTk.PhotoImage(file = "Pics/Me.png")
            self.showpass_icon = ImageTk.PhotoImage(file = "Pics/show-password.png")
            self.subframe_icon = ImageTk.PhotoImage(file = "Pics/Frame_bg.jpg")
            self.register_icon = ImageTk.PhotoImage(file = "Pics/register-button-png-11-e1581365812416.png")

            self.img_bg = Label(self.root, image = self.bg)
            self.img_bg.place(x=0, y=0)

# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
            
            
            self.RightSubFrame = Frame(self.root, relief=FLAT, bd=6,bg="#B80F0A")
            self.RightSubFrame.place(x=470, y=120, width=400, height=500)


            self.RightSubFrame_lbl1= Label(self.RightSubFrame, fg="#FFFF33",text="As Admin",font=("times new roman",18,"bold"),bg= "#B80F0A")
            self.RightSubFrame_lbl1.place(x=10, y=50)

            self.img_RSF1 = Label(self.RightSubFrame, bg="#B80F0A",image = self.me_icon)
            self.img_RSF1.place(x=150, y=10)

            self.RightSubFrame_lbl2= Label(self.RightSubFrame, fg="#FFFF33",text="Sign In",font=("times new roman",18,"bold"),bg= "#B80F0A")
            self.RightSubFrame_lbl2.place(x=290, y=50)

            self.RightSubFrame_lbl3= Label(self.RightSubFrame, fg="#e5b4ff",text="Owner: Aditya Jha",font=("times new roman",10),bg= "#B80F0A")
            self.RightSubFrame_lbl3.place(x=150, y=110)

            self.img_RSF2 = Label(self.RightSubFrame, image = self.email_icon, bg="#B80F0A")
            self.img_RSF2.place(x=10, y=130)


            self.email_entry = Entry(self.RightSubFrame, bg="#B80F0A", fg="#FFFFFF",font=("times new roman",20), bd=2)
            self.email_entry.place(x=70, y=140)
            self.email_entry.insert(0,"Email")

            self.img_RSF3 = Label(self.RightSubFrame, image = self.pass_icon, bg="#B80F0A")
            self.img_RSF3.place(x=10, y=210)

            self.pass_lbl = Label(self.RightSubFrame, text="Password",  fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A")
            self.pass_lbl.place(x=12, y=270)

            self.pass_entry = Entry(self.RightSubFrame,show=".", bg="#B80F0A", fg="#FFFFFF",font=("times new roman",20), bd=2)
            self.pass_entry.place(x=70, y=220,width=240)
            self.pass_entry.insert(0,"********")

            separator1 = ttk.Separator(self.RightSubFrame, orient='horizontal')
            separator1.place(x=10,width=140,y=360)
            
            self.Seprator_lbl1 = Label(self.RightSubFrame, text="Follow Us On",  fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A")
            self.Seprator_lbl1.place(x=160, y=350)

            separator2 = ttk.Separator(self.RightSubFrame, orient='horizontal')
            separator2.place(x=250,width=130,y=360)

            self.Seprator_lbl2 = Label(self.RightSubFrame, text="Developed By Aditya Jha",  fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A")
            self.Seprator_lbl2.place(x=130, y=455)

            
        # =================== Buttons ================================
            
            self.ButtonRSF_1 = Button(self.RightSubFrame,bd=0, image = self.showpass_icon,activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.show)
            self.ButtonRSF_1.place(x=320, y=215)

            self.ButtonRSF_2 = Button(self.RightSubFrame, bd=0,text="Forget Password", activebackground="#B80F0A", fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A",cursor="hand2",command=self.forget)
            self.ButtonRSF_2.place(x=150, y=270)

            self.ButtonRSF_3 = Button(self.RightSubFrame,bd=0, text="Sign In",font=("times new roman",20,"bold"), activebackground="white",bg="white",cursor="hand2", command=self.signin)
            self.ButtonRSF_3.place(x=70, y=300, width=290,height=30)

            self.ButtonRSF_4 = Button(self.RightSubFrame,bd=0, image = self.fb_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link1)
            self.ButtonRSF_4.place(x=20, y=400)

            self.ButtonRSF_5 = Button(self.RightSubFrame,bd=0, image = self.gmail_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link3)
            self.ButtonRSF_5.place(x=130, y=400)

            self.ButtonRSF_6 = Button(self.RightSubFrame,bd=0, image = self.insta_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link3)
            self.ButtonRSF_6.place(x=230, y=400)

            self.ButtonRSF_7 = Button(self.RightSubFrame,bd=0, image = self.twitter_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link4)
            self.ButtonRSF_7.place(x=320, y=400)

            self.ButtonRSF_8 = Button(self.root, relief=GROOVE,bd=5,text="Back", font=("times new roman",20,"bold"),activebackground="blue",bg="blue",activeforeground="#FFFFFF",fg="#FFFFFF",cursor="hand2", command=self.back)
            self.ButtonRSF_8.place(x=20, y=20)

            self.pass_l = StringVar()
            self.pass_lbl = Entry(self.RightSubFrame, font=(
            "time new roman", 10), textvariable=self.pass_l, fg="white", bg="black").place(x=10, y=10)
            self.pass_l.set("Password Mode: Hidden")


            now = datetime.now()
            self.Time1 = now.strftime('%H:%M:%S')
            self.date = now.strftime("%d-%b-%Y")

    def back(self):
        self.root.destroy()
        import logine

    def user(self):
        self.root.destroy()
        import loginu

    def admin(self):
        self.root.destroy()
        import admin

    
    def link1(self):
        webbrowser.open_new("http://www.facebook.com")

    def link2(self):
        webbrowser.open_new("http://www.gmail.com")
    
    def link3(self):
        webbrowser.open_new("https://www.instagram.com/?hl=en")
   
    def link4(self):
        webbrowser.open_new("http://www.twitter.com")
    
    
    def show(self):
        a = self.pass_entry.get()
        self.pass_entry = Entry(self.RightSubFrame,show=".", bg="#B80F0A", fg="#FFFFFF",font=("times new roman",20), bd=2)
        self.pass_entry.place(x=70, y=220,width=240)
        self.pass_entry.insert(0, a)
        if self.pass_l.get() == "Password Mode: Hidden":
            self.pass_l.set("Password Mode: Shown")
            self.pass_entry = Entry(self.RightSubFrame, bg="#B80F0A", fg="#FFFFFF",font=("times new roman",20), bd=2)
            self.pass_entry.place(x=70, y=220,width=240)  
            self.pass_entry.insert(0, a)

        elif self.pass_l.get() == "Password Mode: Shown":
            self.pass_l.set("Password Mode: Hidden")
            self.pass_entry = Entry(self.RightSubFrame,show=".", bg="#B80F0A", fg="#FFFFFF",font=("times new roman",20), bd=2)
            self.pass_entry.place(x=70, y=220,width=240)
            self.pass_entry.insert(0, a)
            
    

    def signin(self):
        is_valid = validate_email(self.email_entry.get())
        if self.email_entry.get() == "" or self.pass_entry.get() == "":
            return messagebox.showerror("Error!", "All field should be filled")
        
        if "@" not in self.email_entry.get():
            return messagebox.showwarning("Error", "Email should have '@' Character")
        
        if is_valid == False:
            return messagebox.showerror("Error","Email not valid")   
        else:
            with open("Temp2.txt", "w+") as file:
                file.write(self.email_entry.get())
            self.conn = sqlite3.connect("bakery.db")
            self.c = self.conn.cursor()
            self.find_user = (
                "SELECT * FROM admin WHERE Email = ?  AND Password = ?")
            self.c.execute(str(self.find_user), (str(
                self.email_entry.get()), str(self.pass_entry.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    self.root.destroy()
                    import admin_home
            else:
                messagebox.showerror(
                    "Error!", "Username or Password may be wrong")

    def forget(self):
        is_valid1 = validate_email(self.email_entry.get())

        if self.email_entry.get() == "":
            return messagebox.showerror("Error!", "Email Required")
        
        if is_valid1 == False:
            return messagebox.showerror("Error","Email not valid")  

        else:
            self.OTP_Forget=random.randint(100000,999999)
            #print(self.OTP_Forget)
            self.root3 = Toplevel()  # Child Window "Tk() can Also be use here"
            self.root3.title("Reset")
            self.root3.geometry("700x320+350+150")
            self.root3.configure(bg="black")
            photo3 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
            self.root3.iconphoto(False, photo3)
            self.root3.focus_force() 
            self.root3.grab_set()  
            self.root3.resizable(False, False)
        
            title_child = Label(self.root3, text="ENTER CONTACT NO.", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
            sub_title_child = Label(self.root3, text="Enter contact no. associate to your given mailid", bg="yellow",compound=LEFT, font=("Calibri(body)", 10), anchor="w").place(x=0, y=120, relwidth=1)
        
            phone_lbl = Label(self.root3, text="Enter Contact", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=150)
            self.phone_entry = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
            self.phone_entry.place(x=230, y=150) 
            confirm_btn = Button(self.root3, text="verify", font=("times new roman", 18, "bold"), activebackground="#262626",activeforeground="white", bg="#262626", fg="white", cursor="hand2", command=self.confirm).place(x=300, y=260, width=140, height=30)
            
    def confirm(self):        
        global entry
        entry = self.phone_entry.get()
        self.conn = sqlite3.connect("bakery.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Email from admin WHERE Phone_No=" +
                    self.phone_entry.get())
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Phon No. not Matched to Your mail Id" , parent=self.root3)
        else:
            for i in self.data:
                    #print(i[0])

                    if i[0] == self.email_entry.get():
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = self.email_entry.get()
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("aj147ps@gmail.com","acdiqfkegwhgambh")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root3.destroy()
                                    self.root4 = Toplevel(root)  # Child Window "Tk() can Also be use here"
                                    self.root4.title("Verification")
                                    self.root4.geometry("750x320+350+150")
                                    self.root4.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
                                    self.root4.iconphoto(False, photo4)
                                    self.root4.grab_set() 
                                    self.root4.resizable(False, False)
                                
                                    title_child = Label(self.root4, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root4, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root4, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    pass_lbl = Label(self.root4, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
                                    self.pass_ = Entry(self.root4, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.pass_.place(x=260, y=170)
                                    
                                    passcon_lbl = Label(self.root4, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
                                    self.passcon = Entry(self.root4, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.passcon.place(x=260, y=220)
                                    
                                    Reset_btn = Button(self.root4, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset(self):
        self.one_ = self.otp_.get()
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        #self.root4.destroy()
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE admin SET Password = {str(self.passw)} WHERE Phone_No = {str(entry)}"
                    #print(str(y))
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    return messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root4)
                    self.OTP_Forget=""                
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root4)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root4)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root4)

root =Tk()
obj = win1(root)
root.mainloop()
