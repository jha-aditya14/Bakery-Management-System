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
import smtplib
from email.message import EmailMessage
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
        
#==============================Icons==============================================        
        self.bg_icon = ImageTk.PhotoImage(file="Pics/x1r4Ao.png")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.bakery_icon=ImageTk.PhotoImage(file="Pics/Bakery1.jpg")
        self.home_icon=ImageTk.PhotoImage(file="Pics/user_btn1.png")
        self.items_icon=ImageTk.PhotoImage(file="Pics/user_btn2.png")
        self.exit_icon=ImageTk.PhotoImage(file="Pics/user_btn4.jpg")
        self.Manage_Admin1=ImageTk.PhotoImage(file="Pics/Manage_admin.jpg")
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

# ============================= Variabe =========================================
# ============================= Variabe =========================================
# ============================= Variabe =========================================
# ============================= Variabe =========================================

        self.EID = StringVar()
        self.Name = StringVar()
        self.Email = StringVar()
        self.pass_ = StringVar()
        self.contact = StringVar()
        self.code = IntVar()
        self.zoneID = StringVar()
        self.branchID = StringVar()
        self.role = StringVar()
        self.EID.set(str(random.randint(1000,999999)))
        

        #-----------F1----------------------------------------------------------------------------------------------------
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
        btn_admin = Button(F23,relief=RAISED,bg=bg_color,image=self.Manage_Admin1,width =115,height=120,command=self.Manage_Admin).place(x=0,y=60,anchor="w")
        btn_view_items = Button(F24,relief=RAISED,image=self.items_icon,bg=bg_color,width =115,height=120, command=self.view_all).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit_icon,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------F3------------------------------------------------------------------------------------------


        F3 = Frame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=30 )
        lbl_1= Label(F3,text="Dashboard / Admin",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------
#------------------------------------------------------------------------Main Screen Frames-------------------------------------------------------------------------------------



#*****************************************************************************************************************************************************************************



#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM1-------------------------------------------------------------------------------------

        self.FM1 = Frame(self.root,bd=5,relief=RAISED)
        self.FM1.place(x=430,y=160,width=700,height=550 )

#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM11-------------------------------------------------------------------------------------




        FM11 =Frame(self.FM1,bd=5,relief=RAISED,bg="yellow")
        FM11.place(x=0,y=0,relwidth=1,height=60 )
        lbl_FM11= Label(FM11,text="Manage Employee",font=("times new roman",30,"bold"),fg="black",bg="yellow")
        lbl_FM11.place(x=20,y=0)

        lblID_roll=Label(FM11,text="Emp ID",bg="yellow",font=("times new roman",18,"bold"))
        lblID_roll.place(x=400,y=25,anchor="w")
        txtID_roll=Entry(FM11, width=17, textvariable=self.EID,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txtID_roll.place(x=485,y=25,anchor="w")


#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------FM12-------------------------------------------------------------------------------------




        FM12 =Frame(self.FM1,bd=10,relief=SUNKEN,bg="#074463")
        FM12.place(x=0,y=440,relwidth=1,height=80 )

        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        #---------------------------------------------BUTTONS--------------------------------------------------------------------------------
        
        
        but_Add=Button(self.FM1,text="ADD Data",bg="grey",bd=5,width=18,font=("times new roman",12,"bold"),command=self.add).place(x=500, y=390, anchor="w")
        btn_update2 = Button(FM12,relief=GROOVE,width=8, font=("times new roman",18,"bold"),bd=6,text="Update",command=self.update).grid(row=0,column=1,pady=6,padx=50,sticky="nesw")        
        btn_Delete = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Delete",command=self.delete).grid(row=0,column=2,pady=6,padx=50,sticky="nesw")
        btn_Clear = Button(FM12,relief=GROOVE, width=8,font=("times new roman",18,"bold"),bd=6,text="Clear",command=self.clear).grid(row=0,column=3,pady=6,padx=50,sticky="nesw")        


        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------
        #---------------------------------------------Entries--------------------------------------------------------------------------------

        

        lbl_roll=Label(self.FM1,text="Name",font=("times new roman",18,"bold"),bg="#F5F5F5")
        lbl_roll.place(x=0,y=90,anchor="w")
        txt_roll=Entry(self.FM1,  width=17, textvariable=self.Name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=90,anchor="w")

        #***************************************************************************************************

        lbl_roll=Label(self.FM1,text="Email",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=140,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.Email, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=140,anchor="w")
        
        #***************************************************************************************************


        lbl_roll=Label(self.FM1,text="Password",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0,y=190,anchor="w")
        txt_roll=Entry(self.FM1, width=17,textvariable=self.pass_, font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=120,y=190,anchor="w")

        #***************************************************************************************************     

        lbl_roll=Label(self.FM1,text="Contact",bg="#F5F5F5",font=("times new roman",18,"bold"))
        lbl_roll.place(x=0, y=240, anchor="w")
        self.code.set(0)
        combo_code = OptionMenu(self.FM1, self.code,"+93","+355","+213","+1684","+376","+244","+1264","+672","+1268","+54","+374","+297","+61","+880","+32","+226","+359","+387","+1246","+681","+590","+1441","+673","+591","+973","+257","+229","+975","+1876","+267","+685","+599","+55","+1242","+441534","+375","+501","+7","+250","+381","+670","+262","+993","+992","+40","+690","+245","+1671","+502","+30","+240","+590","+81","+592","+441481","+594","+995","+1473","+44","+241","+503","+224","+220","+299","+350","+233","+968","+216","+962","+385","+509","+36","+852""+504","+58","+1787","+1939","+970","+680","+351","+47","+595","+964","+507","+689","+675","+51","+92","+63","+870","+48","+508","+260","+212","+372","+20","+27","+593","+39","+84","+677","+251","+252","+263","+966","+34","+291","+382","+373","+261","+590","+212","+377","+998","+95","+223","+853","+976","+692","+389","+230","+356","+265","+960","+596","+1670","+1664","+222","+441624","+256","+255","+60","+52","+972","+33","+246","+290","+358","+679","+500","+691","+298","+505","+31","+47","+264","+678","+687","+227","+672","+234","+64","+977","+674","+683","+682","+225","+41","+57","+86","+237","+56","+61","+1","+242","+236","+243","+420","+357","+61","+506","+599","+238","+53","+268","+963","+599","+996","+254","+211","+597","+686","+855","+1869","+269","+239","+421","+82","+386","+850","+965","+221","+378","+232","+248","+7","+1345","+65","+46","+249","+1809","1-829","+1767","+253","+45","+1-284","+49","+967","+213","+1","+598","+262","+1","+961","+1758","+856","+688","+886","+1868","+90","+94","+423","+371","+676","+370","+352","+231","+266","+66","+228","+235","+1649","+218","+379","+1784","+971","+376","+1268","+93","+1264","+1340","+354","+98","+374","+355","+244","+1684","+54","+61","+43","+297","+91","+35818","+994","+353","+62","+380","+974","+258" )
        combo_code.place(x=118,y=240,anchor="w")
        txt_roll=Entry(self.FM1, width=14, textvariable=self.contact, font=("times new roman",12,"bold"),bd=5,relief=GROOVE)
        txt_roll.place(x=175,y=240,anchor="w")

        #***************************************************************************************************
                
        lb_gender=Label(self.FM1,text="Role", font=("times new roman",18,"bold"),bg="#F5F5F5")
        lb_gender.place(x=0, y=290, anchor="w")
        combo_gender=ttk.Combobox(self.FM1,textvariable=self.role, width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Service_Provider","Bakers")
        combo_gender.place(x=120, y=290, anchor="w")

        #***************************************************************************************************
        lb_zone=Label(self.FM1,text="ZoneID", font=("times new roman",18,"bold"),bg="#F5F5F5")
        lb_zone.place(x=0,y=345, anchor="w")
        combo_zone=ttk.Combobox(self.FM1, textvariable=self.zoneID,width=17, font=("times new roman",13,"bold"),state='readonly')
        combo_zone['values']=("400066","110001","201010")
        combo_zone.place(x=120,y=345, anchor="w")
        
        lb_Branch=Label(self.FM1,text="BranchID", font=("times new roman",18,"bold"),bg="#F5F5F5")
        lb_Branch.place(x=0, y=390, anchor="w")
        combo_Branch=ttk.Combobox(self.FM1, width=17,textvariable=self.branchID, font=("times new roman",13,"bold"),state='readonly')
        combo_Branch['values']=("12CC","12MU","123UP")
        combo_Branch.place(x=120, y=390, anchor="w")

        
        #****************************************************************************************************

        lbl_roll=Label(self.FM1,image=self.bakery_icon1)
        lbl_roll.place(x=480,y=170)
        
        #***********************************************************************************************



        self.clock()
        

#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       
#-----------------------------------------------Functions-----------------------------------------------------------------------------------       


    def add(self):
        if self.Name.get()=="" and self.pass_.get()=="" and self.Email.get()=="" and self.contact.get()=="" and self.code.get()==0 and self.role.get()=="" and self.zoneID.get()=="" and self.branchID.get()=="" :
            return messagebox.showerror("Error!","All Feilds Required")
        
        if self.Name.get()=='':
            return messagebox.showinfo('Error','Enter a Name')
        
        if self.Email.get()=='':
            return messagebox.showinfo('Error','Enter a Email address')

        if "@" not in self.Email.get():
            return messagebox.showwarning("Warrning","Email should have '@' Character")

            
        if self.pass_.get()=='':
            return messagebox.showinfo('Error','Enter a password')

        if len(str(self.pass_.get()))<8:
            return messagebox.showwarning("Warning","Password should be Minimum 8 charactrs")
        
        if self.contact.get()=='':
            return messagebox.showinfo('Error','Enter a contact')
        
        try:
            tmp=self.contact.get()
            int(tmp)
        except ValueError:
            return messagebox.showinfo('Error','Contact No. Should Be Integer')
        
        if len(self.contact.get()+str(self.code.get()))<10 and len(self.contact.get()+str(self.code.get()))>15:
            return messagebox.showinfo('Error','Enter a valid contact')      
        
        if self.code.get()==0:
            return messagebox.showinfo('Error','Choose Country Code')

        if self.role.get()=="Choose Role":
            return messagebox.showwarning("Warrning","Choose Role Please!!!")

        else:
            if str(self.role.get()) == "Service_Provider":
                self.con2 = str(region_code_for_country_code(self.code.get()))
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
                self.c.execute("CREATE TABLE IF NOT EXISTS Emp(EmpID TEXT PRIMARY KEY ,EmpName TEXT, Email TEXT UNIQUE , Country_Code TEXT , Country TEXT, Phone_No TEXT UNIQUE, Password TEXT, FOREIGN KEY (ZoneID) REFERENCES Zone (Zone_ID),FOREIGN KEY (BranchID) REFERENCES Branch (Branch_ID) )")
                self.find_user = ("SELECT * FROM Emp WHERE Email= ?  or Phone_No = ?")
                self.c.execute(str(self.find_user),(self.Email.get(),self.contact.get()))
                results = (self.c).fetchall()
                if results:
                    messagebox.showerror("Error","Email or Contact  is already Used")
                else:
                    try:
                        self.c.execute("INSERT INTO Emp (EmpID, EmpName, Email, Country_Code, Country, Phone_No, Password, ZoneID, BranchID  ) VALUES (?,?,?,?,?,?,?,?,?)",
                        (self.EID.get(),self.Name.get(),str(self.Email.get()),str(self.code.get()),self.con2,self.contact.get(),self.pass_.get(),self.zoneID.get(),self.branchID.get()))
                        self.conn.commit()
                        self.c.close()
                        self.conn.close()
                        messagebox.showinfo("Successfull","Successfully Added Data")
                        self.clear()
                    except Exception:
                        return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                        self.clear()        
            else:
                self.con2 = str(region_code_for_country_code(self.code.get()))
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
                self.c.execute("CREATE TABLE IF NOT EXISTS Bakers(Baker_ID TEXT PRIMARY KEY ,Name TEXT, Email TEXT UNIQUE , Country_Code TEXT , Country TEXT, Phone_No TEXT UNIQUE, FOREIGN KEY (Zone_ID) REFERENCES Zone (Zone_ID),FOREIGN KEY (BranchID) REFERENCES Branch (Branch_ID) )")
                self.find_user = ("SELECT * FROM Bakers WHERE Email= ?  or Phone_No = ?")
                self.c.execute(str(self.find_user),(self.Email.get(),self.contact.get()))
                results = (self.c).fetchall()
                if results:
                    messagebox.showerror("Error","Email or Contact  is already Used")
                else:
                    try:
                        self.c.execute("INSERT INTO Bakers (Baker_ID, Name, Email, Country_Code, Country, Phone_No, Zone_ID, BranchID  ) VALUES (?,?,?,?,?,?,?,?)",
                        (self.EID.get(),self.Name.get(),str(self.Email.get()),str(self.code.get()),self.con2,self.contact.get(),self.zoneID.get(),self.branchID.get()))
                        self.conn.commit()
                        self.c.close()
                        self.conn.close()
                        messagebox.showinfo("Successfull","Successfully Added Data")
                        self.clear()
                    except Exception:
                        return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
                        self.clear()        

    def update(self):
        if str(self.role.get()) == "Service_Provider":
            try:
                self.con2 = str(region_code_for_country_code(self.code.get()))
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
                self.c.execute("SELECT * from Emp WHERE EmpID="+str(self.EID.get()))
                self.data=self.c.fetchall()
                if self.data:
                        for i in self.data:
                            print(i)
                        a=(str(i[4])) 
                        y=\
                        """UPDATE Emp SET EmpID  =\"""" + self.EID.get()+\
                        """\" , EmpName   =\""""+ self.Name.get()+\
                        """\" , Email    =\""""+ self.Email.get()+\
                        """\" , Country_Code =\""""+ str(self.code.get())+\
                        """\" , Country   =\""""+ str(self.con2)+\
                        """\" , Phone_No  =\""""+ str(self.contact.get()) +\
                        """\" , Password  =\""""+ self.pass_.get() +\
                        """\" , ZoneID   =\""""+ self.zoneID.get()+\
                        """\" , BranchID  =\""""+ self.branchID.get() +\
                        """ \""""
                        y=y+" WHERE EmpID= "+self.EID.get()
                        #print(str(y))              
                        self.c.execute(y)
                        self.conn.commit()
                        return messagebox.showinfo("Info"," Data Updated")
                        self.conn.close()
                else:
                    return messagebox.showerror("Error","Employee ID No not Matched")
            except Exception:
                return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
        
        else:
            try:
                self.con2 = str(region_code_for_country_code(self.code.get()))
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
                self.c.execute("SELECT * from Bakers WHERE Baker_ID="+str(self.EID.get()))
                self.data=self.c.fetchall()
                if self.data:
                        for i in self.data:
                            print(i)
                        a=(str(i[4])) 
                        y=\
                        """UPDATE Emp SET Baker_ID  =\"""" + self.EID.get()+\
                        """\" , Name   =\""""+ self.Name.get()+\
                        """\" , Email    =\""""+ self.Email.get()+\
                        """\" , Country_Code =\""""+ str(self.code.get())+\
                        """\" , Country   =\""""+ str(self.con2)+\
                        """\" , Phone_No  =\""""+ str(self.contact.get()) +\
                        """\" , Zone_ID   =\""""+ self.zoneID.get()+\
                        """\" , BranchID  =\""""+ self.branchID.get() +\
                        """ \""""
                        y=y+" WHERE Baker_ID= "+self.EID.get()
                        #print(str(y))              
                        self.c.execute(y)
                        self.conn.commit()
                        return messagebox.showinfo("Info"," Data Updated")
                        self.conn.close()
                        
                else:
                    return messagebox.showerror("Error","Baker ID No not Matched")
            except Exception:
                        return messagebox.showerror("Error!!","Somthing went wrong not able to add data try again ")
        
    
    def delete(self):
        if self.role.get=="":
            return messagebox.showwarning("Warning","Please Tell Type of role to delete")
        else:
            if self.role.get()== "Service_Provider":
                #try:
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
                self.c.execute("SELECT * from Emp WHERE EmpID="+str(self.EID.get()))
                self.data=self.c.fetchall()
                if self.data:
                    self.c.execute("DELETE FROM Emp WHERE EmpID = " +self.EID.get())
                    self.conn.commit()
                    self.conn.close()
                    messagebox.showinfo("Info","Succesfully Deleted")
                    self.clear()
                else:
                    messagebox.showinfo("Info","Data not Exist")
                    self.clear()
                #except sqlite3.Error as error:
                #    messagebox.showerror("error","Failed to update sqlite table")
            else:
                try:
                    self.conn=sqlite3.connect("bakery.db")
                    self.c=self.conn.cursor()
                    self.c.execute("SELECT * from Bakers WHERE Baker_ID="+str(self.EID.get()))
                    self.data=self.c.fetchall()
                    if self.data:
                        self.c.execute("DELETE FROM Bakers WHERE Baker_ID = " +str(self.EID.get()))
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo("Info","Succesfully Deleted")
                        self.clear()
                    else:
                        messagebox.showinfo("Info","Data not Exist")
                        self.clear()
                except sqlite3.Error as error:
                    messagebox.showerror("error","Failed to update sqlite table")

    def clear(self):
        self.Name.set("")
        self.Email.set("")
        self.pass_.set("")
        self.contact.set("")
        self.code.set(0)
        self.zoneID.set("")
        self.branchID.set("")
        self.role.set("")
        self.EID.set(str(random.randint(1000,999999)))
        
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
