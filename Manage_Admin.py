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
import random ,time
from datetime import datetime
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
from tkcalendar import Calendar, DateEntry


        

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

        bg_color ="#FFFFF6"
    

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
        self.bakery_icon=ImageTk.PhotoImage(file="Pics/Bakery1.jpg")
        self.bakery_icon1=ImageTk.PhotoImage(file="Pics/Bakery2.jpg")        
        self.home_icon=ImageTk.PhotoImage(file="Pics/user_btn1.png")
        self.Manage_Emp1=ImageTk.PhotoImage(file="Pics/Manage_Emp.png")
        self.Manage_Admin1=ImageTk.PhotoImage(file="Pics/Manage_admin.jpg")
        self.items_icon=ImageTk.PhotoImage(file="Pics/user_btn2.png")
        self.exit_icon=ImageTk.PhotoImage(file="Pics/user_btn4.jpg")

        

        
        F1 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F1.place(x=0,relwidth=1,height=100 )

        lbl = Label(F1,text="Bakery Management System", bg=bg_color, font= ("times new roman",25,"bold")).place(x=120, y=15)

        self.lbl_hr = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_hr.place(x=850, y=40)
        
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=875, y=40)
       
       
        self.lbl_min = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_min.place(x=885, y=40)
       
        self.lbl_COLON = Label(F1,text=":" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_COLON.place(x=910, y=40)
       
        self.lbl_sec = Label(F1,text="12" , font = ("times new roman", 15,"bold"),bg=bg_color)
        self.lbl_sec.place(x=920, y=40)
        

        self.lbl_abv = Label(F1,text="AM" , font = ("times new roman", 13,"bold"),bg=bg_color)
        self.lbl_abv.place(x=945, y=43)
       
       
        self.font=("times new roman",20,"bold")
        self.calendar = []

        self.calendar.append(DateEntry(F1, font=("times new roman",15,"bold"), locale='en_GB',state="readonly", width=10))
        self.calendar[-1].place(x=855, y=20, anchor="w")

        
        btn_changepass = Button(F1, text="ChangePassword",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="red",foreground="white",command=self.change_pasw).place(x=1145,y=20,anchor="w")
        btn_logout = Button(F1, text="Logout",relief=RAISED,width =15,height=1, font=("times new roman",14,"bold"),bg="light green",foreground="black",command=self.logout).place(x=1145,y=60,anchor="w")

        lbl2 = Label(F1,image=self.bakery_icon,bg=bg_color)
        lbl2.place(x=25,y=10)

     #----------------------------------F2------------------------------------
        F2 = LabelFrame(self.root,bd=10,relief=GROOVE,bg=bg_color)
        F2.place(x=0,y=100,width=150,height=670 )

        F21 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F21.place(x=0,y=0,width=130,height=133 )
        
        F22 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F22.place(x=0,y=133,width=130,height=133)
        
        F23 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F23.place(x=0,y=266,width=130,height=133 )
        
        F24 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F24.place(x=0,y=399,width=130,height=133)
        
        F25 = LabelFrame(F2,bd=5,relief=GROOVE,bg=bg_color)
        F25.place(x=0,y=532,width=130,height=133)

        btn_home = Button(F21,image= self.home_icon,bg=bg_color,relief=RAISED,width =115,height=120,command=self.home).place(x=0,y=60,anchor="w")
        btn_Emp = Button(F22,image= self.Manage_Emp1,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Manage_Emp ).place(x=0,y=60,anchor="w")
        btn_admin = Button(F23,relief=RAISED,bg=bg_color,image=self.Manage_Admin1,width =115,height=120,command=self.Manage_Admin ).place(x=0,y=60,anchor="w")
        btn_view_items = Button(F24,relief=RAISED,image=self.items_icon,bg=bg_color,width =115,height=120, command=self.view_all).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit_icon,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")


         
        
        
       
#------------------------------F3--------------------------------
        F3 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Admin",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

        # ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================
# ================== Right Main Frame 1 =========================================

        self.RightMainFrame = Frame(self.root, relief=FLAT, bg= "#ffe5b4")
        self.RightMainFrame.place(x=390, y=120, width=700, height=600)

        self.RightMainFrame_lbl1= Label(self.RightMainFrame,text="Manage Details",font=("Calibri(body)",30,"bold"),bg= "#ffe5b4")
        self.RightMainFrame_lbl1.place(x=30, y=10)

        self.RightMainFrame_lbl2= Label(self.RightMainFrame,text="Do you added your details?",font=("Calibri(body)",8),bg= "#ffe5b4")
        self.RightMainFrame_lbl2.place(x=30, y=60)

        self.RightMainFrame_lbl3= Label(self.RightMainFrame,text="Add your details, ",font=("Calibri(body)",8),fg="#00FFFF",bg= "#ffe5b4")
        self.RightMainFrame_lbl3.place(x=157, y=60)

        self.RightMainFrame_lbl4= Label(self.RightMainFrame,text="it takes",font=("Calibri(body)",8),bg= "#ffe5b4")
        self.RightMainFrame_lbl4.place(x=262, y=60)

        self.RightMainFrame_lbl5= Label(self.RightMainFrame,text="less than a minute",font=("Calibri(body)",8),bg= "#ffe5b4")
        self.RightMainFrame_lbl5.place(x=30, y=77)

        self.RightMainFrame_lbl6= Label(self.RightMainFrame,image=self.bakery_icon1)
        self.RightMainFrame_lbl6.place(x=470, y=200)

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

        self.ButtonRF_7 = Button(self.RightMainFrame,bd=5, relief=GROOVE, font=("iimes new roman",10,"bold"),text="Back", activebackground="blue",activeforeground="yellow",fg="yellow",bg="blue",cursor="hand2", command=self.back)
        self.ButtonRF_7.place(x=540, y=10, height=30,width=130)

        



        now = datetime.now()
        self.Time1 = now.strftime('%H:%M:%S')
        self.date = now.strftime("%d-%b-%Y")
        self.clock()


    def back(self):
        self.root.destroy()
        import admin

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
        pass
    

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
            self.find_user = ("SELECT * FROM admin WHERE Email= ?  or Phone_No = ?")
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
                    send.login("your Email Id","Your Password")
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
            self.AID=self.name_txt.get()+str(random.randint(1000,40000))

            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            self.c.execute("CREATE TABLE IF NOT EXISTS admin(AdID TEXT UNIQUE PRIMARY KEY NOT NULL ,Ad_name TEXT , Password TEXT NOT NULL, Email TEXT UNIQUE NOT NULL ,Country_Code TEXT, Phone_No TEXT UNIQUE , Country TEXT )")
            self.find_user = ("SELECT * FROM admin WHERE Email= ?  or Phone_No = ?")
            self.c.execute(str(self.find_user),(self.email_txt.get(),self.contact_txt.get()))
            results = (self.c).fetchall()
            if results:
                messagebox.showerror("Error","Email or Contact  is already Used")
            else:
                try:
                    self.c.execute("INSERT INTO admin (Ad_ID  ,Ad_name , Password  , Email ,Country_Code, Phone_No, Country ) VALUES (?,?,?,?,?,?,?)",
                    (self.AID,self.name_txt.get(),self.pass_txt.get(),self.email_txt.get(),self.code.get(), self.contact_txt.get(),self.count))
                    self.conn.commit()
                    self.c.close()
                    self.conn.close()
                    self.otp_entry.delete(0,END)
                    self.otp=None
                    return messagebox.showinfo("Successfull","Successfully Added Data"+"You  Admin ID :"+self.AID)
                
                except Exception:
                    return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again. ")        
        else:
            messagebox.showerror("Error","OTP Enterd Is Wrong! Try Again To Resend again click on Resgister")            


    def clock(self):
        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h)>=12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>=15 and int(self.h)<20 and int(self.m)>0:
            self.lbl_abv.config(text="PM")
        
        if int(self.h)>=20 and int(self.h)<24 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>12 and int(self.h)<15 and int(self.m)>0:
            self.lbl_abv.config(text="PM")

        if int(self.h)>0 and int(self.h)<12 and int(self.m)>0:
            self.lbl_abv.config(text="AM")

        
        self.lbl_hr.config(text = self.h)
        self.lbl_min.config(text = self.m)
        self.lbl_sec.config(text = self.s)
        self.lbl_hr.after(200,self.clock)



    def logout(self):
        self.read1=StringVar()
        with open("Temp2.txt","r+") as file:
            self.read1=file.read()
            file.truncate()
    
        a=messagebox.askyesnocancel("Hey","Confirm again for Logout")
        if a>0:
            now = datetime.now()
            self.Time2=now.strftime('%H:%M:%S')

            self.today1= now.strftime("%Y-%m-%d")
            self.root.destroy()
            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            y="UPDATE Last_Login_Admin set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where Email =\""+str(self.read1)+"\""
            print(y)
            self.c.execute(y)
            self.conn.commit()
            import admin
        else:
            pass

    
    def home(self):
        self.root.destroy()
        import admin_home

    def Manage_Emp(self):
        self.root.destroy()
        import Manage_Emp

    def Manage_Admin(self):
        self.root.destroy()
        import Manage_Admin
    
    def view_all(self):
        self.root.destroy()
        import View_Item_List_admin

    def change_pasw(self):  
        self.root2 = Toplevel(root)  # Child Window "Tk() can Also be use here"
        self.root2.title("Change Password")
        self.root2.geometry("750x370+350+150")
        self.root2.configure(bg="black")
        photo1 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
        self.root2.iconphoto(False, photo1)
        self.root2.grab_set() 
        self.root2.resizable(False, False)

        title_child = Label(self.root2, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
        
        phone_lbl = Label(self.root2, text="Phone No.", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
        self.phone_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.phone_.place(x=260, y=120)
        
        current_lbl = Label(self.root2, text="Current Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=170)
        self.current_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.current_.place(x=260, y=170)
        
        pass_lbl = Label(self.root2, text="New Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=220)
        self.pass_ = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.pass_.place(x=260, y=220)
        
        passcon_lbl = Label(self.root2, text="Confirm Password", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=270)
        self.passcon = Entry(self.root2, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
        self.passcon.place(x=260, y=270)
        
        Reset_btn = Button(self.root2, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset)
        Reset_btn.place(x=495, y=310, width=140, height=30) 

      
        
    def reset(self):
        with open("Temp2.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("bakery.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from admin WHERE Phone_No=" +self.phone_2)
        self.data = self.c.fetchall()
        if self.data==[]:
            return messagebox.showerror("Error"," Current Password not Matched to Your mail Id" , parent=self.root2)
        else:
            for i in self.data:
                    #print(i[0])

                    if i[0] == self.current2_:
                        self.OTP_Forget=str(random.randint(100000,999999))
                        send = smtplib.SMTP("smtp.gmail.com", 587)  # Create session for Gmail
                        send.starttls()  # transport layer

                        msg = EmailMessage()
                        msg["Subject"] = "OTP"
                        msg["From"] = "aj147ps@gmail.com"
                        msg["To"] = self.read1
                        msg.set_content("Hi! your OTP for reset password: "+"\'"+str(self.OTP_Forget)+"\'")        
                            
                        try:
                            send.login("your Email Id","Your Password")
                        except smtplib.SMTPAuthenticationError:
                            messagebox.showerror("Error","Error Occur Otp Not")    

                        try:
                            try:
                                try:                                
                                    
                                    send.send_message(msg)
                                    messagebox.showinfo("Mailed","OTP Sent to Your Mail Id") 
                                    self.root2.destroy()
                                    self.root3 = Toplevel(root)  # Child Window "Tk() can Also be use here"
                                    self.root3.title("Verification")
                                    self.root3.geometry("750x320+350+150")
                                    self.root3.configure(bg="black")
                                    photo4 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
                                    self.root3.iconphoto(False, photo4)
                                    self.root3.grab_set() 
                                    self.root3.resizable(False, False)
                                
                                    title_child = Label(self.root3, text="Reset Password", bg="#152238", fg="white",compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w").place(x=0, y=0, relwidth=1)
                                    otp_lbl = Label(self.root3, text="Enter OTP", font=("time new roman", 18, "bold"), fg="white", bg="black").place(x=30, y=120)
                                    self.otp_ = Entry(self.root3, bd=5, width=30, bg="lightgrey", font=("times new roman", 18))
                                    self.otp_.place(x=260, y=120)
                                    
                                    Reset_btn = Button(self.root3, text="Reset", font=("times new roman", 18, "bold"), activebackground="blue",activeforeground="white", bg="blue", fg="white", cursor="hand2", command=self.reset1)
                                    Reset_btn.place(x=495, y=260, width=140, height=30) 
                        
                                except smtplib.SMTPRecipientsRefused:
                                    messagebox.showerror("Mailed","Mail Not Sent")
                            except smtplib.SMTPException:
                                messagebox.showerror("Mailed","Mail Not Sent")
                        except smtplib.SMTPConnectError:
                            messagebox.showerror("Error","Connection Error")
                    else:
                        return messagebox.showerror("Error","Contact No. have not given Mail Id")

    def reset1(self):
        self.one_ = self.otp_.get()
        #print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE admin SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
                    self.c.execute(str(y))
                    self.conn.commit()
                    self.conn.close()
                    self.OTP_Forget=""
                    messagebox.showinfo("Info", "Successfully Changed!!", parent=self.root3)
                    self.root3.destroy()                    
                else:
                    return messagebox.showerror("Error", "Password Cann't Changed  password  and confirm password not match!!", parent=self.root3)
            else:
                return messagebox.showerror("Error", "Password should be of minimum 8 Characters", parent=self.root3)
        else:
            return messagebox.showerror("Error", "OTP Entered is Wrong", parent=self.root3)

    
    def Exit(self):
        self.root.destroy()
            

root = Tk()
obj = win1(root)
root.mainloop()
