from tkinter import*
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import sys,sqlite3,time
from datetime import datetime
import random
from ttkthemes import ThemedTk
from tkcalendar import Calendar, DateEntry
import pycountry
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code

from tkinter import ttk # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk

#--------
#self.F2 = ImageTk.PhotoImage(file="download1.jpeg") # here we store image to a variable using PIL module help 

class win1:
    def __init__(self,root):
        self.root = root
        self.root.title("Bakery Management System".center(420))  # title for Window 
        self.root.configure(background = "black")  # background color for window 
        self.root.geometry("1360x768+0+0")
        photo = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
        root.iconphoto(False, photo)

        bg_color ="#FFFFF6"
        
        #-----------F1----------------------------------------------------------------------------------------------------
        self.bg_icon = ImageTk.PhotoImage(file="Pics/x1r4Ao.png")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.bakery_icon=ImageTk.PhotoImage(file="Pics/Bakery1.jpg")
        self.home_icon=ImageTk.PhotoImage(file="Pics/user_btn1.png")
        self.orderhis_icon=ImageTk.PhotoImage(file="Pics/user_btn6.png")
        self.order_icon=ImageTk.PhotoImage(file="Pics/user_btn5.jpg")
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
        btn_orderhis = Button(F22,image= self.orderhis_icon,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Search_Items ).place(x=0,y=60,anchor="w")
        btn_order = Button(F23,relief=RAISED,bg=bg_color,image=self.order_icon,width =115,height=120,command=self.buy ).place(x=0,y=60,anchor="w")
        btn_view_items = Button(F24,relief=RAISED,image=self.items_icon,bg=bg_color,width =115,height=120, command=self.view_all).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit_icon,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")


         
        
        
       
#------------------------------F3--------------------------------
        F3 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Employee",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

#-----------------Main Screen Frames---------------------------------
        self.conn=sqlite3.connect("bakery.db")
        self.c=self.conn.cursor()
        

        F4 = LabelFrame(self.root,bd=10,relief=GROOVE,bg="#DC143C")
        F4.place(x=300,y=170,width=400,height=250 )

        F41 = LabelFrame(F4,bd=5,relief=SUNKEN,bg="#DC143C")
        F41.place(x=0,y=0,width=380,height=60 )
        lbl_2= Label(F41,text="Total Users",fg="#FFFFFF",bg="#DC143C",font=("times new roman",25,"bold"))
        lbl_2.place(x=0,y=0)

        
        F42 = LabelFrame(F4,bd=5,relief=GROOVE)
        F42.place(x=0,y=60,width=380,height=180 )

        text1=Text(F42,bd=5, font=("times new roman",30,"bold"))
        self.c.execute("SELECT COUNT(*) FROM user")
        self.results1 = ((self.c).fetchall())        
        text1.insert(INSERT,("\n             Total\n           Users: "))
        text1.insert(INSERT,self.results1)
        text1.place(x=0,y=0,width=370,height=170)
        text1.configure(state="disabled")
                        

        F5 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F5.place(x=800,y=170,width=400,height=250 )

        F51 = LabelFrame(F5,bd=5,relief=SUNKEN, bg="#3B9C9C")
        F51.place(x=0,y=0,width=380,height=60 )
        lbl_3= Label(F51,text="Last Login",fg="#FFFFFF",bg="#3B9C9C",font=("times new roman",30,"bold"))
        lbl_3.place(x=0,y=0)

        
        F52 = LabelFrame(F5,bd=5,relief=GROOVE)
        F52.place(x=0,y=60,width=380,height=180 )

        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        text2=Text(F52,bd=5, fg="white",font=("times new roman",15,"bold"),bg="#151B54")
        self.c.execute("SELECT * FROM Last_Login_Emp WHERE Email =\""+str(self.read1)+"\"")
        self.results2 = ((self.c).fetchall())        
        text2.insert(INSERT,(""))
        if self.results2:
            for i in self.results2:
                print(i)    
            #self.EmpID.set(i[0])  
            text2.insert(INSERT,("\nEmpID                 :   "+str(i[0]+" ")))
            text2.insert(INSERT,("\nEmail                   :   "+str(i[1])+"\n"))
            text2.insert(INSERT,("Last Login Time :   "+str(i[2])+"\n"))
            text2.insert(INSERT,("Last Login Date :   "+str(i[3])+"\n"))

            text2.place(x=0,y=0,width=370,height=170)
            text2.configure(state="disabled")

        
        
        F6 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F6.place(x=300,y=450,width=400,height=250 )

        F61 = LabelFrame(F6,bd=5,relief=SUNKEN,fg="#FFFFFF",bg="black")
        F61.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F61,text="Total Employees",bg="black",fg="#FFFFFF",font=("times new roman",30,"bold"))
        lbl_4.place(x=0,y=0)


        F62 = LabelFrame(F6,bd=5,relief=GROOVE)
        F62.place(x=0,y=60,width=380,height=180 )

        text3=Text(F62,bd=5, fg="white",font=("times new roman",30,"bold"),bg="#151B54")
        self.c.execute("SELECT COUNT(*) FROM Emp")
        self.results3 = ((self.c).fetchall())        
        text3.insert(INSERT,("\n             Total\n         Employees: "))
        text3.insert(INSERT,self.results3)
        text3.place(x=0,y=0,width=370,height=170)
        text3.configure(state="disabled")

        
        
        F7 = LabelFrame(self.root,bd=10,relief=GROOVE)
        F7.place(x=800,y=450,width=400,height=250 )
        
        F71 = LabelFrame(F7,bd=5,relief=SUNKEN,bg="white")
        F71.place(x=0,y=0,width=380,height=60 )
        lbl_4= Label(F71,text="Developer",bg="white",font=("times new roman",30,"bold"),fg="#DC143C")
        lbl_4.place(x=0,y=0)


        F72 = LabelFrame(F7,bd=5,relief=RAISED)
        F72.place(x=0,y=60,width=380,height=180 )

        text7=Text(F72,bd=5,font=("times new roman",15, "italic"),fg="#FFFFFF", bg="#DC143C",relief=GROOVE)
        text7.insert(INSERT,("                       Developed By\n\nAditya Jha\nEmail Id:aj147ps@gmail.com\nAlternate Email Id:codewithajofficial14@gmail.com\nFollow on #codewithajofficial on insta "))
        text7.place(x=0,y=0,width=370,height=170)
        text7.configure(state="disabled")


        self.clock()

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
        with open("Temp1.txt","r+") as file:
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
            y="UPDATE Last_Login_Emp set last_login_time=\""+str(self.Time2)+"\", last_login_date=\""+str(self.today1)+"\" where Email =\""+str(self.read1)+"\""
            print(y)
            self.c.execute(y)
            self.conn.commit()
            import logine
        else:
            pass

    
    def home(self):
        self.root.destroy()
        import HomeE

    def Search_Items(self):
        self.root.destroy()
        import Search_ItemsE

    def buy(self):
        self.root.destroy()
        import BuyUE
        
    def view_all(self):
        self.root.destroy()
        import View_Item_listE
    
            
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
        with open("Temp1.txt","r+") as file:
            self.read1=file.read()
        #print(self.read1)
        self.passw = self.pass_.get()
        self.passconw = self.passcon.get()
        self.current2_=self.current_.get()
        self.phone_2=self.phone_.get()
        
        self.conn = sqlite3.connect("bakery.db")
        self.c = self.conn.cursor()
        self.c.execute("SELECT Password from Emp WHERE Phone_No=" +self.phone_2)
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
        print(self.one_)
        if str(self.one_)==str(self.OTP_Forget):
            if len(str(self.passw))>=8:
                if self.passw == self.passconw:
                    y= f"UPDATE Emp SET Password = {str(self.passw)} WHERE Phone_No = {str(self.phone_2)}"
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
