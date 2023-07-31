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
            self.pass_l = StringVar()
            self.pass_l1 = StringVar()


# ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================

            self.RightMainFrame = Frame(self.root, relief=FLAT, bg= "#ffe5b4")
            self.RightMainFrame.place(x=520, y=70, width=700, height=600)

            self.RightMainFrame_lbl1= Label(self.RightMainFrame,text="Register",font=("Calibri(body)",30,"bold"),bg= "#ffe5b4")
            self.RightMainFrame_lbl1.place(x=30, y=10)

            self.RightMainFrame_lbl2= Label(self.RightMainFrame,text="Do you have an account?",font=("Calibri(body)",8),bg= "#ffe5b4")
            self.RightMainFrame_lbl2.place(x=30, y=60)

            self.RightMainFrame_lbl3= Label(self.RightMainFrame,text="Create your account, ",font=("Calibri(body)",8),fg="#00FFFF",bg= "#ffe5b4")
            self.RightMainFrame_lbl3.place(x=157, y=60)

            self.RightMainFrame_lbl4= Label(self.RightMainFrame,text="it takes",font=("Calibri(body)",8),bg= "#ffe5b4")
            self.RightMainFrame_lbl4.place(x=262, y=60)

            self.RightMainFrame_lbl5= Label(self.RightMainFrame,text="less than a minute",font=("Calibri(body)",8),bg= "#ffe5b4")
            self.RightMainFrame_lbl5.place(x=30, y=77)

        #========================= Entries =================================
        #========================= Entries =================================


        #============================= Name Field =====================================
        #============================= Name Field =====================================

            self.name_lbl = Label(self.RightMainFrame,text="USERNAME",anchor="w",font=("times new roman",12),bg="#ffe5b4")
            self.name_lbl.place(x=30,y=150)
            self.name_txt = Entry(self.RightMainFrame,bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
            self.name_txt.place(x=125,y=150, width= 240)

            separator1RM = ttk.Separator(self.RightMainFrame, orient='horizontal')
            separator1RM.place(x=30,width=335,y=180)

        #============================= Email Field =====================================
        #============================= Email Field =====================================

            self.email_lbl = Label(self.RightMainFrame,text="EMAIL ID",anchor="w",font=("times new roman",12),bg="#ffe5b4")
            self.email_lbl.place(x=30,y=230)
            self.email_txt = Entry(self.RightMainFrame, bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
            self.email_txt.place(x=125,y=230, width= 240)

            separator2RM = ttk.Separator(self.RightMainFrame, orient='horizontal')
            separator2RM.place(x=30,width=335,y=260)
            
        #============================= Contact Field =====================================
        #============================= Contact Field =====================================

            self.contact_lbl=Label(self.RightMainFrame,text="CONTACT",bg="#ffe5b4",font=("times new roman",12))
            self.contact_lbl.place(x=30, y=325, anchor="w")
    
            self.code=IntVar()
            self.code.set(0)
            combo_code = OptionMenu(self.RightMainFrame, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
            combo_code.place(x=120,y=310)
            combo_code.config(bg="#ffe5b4",bd=0,activebackground="#ffe5b4")

            self.contact_txt = Entry(self.RightMainFrame,bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
            self.contact_txt.place(x=180,y=310, width= 185)

            separator3RM = ttk.Separator(self.RightMainFrame, orient='horizontal')
            separator3RM.place(x=30,width=335,y=340)

        #============================= Password Field =====================================
        #============================= Password Field =====================================

            self.pass_lbl = Label(self.RightMainFrame, text="PASSWORD",anchor="w",font=("times new roman",12),bg="#ffe5b4")
            self.pass_lbl.place(x=30,y=390)
            self.pass_txt = Entry(self.RightMainFrame,show=".",bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
            self.pass_txt.place(x=125,y=390, width= 195)

            separator4RM = ttk.Separator(self.RightMainFrame, orient='horizontal')
            separator4RM.place(x=30,width=335,y=420)

        #============================= Extras =====================================
        #============================= Extras =====================================

            self.val = StringVar()
            self.Terms = Radiobutton(self.RightMainFrame, font=("times new roman",8), fg="#606060", activebackground="#ffe5b4",cursor="hand2",activeforeground="#606060",text="I Accept terms and conditions & privacy policy",bg="#ffe5b4",variable=self.val)
            self.Terms.place(x=120,y=425)

            self.Seprator_lbl = Label(self.RightMainFrame, text="Follow Us On",  fg="red",font=("times new roman",15,"bold"),bg="#ffe5b4")
            self.Seprator_lbl.place(x=30, y=480)

        #============================ Buttons ===================================
        #============================ Buttons ===================================

            self.ButtonRF_1 = Button(self.RightMainFrame,bd=0, image = self.register_icon, activebackground="#ffe5b4",bg="#ffe5b4",borderwidth=0,cursor="hand2", command=self.register)
            self.ButtonRF_1.place(x=230, y=460)

            self.ButtonRF_2 = Button(self.RightMainFrame,bd=0, image = self.fb_icon, activebackground="#ffe5b4",bg="#ffe5b4",cursor="hand2", command=self.link1)
            self.ButtonRF_2.place(x=30, y=530)

            self.ButtonRF_3 = Button(self.RightMainFrame,bd=0, image = self.gmail_icon, activebackground="#ffe5b4",bg="#ffe5b4",cursor="hand2", command=self.link2)
            self.ButtonRF_3.place(x=130, y=530)

            self.ButtonRF_4 = Button(self.RightMainFrame,bd=0, image = self.insta_icon, activebackground="#ffe5b4",bg="#ffe5b4",cursor="hand2", command=self.link3)
            self.ButtonRF_4.place(x=230, y=530)

            self.ButtonRF_5 = Button(self.RightMainFrame,bd=0, image = self.twitter_icon, activebackground="#ffe5b4",bg="#ffe5b4",cursor="hand2", command=self.link4)
            self.ButtonRF_5.place(x=320, y=530)

            self.ButtonRF_6 = Button(self.RightMainFrame,bd=0, image = self.showpass_icon, activebackground="#ffe5b4",bg="#ffe5b4",cursor="hand2", command=self.show)
            self.ButtonRF_6.place(x=325, y=388, height=30)

            self.ButtonRF_7 = Button(self.RightMainFrame,bd=5, relief=GROOVE, font=("iimes new roman",10,"bold"),text="Employee Sign In", activebackground="blue",activeforeground="yellow",fg="yellow",bg="blue",cursor="hand2", command=self.employee)
            self.ButtonRF_7.place(x=540, y=10, height=30,width=130)

           
# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
# ================== Right Sub Frame 1 =========================================
            
            
            self.RightSubFrame = Frame(self.root, relief=FLAT, bd=6,bg="#B80F0A")
            self.RightSubFrame.place(x=900, y=120, width=400, height=500)


            self.RightSubFrame_lbl1= Label(self.RightSubFrame, fg="#FFFF33",text="As User",font=("times new roman",20,"bold"),bg= "#B80F0A")
            self.RightSubFrame_lbl1.place(x=10, y=50)

            self.img_RSF1 = Label(self.RightSubFrame, bg="#B80F0A",image = self.me_icon)
            self.img_RSF1.place(x=150, y=10)

            self.RightSubFrame_lbl2= Label(self.RightSubFrame, fg="#FFFF33",text="Sign In",font=("times new roman",20,"bold"),bg= "#B80F0A")
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
            self.pass_entry.insert(0,"...........")

            separator1 = ttk.Separator(self.RightSubFrame, orient='horizontal')
            separator1.place(x=10,width=140,y=360)
            
            self.Seprator_lbl1 = Label(self.RightSubFrame, text="Follow Us On",  fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A")
            self.Seprator_lbl1.place(x=160, y=350)

            separator2 = ttk.Separator(self.RightSubFrame, orient='horizontal')
            separator2.place(x=250,width=130,y=360)

            self.Seprator_lbl2 = Label(self.RightSubFrame, text="Developed By Aditya Jha",  fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A")
            self.Seprator_lbl2.place(x=130, y=455)

            
        # =================== Buttons ================================
            
            self.ButtonRSF_1 = Button(self.RightSubFrame,bd=0, image = self.showpass_icon,activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.show1)
            self.ButtonRSF_1.place(x=320, y=215)

            self.ButtonRSF_2 = Button(self.RightSubFrame, bd=0,text="Forget Password", activebackground="#B80F0A", fg="#FFFFFF",font=("times new roman",10),bg="#B80F0A",cursor="hand2",command=self.forget)
            self.ButtonRSF_2.place(x=150, y=270)

            self.ButtonRSF_3 = Button(self.RightSubFrame,bd=0, text="Sign In",font=("times new roman",20,"bold"), activebackground="white",bg="white",cursor="hand2", command=self.signin)
            self.ButtonRSF_3.place(x=70, y=300, width=290,height=30)

            self.ButtonRSF_4 = Button(self.RightSubFrame,bd=0, image = self.fb_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link1)
            self.ButtonRSF_4.place(x=20, y=400)

            self.ButtonRSF_5 = Button(self.RightSubFrame,bd=0, image = self.gmail_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link2)
            self.ButtonRSF_5.place(x=130, y=400)

            self.ButtonRSF_6 = Button(self.RightSubFrame,bd=0, image = self.insta_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link3)
            self.ButtonRSF_6.place(x=230, y=400)

            self.ButtonRSF_7 = Button(self.RightSubFrame,bd=0, image = self.twitter_icon, activebackground="#B80F0A",bg="#B80F0A",cursor="hand2", command=self.link4)
            self.ButtonRSF_7.place(x=320, y=400)



# ================== Left Main Frame 1 =========================================
# ================== Left Main Frame 1 =========================================
# ================== Left Main Frame 1 =========================================
# ================== Left Main Frame 1 =========================================

            self.LeftMainFrame = Frame(self.root, relief=FLAT, bg= "#0e1111")
            self.LeftMainFrame.place(x=150, y=70, width=370, height=600)


            self.img_LF1 = Label(self.LeftMainFrame, image = self.icon2, bg="#0e1111")
            self.img_LF1.place(x=10, y=10)

            self.img_LF2 = Label(self.LeftMainFrame, image = self.icon, bg="#0e1111")
            self.img_LF2.place(x=130, y=160)

            
            self.Mlbl_LF = Label(self.LeftMainFrame, text="Aditya's Bakery", fg="white",bg= "#0e1111", font=("Abril Fatface",25, "bold"))
            self.Mlbl_LF.place(x=65, y=230)

            self.sloganlbl_LF = Label(self.LeftMainFrame, text="\"Bake the World a better place\"", fg="#CD5C5C",bg= "#0e1111", font=("Crimson Text",15))
            self.sloganlbl_LF.place(x=50, y=280)

            self.introlbl_LF = Label(self.LeftMainFrame, text="A bakery is an establishment that produces \nand sells flour-based food baked in an \noven such as bread, cookies, cakes, \npastries, and pies.", fg="white",bg= "#0e1111", font=("times new roman",10))
            self.introlbl_LF.place(x=60, y=340)

            self.versionlbl_LF = Label(self.LeftMainFrame, text="version 1.0", fg="white",bg= "#0e1111", font=("times new roman",8))
            self.versionlbl_LF.place(x=30, y=570)

            self.ButtonLeft = Button(self.LeftMainFrame, text="Admin Sign In", font=("times new roman",15,"bold"), bg="#0276FD", fg="#FFFFFF", activeforeground="#FFFFFF", activebackground="#0276FD", relief=GROOVE, bd=5, cursor="hand2",command=self.admin)
            self.ButtonLeft.place(x=230, y=420, width=130, height=35)


            self.pass_lbl = Entry(self.RightSubFrame, font=(
            "time new roman", 10), textvariable=self.pass_l, fg="white", bg="black").place(x=10, y=10)
            self.pass_l.set("Password Mode: Hidden")
            
            self.pass_lbl1 = Entry(self.RightMainFrame, font=(
            "time new roman", 10), textvariable=self.pass_l1, fg="white", bg="black").place(x=250, y=10)
            self.pass_l1.set("Password Mode: Hidden")
            
            now = datetime.now()
            self.Time1 = now.strftime('%H:%M:%S')
            self.date = now.strftime("%d-%b-%Y")


    def employee(self):
        self.root.destroy()
        import logine

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
    
    
    def show1(self):
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
        
    
    def show(self):
        a = self.pass_txt.get()
        self.pass_txt = Entry(self.RightMainFrame,show=".",bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
        self.pass_txt.place(x=125,y=390, width= 195)
        self.pass_txt.insert(0, a)
        if self.pass_l1.get() == "Password Mode: Hidden":
            self.pass_l1.set("Password Mode: Shown")
            self.pass_txt = Entry(self.RightMainFrame,bd=0,font=("times new roman",15,"bold"),bg="#ffe5b4", fg="grey")
            self.pass_txt.place(x=125,y=390, width= 195)
            self.pass_txt.insert(0, a)

        elif self.pass_l1.get() == "Password Mode: Shown":
            self.pass_l1.set("Password Mode: Hidden")
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
            with open("Temp.txt", "w+") as file:
                file.write(self.email_entry.get())
            self.conn = sqlite3.connect("bakery.db")
            self.c = self.conn.cursor()
            self.find_user = (
                "SELECT * FROM user WHERE Email = ?  AND Password = ?")
            self.c.execute(str(self.find_user), (str(
                self.email_entry.get()), str(self.pass_entry.get())))
            results = (self.c).fetchall()
            if results:
                for i in results:
                    messagebox.showinfo("Success","Successfully Logined")
                    self.root.destroy()
                    import Homeu
            else:
                messagebox.showerror(
                    "Error!", "Username or Password may be wrong")

    def register(self):
        is_valid1 = validate_email(self.email_txt.get())
        
        if self.name_txt.get() == "" or self.email_txt.get() == "" or self.contact_txt.get() == "" or self.pass_txt.get() == "" or self.code.get() == 0:
            return messagebox.showerror("Error", "All Fields Required and contry code need to be set")
        
        if is_valid1 == False:
            return messagebox.showerror("Error","Email not valid")  

        try:
            tmp=self.contact_txt.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer or remove space')
        
        if len(self.contact_txt.get()+str(self.code.get()))<10 and len(self.contact_txt.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
         
        if len(self.pass_txt.get())<8:
            return messagebox.showinfo('Error','Password Should Of minimum 8 character')      
        
        if  " " in self.name_txt.get() :
            return messagebox.showinfo('Error','Username Cann\'t have space')      
        
        if  " " in self.pass_txt.get():
            return messagebox.showinfo('Error','Password Cann\'t have space')      
        
        if  " " in self.email_txt.get() :
            return messagebox.showinfo('Error','Email Cann\'t have space')      
        
        else:
            self.otp = str(random.randint(100000,999999))
            #print(self.otp)

            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            self.find_user = ("SELECT * FROM user WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email_txt.get(),self.contact_txt.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
            
                send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                send.starttls()  # transport layer

                #===================Plain Text=====================

                msg = EmailMessage()
                msg["Subject"] = "OTP"
                msg["From"] = "aj147ps@gmail.com"
                msg["To"] = self.email_txt.get()
                msg.set_content("Hi!"+str(self.name_txt.get())+" your OTP for registration is: "+"\'"+self.otp+"\'")        
                    
                try:
                    send.login("aj147ps@gmail.com","acdiqfkegwhgambh")
                except smtplib.SMTPAuthenticationError:
                    messagebox.showerror("Error","Error Occur Otp Not")    

                try:
                    try:
                        try:
                            send.send_message(msg)
                            messagebox.showinfo("Mailed","OTP Sent to Your Mail Id")                        
                            self.root2 = Toplevel()  # Child Window "Tk() can Also be use here"
                            self.root2.title("OTP")
                            self.root2.geometry("700x320+350+150")
                            self.root2.configure(bg="black")
                            photo2 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
                            self.root2.iconphoto(False, photo2)
                            self.root2.focus_force() 
                            self.root2.grab_set()  
                            self.root2.resizable(False, False)
                        
                            title_child = Label(self.root2, text="ENTER OTP", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                        
                            otp_lbl = Label(self.root2, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=150)
                            self.otp_entry = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                            self.otp_entry.place(x=230, y=150)

                            verify_btn = Button(self.root2, text="verify", font=("times new roman", 18, "bold"), activebackground="#262626",activeforeground="white", bg="#262626", fg="white", cursor="hand2", command=self.verify).place(x=300, y=260, width=140, height=30)
                        except smtplib.SMTPRecipientsRefused:
                            messagebox.showerror("Mailed","Mail Not Sent")
                    except smtplib.SMTPException:
                        messagebox.showerror("Mailed","Mail Not Sent")
                except smtplib.SMTPConnectError:
                    messagebox.showerror("Error","Connection Error")

    def verify(self):
        if self.otp == self.otp_entry.get():
            messagebox.showinfo("Success","Verified", parent=self.root2)
            self.count = str(region_code_for_country_code(self.code.get()))
            self.UID=self.name_txt.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS user(UID TEXT UNIQUE PRIMARY KEY NOT NULL ,Uname TEXT NOT NULL, Email TEXT UNIQUE NOT NULL ,Country_Code TEXT NOT NULL, Country TEXT NOT NULL,Phone_No TEXT UNIQUE NOT NULL,Password TEXT NOT NULL)")
            self.find_user = ("SELECT * FROM user WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email_txt.get(),self.contact_txt.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO user (UID ,Uname, Email ,Country_Code, Country,Phone_No,Password ) VALUES (?,?,?,?,?,?,?)",
                    (self.UID,self.name_txt.get(),self.email_txt.get(),self.code.get(),self.count, self.contact_txt.get(),self.pass_txt.get()))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.otp_entry.delete(0,END)
                    self.otp=None
                    return messagebox.showinfo("Successfull","Successfully Added Data, Now You Can Login")
                    
                except Exception:
                    return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again. "+"You  User ID :"+self.UID)        
        else:
            messagebox.showerror("Error","OTP Enterd Is Wrong! Try Again To Resend again click on Resgister")            

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
        self.c.execute("SELECT Email from user WHERE Phone_No=" +
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
                    y= f"UPDATE user SET Password = {str(self.passw)} WHERE Phone_No = {str(entry)}"
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
