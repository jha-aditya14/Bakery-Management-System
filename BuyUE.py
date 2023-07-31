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
import tempfile, os

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
#==============================Icons==============================================        
#==============================Icons==============================================        
#==============================Icons==============================================        
     
        self.bg_icon = ImageTk.PhotoImage(file="Pics/x1r4Ao.png")
        bg_lbl = Label(self.root, image = self.bg_icon).pack(fill=Y) # we put image into our window
        
        self.bakery_icon=ImageTk.PhotoImage(file="Pics/Bakery1.jpg")
        self.home_icon=ImageTk.PhotoImage(file="Pics/user_btn1.png")
        self.orderhis_icon=ImageTk.PhotoImage(file="Pics/user_btn6.png")
        self.order_icon=ImageTk.PhotoImage(file="Pics/user_btn5.jpg")
        self.items_icon=ImageTk.PhotoImage(file="Pics/user_btn2.png")
        self.exit_icon=ImageTk.PhotoImage(file="Pics/user_btn4.jpg")
                
#=================================== Variables ============================================
#=================================== Variables ============================================      
#=================================== Variables ============================================
#=================================== Variables ============================================

          
        #------Breads and Cake Variable-------#
        
        self.rusktoast=StringVar()
        self.Pies=StringVar()
        self.Bread=StringVar()
        self.Cakes=StringVar()
        self.pastries=StringVar()
        self.CupcakesandMuffins=StringVar()
        
        #-------Icecreams variable-------#
        
        self.Small_Cone=StringVar()
        self.Large_Cone=StringVar()
        self.Small_Cups=StringVar()
        self.Large_Cups=StringVar()
        self.Stick_Icecream_Small=StringVar()
        self.Stick_Icecream_Large=StringVar()
        
        #-----------softdrink variable--------#
        
        self.maza=StringVar()
        self.fanta=StringVar()
        self.frooti=StringVar()
        self.thumbs_up=StringVar()
        self.limca=StringVar()
        self.sprite=StringVar()
        
        #---- Total Product & Tax Variable--------#
        
        self.cake_price=StringVar()
        self.icecreams_price=StringVar()
        self.soft_drink_price=StringVar()
        
        self.cake_tax=StringVar()
        self.icecream_tax=StringVar()
        self.soft_drink_tax=StringVar()
        
        #------Customer------#
        
        self.c_name=StringVar()
        self.c_phno=StringVar()
        self.bill_no=StringVar()
        self.search_bill=StringVar()
        x=random.randint(1000,99999)
        self.bill_no.set(str(x))
        self.total_bill=StringVar()
        
#============================== F1 ==============================================
#============================== F1 ==============================================        
#============================== F1 ==============================================        
#============================== F1 ==============================================        
        
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

# ==================================F2====================================
# ==================================F2====================================
# ==================================F2====================================
# ==================================F2====================================

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

#==============================F3================================
#==============================F3================================
#==============================F3================================
#==============================F3================================

        F3 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=40 )
        lbl_1= Label(F3,text="Dashboard / Employee",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)

#============================== F4 ================================ 
#============================== F4 ================================
#============================== F4 ================================
#============================== F4 ================================

        F4=LabelFrame(self.root, bd=10, relief=GROOVE, text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F4.place(x=170,y=150, width=1150, height=100)

        cname_lbl=Label(F4,text="Customer Name",bg="#074463", fg="white",font=("times new roman",15, "bold")).grid(row=0,column=0,padx=3,pady=20)
        cname_txt=Entry(F4,width = 15, textvariable=self.c_name,font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=1,pady=5,padx=3)

        cphn_lbl=Label(F4,text="Phone No.",bg="#074463", fg="white",font=("times new roman",15, "bold")).grid(row=0,column=2,padx=3,pady=20)
        cphn_txt=Entry(F4,width = 15, textvariable=self.c_phno, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=3,pady=5,padx=3)

        cbill_lbl=Label(F4,text="Bill Number",bg="#074463", fg="white",font=("times new roman",15, "bold")).grid(row=0,column=4,padx=20,pady=20)
        cbill_txt=Entry(F4,width = 15, textvariable=self.search_bill, font="arial 15",bd=7, relief=SUNKEN).grid(row=0,column=5,pady=10,padx=3)

        bill_btn=Button(F4, text="Search", command=self.find, width=10,bd=7,font="arial 12 bold", cursor="hand2").grid(row=0,column=6, pady=10, padx=20)
        
#============================== F5 ================================ 
#============================== F5 ================================
#============================== F5 ================================
#============================== F5 ================================

        F5=LabelFrame(self.root, bd=10, relief=GROOVE, text="Breads & Cake",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F5.place(x=170,y=250,width=270, height=300)

        c1_lbl=Label(F5, text="Rusktoast",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=8,sticky="w")
        c1=Entry(F5,width=10, textvariable=self.rusktoast,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=8)  
         
        c2_lbl=Label(F5, text="Pies",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=8,sticky="w")
        c2_txt=Entry(F5,width=10, textvariable=self.Pies,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8)  
        
        c3_lbl=Label(F5, text="Bread",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=8,sticky="w")
        c3_txt=Entry(F5,width=10, textvariable=self.Bread, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=8)  
        
        c4_lbl=Label(F5, text="Cake",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=8,sticky="w")
        c4_txt=Entry(F5,width=10, textvariable=self.Cakes, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8)  
        
        c5_lbl=Label(F5, text="Pastries",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,pady=8,sticky="w")
        c5_txt=Entry(F5,width=10, textvariable=self.pastries,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8)  
        
        c6_lbl=Label(F5, text="Cupcakes and Muffins",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,pady=8,sticky="w")
        c6_txt=Entry(F5,width=10, textvariable=self.CupcakesandMuffins, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=8)  
        

#============================== F6 ================================ 
#============================== F6 ================================
#============================== F6 ================================
#============================== F6 ================================

        F6=LabelFrame(self.root, bd=10, relief=GROOVE, text="Icecreams",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F6.place(x=445,y=250,width=270, height=300)

        g1_lbl=Label(F6, text="Cone(Small)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=8,sticky="w")
        g1_txt=Entry(F6,width=10,textvariable=self.Small_Cone,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=8)  
         
        g2_lbl=Label(F6, text="Cone(Large)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=8,sticky="w")
        g2_txt=Entry(F6,width=10,textvariable=self.Large_Cone,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=8)  
        
        g3_lbl=Label(F6, text="Cups(Small)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=8,sticky="w")
        g3=Entry(F6,width=10, textvariable=self.Small_Cups,font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=8)  
        
        g4_lbl=Label(F6, text="Cups(Large)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=8,sticky="w")
        g4_txt=Entry(F6,width=10, textvariable=self.Large_Cups, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=8)  
        
        g5_lbl=Label(F6, text="Stick Iecream(Small)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,pady=8,sticky="w")
        g5_txt=Entry(F6,width=10, textvariable=self.Stick_Icecream_Small, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=8)  
        
        g6_lbl=Label(F6, text="Stick Iecream(Large)",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,pady=8,sticky="w")
        g6_txt=Entry(F6,width=10, textvariable=self.Stick_Icecream_Large, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=8)  
        
#============================== F7 ================================ 
#============================== F7 ================================
#============================== F7 ================================
#============================== F7 ================================

        F7=LabelFrame(self.root, bd=10, relief=GROOVE, text="Soft Drinks",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F7.place(x=700,y=250,width=270, height=300)

        sf1_lbl=Label(F7, text="Maza",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=0,column=0,padx=10,pady=8,sticky="w")
        sf1_txt=Entry(F7,width=10,textvariable=self.maza, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=70,pady=8)  
         
        sf2_lbl=Label(F7, text="Fanta",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=1,column=0,padx=10,pady=8,sticky="w")
        sf2_txt=Entry(F7,width=10, textvariable=self.fanta, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=70,pady=8)  
        
        sf3_lbl=Label(F7, text="Frooti",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=2,column=0,padx=10,pady=8,sticky="w")
        sf3_txt=Entry(F7,width=10,textvariable=self.frooti, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=70,pady=8)  
        
        sf4_lbl=Label(F7, text="Thumbs Up",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=3,column=0,padx=10,pady=8,sticky="w")
        sf4_txt=Entry(F7,width=10,textvariable=self.thumbs_up, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=70,pady=8)  
        
        sf5_lbl=Label(F7, text="Limca",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=4,column=0,padx=10,pady=8,sticky="w")
        sf5_txt=Entry(F7,width=10, textvariable=self.limca, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=70,pady=8)  
        
        sf6_lbl=Label(F7, text="Sprite",font=("times new roman",10,"bold"),bg="#074463",fg="lightgreen").grid(row=5,column=0,padx=10,pady=8,sticky="w")
        sf6_txt=Entry(F7,width=10, textvariable=self.sprite, font=("times new roman",10,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=70,pady=8)  
        
#============================== F8 ================================ 
#============================== F8 ================================
#============================== F8 ================================
#============================== F8 ================================

        F8=Frame(self.root, bd=10, relief=GROOVE)
        F8.place(x=970,y=250,width=350, height=300)
        bill_title=Label(F8,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F8, orient=VERTICAL)
        self.txtarea=Text(F8,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
#============================== F9 ================================ 
#============================== F9 ================================
#============================== F9 ================================
#============================== F9 ================================

        F9=LabelFrame(self.root, bd=10, relief=GROOVE, text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F9.place(x=170,y=560,width=1150, height=140)

        m1_lbl=Label(F9,text="Total Cake & Bread Price ",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=0,column=0,pady=1,sticky="w")
        m1_txt=Entry(F9,width=18, textvariable=self.cake_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=1,pady=1)
        
        m2_lbl=Label(F9,text="Total Icecreams Price",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=1,column=0,pady=1,sticky="w")
        m2_txt=Entry(F9,width=18, textvariable=self.icecreams_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=1,pady=1)
        
        m3_lbl=Label(F9,text="Total Soft Drink Price",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=2,column=0,pady=1,sticky="w")
        m3_txt=Entry(F9,width=18, textvariable=self.soft_drink_price, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=1,pady=1)
        
        c1_lbl=Label(F9,text="Cake Tax",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=0,column=2,pady=1,sticky="w")
        c1_txt=Entry(F9,width=18, textvariable=self.cake_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=0,column=3,pady=1)
        
        c2_lbl=Label(F9,text="Icecream Tax",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=1,column=2,pady=1,sticky="w")
        c2_txt=Entry(F9,width=18, textvariable=self.icecream_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=1,column=3,pady=1)
        
        c3_lbl=Label(F9,text="Soft Drink Tax",bg="#074463", fg="white",font=("times new roman", 14, "bold")).grid(row=2,column=2,pady=1,sticky="w")
        c3_txt=Entry(F9,width=18, textvariable=self.soft_drink_tax, font="arial 10 bold",bd=7, relief=SUNKEN).grid(row=2,column=3,pady=1)
       
#============================== F10 ================================ 
#============================== F10 ================================
#============================== F10 ================================
#============================== F10 ================================
        
        F10=Frame(F9,bd=7,relief=GROOVE)
        F10.place(x=660,width=460, height=105)
        
        total_btn=Button(F10, command=self.total, text="Total", bg="cadetblue",fg="white",activebackground="cadetblue",activeforeground="white",pady=15,width=10,bd=2, font="arial 11 bold").grid(row=0,column=0,padx=5,pady=15)
        GBill_btn=Button(F10, command=self.bill_area, text="Generate Bill", bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 11 bold").grid(row=0,column=1,padx=5,pady=15)
        Clear_btn=Button(F10, text="Clear",command=self.clear_data, bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 11 bold").grid(row=0,column=2,padx=5,pady=15)
        Print_btn=Button(F10, text="Print", command=self.Print, bg="cadetblue",fg="white",pady=15,width=10,bd=2, font="arial 11 bold").grid(row=0,column=3,padx=5,pady=15)
        
        self.rusktoast.set(0)
        self.Pies.set(0)
        self.Bread.set(0)
        self.Cakes.set(0)
        self.pastries.set(0)
        self.CupcakesandMuffins.set(0)
        
        #-------Icecreams variable-------#
        
        self.Small_Cone.set(0)
        self.Large_Cone.set(0)
        self.Small_Cups.set(0)
        self.Large_Cups.set(0)
        self.Stick_Icecream_Small.set(0)
        self.Stick_Icecream_Large.set(0)
        
        #-----------softdrink variable--------#
        
        self.maza.set(0)
        self.fanta.set(0)
        self.frooti.set(0)
        self.thumbs_up.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        
        self.clock()
        
    def total(self):
        if len(self.c_phno.get())<10 :
            return messagebox.showerror("Error","Invalid Contact")
        
        if len(self.c_phno.get())>15 :
            return messagebox.showerror("Error","Invalid Contact")

        try:
            tmp=self.c_phno.get()                
            int(tmp)                
        except ValueError:
            return messagebox.showinfo('Error','Contact must be integer')

        if self.c_name.get()=="" or str(self.c_phno.get())=="":
                messagebox.showerror("Error","Customer details are must!!")

        else:
            self.c_s_p=int(self.rusktoast.get())*120
            self.c_fc_p=int(self.Pies.get())*312
            self.c_fw_p=int(self.pastries.get())*45
            self.c_hs_p=int(self.Bread.get())*35
            self.c_hg_p=int(self.Cakes.get())*750
            self.c_bl_p=int(self.CupcakesandMuffins.get())*151

            self.g_r_p=int(self.Small_Cone.get())*70
            self.g_f_p=int(self.Small_Cups.get())*152
            self.g_d_p=int(self.Stick_Icecream_Small.get())*30
            self.g_w_p=int(self.Large_Cone.get())*155
            self.g_s_p=int(self.Large_Cups.get())*256
            self.g_t_p=int(self.Stick_Icecream_Large.get())*70
            
            self.sd_m_p=int(self.maza.get())*85
            self.sd_f_p=int(self.fanta.get())*85
            self.sd_fr_p=int(self.frooti.get())*92
            self.sd_t_p=int(self.thumbs_up.get())*90
            self.sd_l_p=int(self.limca.get())*87
            self.sd_s_p=int(self.sprite.get())*90


            self.total_cake_price=float(
                                            self.c_s_p+
                                            self.c_fc_p+
                                            self.c_fw_p+
                                            self.c_hs_p+
                                            self.c_hg_p+
                                            self.c_bl_p
                                            )
            self.cake_price.set("Rs. "+str(self.total_cake_price))
            self.c_tax=self.total_cake_price*0.05
            self.cake_tax.set("Rs. "+str(round((self.c_tax),2)))
                        
            self.total_icecreams_price=float(
                                            self.g_r_p+
                                            self.g_f_p+
                                            self.g_d_p+
                                            self.g_w_p+
                                            self.g_s_p+
                                            self.g_t_p
                                            )
                                                            
            self.icecreams_price.set("Rs. "+str(self.total_icecreams_price))
            self.g_tax=self.total_icecreams_price*0.02
            self.icecream_tax.set("Rs. "+str(round((self.g_tax),2)))

            self.total_soft_drinks_price=float(
                                                self.sd_m_p+
                                                self.sd_f_p+
                                                self.sd_fr_p+
                                                self.sd_t_p+
                                                self.sd_l_p+
                                                self.sd_s_p
                                            )
            self.soft_drink_price.set("Rs. "+str(self.total_soft_drinks_price))
            self.sd_tax=self.total_soft_drinks_price*0.019
            self.soft_drink_tax.set("Rs. "+str(round((self.sd_tax),2)))

            self.total_bill=float(self.g_tax+self.sd_tax+self.c_tax+self.total_cake_price+self.total_icecreams_price+self.total_soft_drinks_price)


    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tWelcome Aditya's Bakery Retail\n")
        self.txtarea.insert(END, f"\nBill Number :{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name: {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number :{self.c_phno.get()} ")
        self.txtarea.insert(END, f"\n*************************************")
        self.txtarea.insert(END, f"\nProducts\t\t  Qty\t\tPrice")
        self.txtarea.insert(END, f"\n*************************************")

    def bill_area(self):
        self.root2 = Toplevel()  # Child Window "Tk() can Also be use here"
        self.root2.title("Customer")
        self.root2.geometry("300x70+350+150")
        self.root2.configure(bg="black")
        photo2 = ImageTk.PhotoImage(file = "Pics/bakeryicon.jpg")
        self.root2.iconphoto(False, photo2)
        self.root2.focus_force() 
        self.root2.grab_set()  
        self.root2.resizable(False, False)
    
        old_btn=Button(self.root2, text="OLD CUSTOMER",command=self.bill_area1, bg="blue",fg="gold",relief=GROOVE, font="arial 11 bold").grid(row=0,column=1,padx=5,pady=15)
        new_btn=Button(self.root2, command=self.bill_area2, text="NEW CUSTOMER", bg="blue",fg="gold",relief=GROOVE,font="arial 11 bold").grid(row=0,column=2,padx=5,pady=15)
        
    def bill_area1(self):
        self.root2.destroy()
        
        if len(self.c_phno.get())<10 :
            return messagebox.showerror("Error","Invalid Contact")
        
        if len(self.c_phno.get())>15 :
            return messagebox.showerror("Error","Invalid Contact")

        if self.c_name.get()=="" or self.c_phno.get()=="":
            return messagebox.showerror("Error","Customer details are must!!")

        elif self.cake_price.get()=="Rs. 0.0" and self.icecreams_price.get()=="Rs. 0.0" and self.soft_drink_price.get()=="Rs. 0.0":
            return messagebox.showerror("Error","No Product purchased")

        
        else:
            try:
                a=self.rusktoast.get()
                b=self.Pies.get()
                c=self.pastries.get()
                d=self.Bread.get()
                e=self.Cakes.get()
                f=self.CupcakesandMuffins.get()
                g=self.Small_Cone.get()
                h=self.Small_Cups.get()
                i=self.Stick_Icecream_Small.get()
                j=self.Large_Cone.get()
                k=self.Large_Cups.get()
                l=self.Stick_Icecream_Large.get()
                m=self.maza.get()
                n=self.fanta.get()
                o=self.frooti.get()
                p=self.thumbs_up.get()
                q=self.limca.get()
                r=self.sprite.get()
                
                int(a)
                int(b)
                int(c)
                int(d)
                int(e)
                int(f)
                int(g)
                int(h)
                int(i)
                int(j)
                int(k)
                int(l)
                int(m)
                int(n)
                int(o)
                int(p)
                int(q)
                int(r)
                
            except ValueError:
                return messagebox.showinfo('Error','Quantity must be integer')

            
            try:
                tmp=self.c_phno.get()                
                int(tmp)                
            except ValueError:
                return messagebox.showinfo('Error','Contact must be integer')



            self.welcome_bill()
            if self.rusktoast.get()!=0 :
                self.txtarea.insert(END, f"\nRusk     \t\t  {self.rusktoast.get()}\t   Rs. {self.c_s_p}")
            
            if self.Pies.get()!=0: 
                self.txtarea.insert(END, f"\nPies      \t\t  {self.Pies.get()}\t   Rs. {self.c_fc_p}")
                
            if self.pastries.get()!=0:
                self.txtarea.insert(END, f"\nPastries \t\t  {self.pastries.get()}\t   Rs. {self.c_fw_p}")
                
            if self.Bread.get()!=0: 
                self.txtarea.insert(END, f"\nBread\t\t  {self.Bread.get()}\t   Rs. {self.c_hs_p}")
                
            if self.Cakes.get()!=0: 
                self.txtarea.insert(END, f"\nCakes          \t  {self.Cakes.get()}\t   Rs. {self.c_hg_p}")
                
            if self.CupcakesandMuffins.get()!=0:
                self.txtarea.insert(END, f"\nCupCakes & Muffins {self.CupcakesandMuffins.get()}\t   Rs. {self.c_bl_p}")

        #--------------------------------------------------#

            if self.Small_Cone.get()!=0:
                self.txtarea.insert(END, f"\nSmall Cone\t\t  {self.Small_Cone.get()}\t   Rs. {self.g_r_p}")
            
            if self.Small_Cups.get()!=0: 
                self.txtarea.insert(END, f"\nSmall Cups  \t\t  {self.Small_Cups.get()}\t   Rs. {self.g_f_p}")

            if self.Stick_Icecream_Small.get()!=0:
                self.txtarea.insert(END, f"\nStick Icecreame Small  {self.Stick_Icecream_Small.get()}\t   Rs. {self.g_d_p}")
            
            if self.Large_Cone.get()!=0: 
                self.txtarea.insert(END, f"\nLarge Cone  \t\t  {self.Large_Cone.get()}\t   Rs. {self.g_w_p}")

            if self.Large_Cups.get()!=0:
                self.txtarea.insert(END, f"\nLarge Cups \t \t  {self.Large_Cups.get()}\t   Rs. {self.g_s_p}")
            
            if self.Stick_Icecream_Large.get()!=0: 
                self.txtarea.insert(END, f"\nStick Icecream Large  {self.Stick_Icecream_Large.get()}\t   Rs. {self.g_t_p}")
                
            
    #------------------------------------------------------------------#

            if self.maza.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.maza.get()}\t   Rs. {self.sd_m_p}")
            
            if self.fanta.get()!=0:
                self.txtarea.insert(END, f"\nFanta\t\t  {self.fanta.get()}\t   Rs. {self.sd_f_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END, f"\nFrooti\t\t  {self.frooti.get()}\t   Rs. {self.sd_fr_p}")
            
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END, f"\nThumbs Uo\t\t  {self.thumbs_up.get()}\t   Rs. {self.sd_t_p}")
            
            if self.limca.get()!=0:
                self.txtarea.insert(END, f"\nLimca\t\t  {self.limca.get()}\t   Rs. {self.sd_l_p}")
            
            if self.sprite.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.sprite.get()}\t   Rs. {self.sd_s_p}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")


            if self.cake_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCakes and Bread Tax  \t\t   {self.cake_tax.get()}")
            
            if self.icecream_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nIcecreams Tax\t\t\t   {self.icecream_tax.get()}")
            
            if self.soft_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nSoft Drink Tax\t\t\t   {self.soft_drink_tax.get()}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\tRs. {str(self.total_bill)}")

            self.L=[]
            self.conn = sqlite3.connect("bakery.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT Stock_Left FROM Stock" )
            self.data3 = self.c.fetchall()
            for i in self.data3:
                self.L.append(str(i))
           
            string1 = str(self.L[0])
            string2 = str(self.L[1])
            string3 = str(self.L[2])
            string4 = str(self.L[3])
            string5 = str(self.L[4])
            string6 = str(self.L[5])
            string7 = str(self.L[6])
            string8 = str(self.L[7])
            string9 = str(self.L[8])
            string10 = str(self.L[9])
            string11 = str(self.L[10])
            string12 = str(self.L[11])
            string13 = str(self.L[12])
            string14 = str(self.L[13])
            string15 = str(self.L[14])
            string16= str(self.L[15])
            string17 = str(self.L[16])
            string18 = str(self.L[17])
            
            a1 = str(int(re.search(r'\d+', string1).group())-int(self.Stick_Icecream_Small.get()))
            a2 = str(int(re.search(r'\d+', string2).group())-int(self.Large_Cups.get()))
            a3 = str(int(re.search(r'\d+', string3).group())-int(self.Small_Cups.get()))
            a4 = str(int(re.search(r'\d+', string4).group())-int(self.Large_Cone.get()))
            a5 = str(int(re.search(r'\d+', string5).group())-int(self.Small_Cone.get()))
            a6 = str(int(re.search(r'\d+', string6).group())-int(self.pastries.get()))
            
            a7 = str(int(re.search(r'\d+', string7).group())-int(self.Cakes.get()))
            a8 = str(int(re.search(r'\d+', string8).group())-int(self.Bread.get()))
            a9 = str(int(re.search(r'\d+', string9).group())-int(self.Pies.get()))
            a10 = str(int(re.search(r'\d+', string10).group())-int(self.rusktoast.get()))
            a11 = str(int(re.search(r'\d+', string11).group())-int(self.sprite.get()))
            a12 = str(int(re.search(r'\d+', string12).group())-int(self.limca.get()))
            
            a13 = str(int(re.search(r'\d+', string13).group())-int(self.thumbs_up.get()))
            a14 = str(int(re.search(r'\d+', string14).group())-int(self.frooti.get()))
            a15 = str(int(re.search(r'\d+', string15).group())-int(self.fanta.get()))
            a16 = str(int(re.search(r'\d+', string16).group())-int(self.maza.get()))
            a17 = str(int(re.search(r'\d+', string17).group())-int(self.Stick_Icecream_Large.get()))
            a18 = str(int(re.search(r'\d+', string18).group())-int(self.CupcakesandMuffins.get()))
            
            if int(a1)<0 or int(a2)<0 or int(a3)<0 or int(a4)<0 or int(a5)<0 or int(a6)<0 or  int(a7)<0 or int(a8)<0 or int(a9)<0 or int(a10)<0 or int(a11)<0 or int(a12)<0 or int(a13)<0 or int(a14)<0 or int(a15)<0 or int(a16)<0 or int(a17)<0 or int(a18)<0 :
                return messagebox.showerror("Error","Any of Your Product is Out of Stock or Quantity is more according to stock")
            else:
                
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()

                self.c.execute("DROP TABLE Stock")
                    
                self.c.execute("CREATE TABLE IF NOT EXISTS Stock(ItemID TEXT PRIMARY KEY, ItemName TEXT NOT NULL, Stock_Left TEXT, Item_Price TEXT)")
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SS1012","Small_Stick_Icecream",str(a1),"30"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LGC1011","Large_Cups",str(a2),"256"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SCU1010","Small_Cups",str(a3),"152"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LG1009","Large_Cone",str(a4),"155"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SC1008","Small_Cone",str(a5),"70"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PA1007","Pastries",str(a6),"45"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("C10066","Cakes",str(a7),"750"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("BR1005","Bread",str(a8),"35"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PI1004","Pies",str(a9),"312"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("RT1003","Rusk_Toast",str(a10),"120"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("S345","Sprite",str(a11),"90"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("L435","Limca",str(a12),"87"))
                        
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("TU555","Thumbs_Up",str(a13),"90"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("FR65","Frooti",str(a14),"92"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("F788","Fanta",str(a15),"85"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("M908","Maza",str(a16),"85"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LS1013","Large_Stick_Icecream",str(a17),"70"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("CM1020","CupCake_Muffins",str(a18),"151"))
                
                self.conn.commit()

            
            self.save_bill1()

    def bill_area2(self):
        self.root2.destroy()
        
        if len(self.c_phno.get())<10 :
            return messagebox.showerror("Error","Invalid Contact")
        
        if len(self.c_phno.get())>15 :
            return messagebox.showerror("Error","Invalid Contact")

        if self.c_name.get()=="" or self.c_phno.get()=="":
            return messagebox.showerror("Error","Customer details are must!!")

        elif self.cake_price.get()=="Rs. 0.0" and self.icecreams_price.get()=="Rs. 0.0" and self.soft_drink_price.get()=="Rs. 0.0":
            return messagebox.showerror("Error","No Product purchased")

        
        else:
            try:
                a=self.rusktoast.get()
                b=self.Pies.get()
                c=self.pastries.get()
                d=self.Bread.get()
                e=self.Cakes.get()
                f=self.CupcakesandMuffins.get()
                g=self.Small_Cone.get()
                h=self.Small_Cups.get()
                i=self.Stick_Icecream_Small.get()
                j=self.Large_Cone.get()
                k=self.Large_Cups.get()
                l=self.Stick_Icecream_Large.get()
                m=self.maza.get()
                n=self.fanta.get()
                o=self.frooti.get()
                p=self.thumbs_up.get()
                q=self.limca.get()
                r=self.sprite.get()
                
                int(a)
                int(b)
                int(c)
                int(d)
                int(e)
                int(f)
                int(g)
                int(h)
                int(i)
                int(j)
                int(k)
                int(l)
                int(m)
                int(n)
                int(o)
                int(p)
                int(q)
                int(r)
                
            except ValueError:
                return messagebox.showinfo('Error','Quantity must be integer')

            
            try:
                tmp=self.c_phno.get()                
                int(tmp)                
            except ValueError:
                return messagebox.showinfo('Error','Contact must be integer')



            self.welcome_bill()
            if self.rusktoast.get()!=0 :
                self.txtarea.insert(END, f"\nRusk     \t\t  {self.rusktoast.get()}\t   Rs. {self.c_s_p}")
            
            if self.Pies.get()!=0: 
                self.txtarea.insert(END, f"\nPies      \t\t  {self.Pies.get()}\t   Rs. {self.c_fc_p}")
                
            if self.pastries.get()!=0:
                self.txtarea.insert(END, f"\nPastries \t\t  {self.pastries.get()}\t   Rs. {self.c_fw_p}")
                
            if self.Bread.get()!=0: 
                self.txtarea.insert(END, f"\nBread\t\t  {self.Bread.get()}\t   Rs. {self.c_hs_p}")
                
            if self.Cakes.get()!=0: 
                self.txtarea.insert(END, f"\nCakes          \t  {self.Cakes.get()}\t   Rs. {self.c_hg_p}")
                
            if self.CupcakesandMuffins.get()!=0:
                self.txtarea.insert(END, f"\nCupCakes & Muffins {self.CupcakesandMuffins.get()}\t   Rs. {self.c_bl_p}")

        #--------------------------------------------------#

            if self.Small_Cone.get()!=0:
                self.txtarea.insert(END, f"\nSmall Cone\t\t  {self.Small_Cone.get()}\t   Rs. {self.g_r_p}")
            
            if self.Small_Cups.get()!=0: 
                self.txtarea.insert(END, f"\nSmall Cups  \t\t  {self.Small_Cups.get()}\t   Rs. {self.g_f_p}")

            if self.Stick_Icecream_Small.get()!=0:
                self.txtarea.insert(END, f"\nStick Icecreame Small  {self.Stick_Icecream_Small.get()}\t   Rs. {self.g_d_p}")
            
            if self.Large_Cone.get()!=0: 
                self.txtarea.insert(END, f"\nLarge Cone  \t\t  {self.Large_Cone.get()}\t   Rs. {self.g_w_p}")

            if self.Large_Cups.get()!=0:
                self.txtarea.insert(END, f"\nLarge Cups \t \t  {self.Large_Cups.get()}\t   Rs. {self.g_s_p}")
            
            if self.Stick_Icecream_Large.get()!=0: 
                self.txtarea.insert(END, f"\nStick Icecream Large  {self.Stick_Icecream_Large.get()}\t   Rs. {self.g_t_p}")
                
            
    #------------------------------------------------------------------#

            if self.maza.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.maza.get()}\t   Rs. {self.sd_m_p}")
            
            if self.fanta.get()!=0:
                self.txtarea.insert(END, f"\nFanta\t\t  {self.fanta.get()}\t   Rs. {self.sd_f_p}")

            if self.frooti.get()!=0:
                self.txtarea.insert(END, f"\nFrooti\t\t  {self.frooti.get()}\t   Rs. {self.sd_fr_p}")
            
            if self.thumbs_up.get()!=0:
                self.txtarea.insert(END, f"\nThumbs Uo\t\t  {self.thumbs_up.get()}\t   Rs. {self.sd_t_p}")
            
            if self.limca.get()!=0:
                self.txtarea.insert(END, f"\nLimca\t\t  {self.limca.get()}\t   Rs. {self.sd_l_p}")
            
            if self.sprite.get()!=0:
                self.txtarea.insert(END, f"\nMaza\t\t  {self.sprite.get()}\t   Rs. {self.sd_s_p}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")


            if self.cake_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nCakes and Bread Tax  \t\t   {self.cake_tax.get()}")
            
            if self.icecream_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nIcecreams Tax\t\t\t   {self.icecream_tax.get()}")
            
            if self.soft_drink_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END, f"\nSoft Drink Tax\t\t\t   {self.soft_drink_tax.get()}")
            
            self.txtarea.insert(END, f"\n-------------------------------------")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\tRs. {str(self.total_bill)}")

            self.L1=[]           
            self.conn = sqlite3.connect("bakery.db")
            self.c = self.conn.cursor()
            self.c.execute("SELECT Stock_Left FROM Stock" )
            self.data3 = self.c.fetchall()
            for i in self.data3:
                self.L1.append(str(i))
           
            string1 = str(self.L1[0])
            string2 = str(self.L1[1])
            string3 = str(self.L1[2])
            string4 = str(self.L1[3])
            string5 = str(self.L1[4])
            string6 = str(self.L1[5])
            string7 = str(self.L1[6])
            string8 = str(self.L1[7])
            string9 = str(self.L1[8])
            string10 = str(self.L1[9])
            string11 = str(self.L1[10])
            string12 = str(self.L1[11])
            string13 = str(self.L1[12])
            string14 = str(self.L1[13])
            string15 = str(self.L1[14])
            string16= str(self.L1[15])
            string17 = str(self.L1[16])
            string18 = str(self.L1[17])
            
            a1 = str(int(re.search(r'\d+', string1).group())-int(self.Stick_Icecream_Small.get()))
            a2 = str(int(re.search(r'\d+', string2).group())-int(self.Large_Cups.get()))
            a3 = str(int(re.search(r'\d+', string3).group())-int(self.Small_Cups.get()))
            a4 = str(int(re.search(r'\d+', string4).group())-int(self.Large_Cone.get()))
            a5 = str(int(re.search(r'\d+', string5).group())-int(self.Small_Cone.get()))
            a6 = str(int(re.search(r'\d+', string6).group())-int(self.pastries.get()))
            
            a7 = str(int(re.search(r'\d+', string7).group())-int(self.Cakes.get()))
            a8 = str(int(re.search(r'\d+', string8).group())-int(self.Bread.get()))
            a9 = str(int(re.search(r'\d+', string9).group())-int(self.Pies.get()))
            a10 = str(int(re.search(r'\d+', string10).group())-int(self.rusktoast.get()))
            a11 = str(int(re.search(r'\d+', string11).group())-int(self.sprite.get()))
            a12 = str(int(re.search(r'\d+', string12).group())-int(self.limca.get()))
            
            a13 = str(int(re.search(r'\d+', string13).group())-int(self.thumbs_up.get()))
            a14 = str(int(re.search(r'\d+', string14).group())-int(self.frooti.get()))
            a15 = str(int(re.search(r'\d+', string15).group())-int(self.fanta.get()))
            a16 = str(int(re.search(r'\d+', string16).group())-int(self.maza.get()))
            a17 = str(int(re.search(r'\d+', string17).group())-int(self.Stick_Icecream_Large.get()))
            a18 = str(int(re.search(r'\d+', string18).group())-int(self.CupcakesandMuffins.get()))
            
            if int(a1)<0 or int(a2)<0 or int(a3)<0 or int(a4)<0 or int(a5)<0 or int(a6)<0 or  int(a7)<0 or int(a8)<0 or int(a9)<0 or int(a10)<0 or int(a11)<0 or int(a12)<0 or int(a13)<0 or int(a14)<0 or int(a15)<0 or int(a16)<0 or int(a17)<0 or int(a18)<0 :
                return messagebox.showerror("Error","Any of Your Product is Out of Stock or Quantity is more according to stock")
            else:
                self.conn=sqlite3.connect("bakery.db")
                self.c=self.conn.cursor()
    
                self.c.execute("DROP TABLE Stock")
                    
                self.c.execute("CREATE TABLE IF NOT EXISTS Stock(ItemID , ItemName, Stock_Left, Item_Price)")
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SS1012","Small_Stick_Icecream",str(a1),"30"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LGC1011","Large_Cups",str(a2),"256"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SCU1010","Small_Cups",str(a3),"152"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LG1009","Large_Cone",str(a4),"155"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("SC1008","Small_Cone",str(a5),"70"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PA1007","Pastries",str(a6),"45"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("C10066","Cakes",str(a7),"750"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("BR1005","Bread",str(a8),"35"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("PI1004","Pies",str(a9),"312"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("RT1003","Rusk_Toast",str(a10),"120"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("S345","Sprite",str(a11),"90"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("L435","Limca",str(a12),"87"))
                        
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("TU555","Thumbs_Up",str(a13),"90"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("FR65","Frooti",str(a14),"92"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("F788","Fanta",str(a15),"85"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("M908","Maza",str(a16),"85"))

                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("LS1013","Large_Stick_Icecream",str(a17),"70"))
                
                self.c.execute("INSERT INTO Stock (ItemID , ItemName, Stock_Left, Item_Price) VALUES (?,?,?,?)",
                ("CM1020","CupCake_Muffins",str(a18),"151"))
                
                self.conn.commit()

                
            self.save_bill2()


    def save_bill1(self):
        now = datetime.now()
        self.Time=now.strftime('%H:%M:%S')
        self.Today= now.strftime("%d-%m-%Y")
        self.order = str(random.randint(10000,999999))
        try:
            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            self.c.execute("SELECT UID FROM user WHERE Phone_No =" +str(self.c_phno.get()))
            self.result = (self.c).fetchall()
            #print(self.result)
            self.a = (str(self.result)).split("[(\'")[1]
            self.b = (str(self.a)).split("\',)]")[0]
            #print(self.b)
            self.c.execute("INSERT INTO Order_Hist(Bill_No ,OrderNo, OrderDate ,OrderTime, Customer_ID, Total_Amt_Paid) VALUES (?,?,?,?,?,?)",(self.bill_no.get(),self.order,str(self.Today),str(self.Time),str(self.b), str(self.total_bill)))
            self.conn.commit()

        except Exception:
            return messagebox.showerror("Error","Enter Valid Phone Number through which Your Id is registered")    
            
        op=messagebox.askyesnocancel("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END) 
            f1=open("Bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def save_bill2(self):
        now = datetime.now()
        self.Time=now.strftime('%H:%M:%S')
        self.Today= now.strftime("%d-%m-%Y")
        self.order = str(random.randint(10000,999999))
        self.b = str(self.c_name.get())+str(random.randint(1000,9999))
        try:   
            self.conn=sqlite3.connect("bakery.db")
            self.c=self.conn.cursor()
            self.c.execute("INSERT INTO CusOFFline(NUID, NUname, Phone_No) VALUES (?,?,?)",(str(self.b), str(self.c_name.get()), str(self.c_phno.get())))
            self.c.execute("INSERT INTO Order_HistN(NBill_No ,OrderNo, OrderDate ,OrderTime, NUID, Total_Amt_Paid) VALUES (?,?,?,?,?,?)",(self.bill_no.get(),self.order,str(self.Today),str(self.Time),str(self.b), str(self.total_bill)))
            self.conn.commit()

        except Exception:
            return messagebox.showerror("Error","Enter Valid Phone Number through which Your Id is registered")    
            
        op=messagebox.askyesnocancel("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END) 
            f1=open("Billstemp/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. : {self.bill_no.get()} Saved Successfully")
        else:
            return

    def clear_data(self):
        op=messagebox.askyesnocancel("Clear","Do you really want to Clear?")   
        if op>0:
            self.rusktoast.set(0)
            self.Pies.set(0)
            self.Bread.set(0)
            self.Cakes.set(0)
            self.pastries.set(0)
            self.CupcakesandMuffins.set(0)
            
            #-------Icecreams variable-------#
            
            self.Small_Cone.set(0)
            self.Large_Cone.set(0)
            self.Small_Cups.set(0)
            self.Large_Cups.set(0)
            self.Stick_Icecream_Small.set(0)
            self.Stick_Icecream_Large.set(0)
            
            #-----------softdrink variable--------#
            
            self.maza.set(0)
            self.fanta.set(0)
            self.frooti.set(0)
            self.thumbs_up.set(0)
            self.limca.set(0)
            self.sprite.set(0)

            self.cake_price.set("")
            self.icecreams_price.set("")
            self.soft_drink_price.set("")
            
            self.cake_tax.set("")
            self.icecream_tax.set("")
            self.soft_drink_tax.set("")


            self.c_name.set("")
            self.c_phno.set("")
            self.bill_no.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str())

            self.txtarea.delete("1.0",END)

        else:
            pass    
            

    def Print(self):
        a = self.txtarea.get("1.0", "end-1c") # can use END
        filename = tempfile.mktemp(".txt") #can take txt 
        open(filename,"w").write(a)
        os.startfile(filename,"print") 


    def find(self):
        present="no"
        for i in os.listdir("Billstemp/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"Billstemp/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No.")
           

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
