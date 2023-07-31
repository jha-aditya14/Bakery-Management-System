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
        self.orderhis_icon=ImageTk.PhotoImage(file="Pics/user_btn6.png")
        self.order_icon=ImageTk.PhotoImage(file="Pics/user_btn5.jpg")
        self.items_icon=ImageTk.PhotoImage(file="Pics/user_btn2.png")
        self.exit_icon=ImageTk.PhotoImage(file="Pics/user_btn4.jpg")
                
#======================= Variables =================================

        self.searchby=StringVar()
        self.searchval=StringVar()

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
        btn_orderhis = Button(F22,image= self.orderhis_icon,bg=bg_color,relief=RAISED,width =115,height=120,command=self.Search_Items ).place(x=0,y=60,anchor="w")
        btn_order = Button(F23,relief=RAISED,bg=bg_color,image=self.order_icon,width =115,height=120,command=self.buy ).place(x=0,y=60,anchor="w")
        btn_view_items = Button(F24,relief=RAISED,image=self.items_icon,bg=bg_color,width =115,height=120, command=self.view_all).place(x=0,y=60,anchor="w")
        btn_Exit = Button(F25,relief=RAISED,bg=bg_color,image=self.exit_icon,width =115,height=120, command=self.Exit).place(x=0,y=60,anchor="w")

        #------------------------------F3--------------------------------
        F3 = LabelFrame(self.root,bd=5,relief=FLAT,bg="light gray")
        F3.place(x=150,y=100,relwidth=1,height=80 )
        lbl_1= Label(F3,text="Dashboard / Employee",font=("comic sans",15,"italic"),bg="light gray")
        lbl_1.place(x=0,y=0)


#-----------------Main Screen Frames---------------------------------
        
        lb_search=Label(self.root,text="Search By", font=("times new roman",15,"bold"))
        lb_search.place(x=180 ,y=165, anchor="w")
        combo_search=ttk.Combobox(self.root, textvariable=self.searchby,width=17, font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("Bill_No","OrderNo")
        combo_search.place(x=273, y=165, anchor="w")

        self.search1 = Entry(self.root, bd=5,textvariable=self.searchval, bg="lightgrey", font=("times new roman", 18))
        self.search1.place(x=490, y=150,width=200, height=30)

        self.F4 =Frame(self.root,bd=10,relief=SUNKEN)
        self.F4.place(x=180,y=200,width=1130,height=500 )
        
        
        lb_search_btn=Button(self.root,text="Search", bd=6, relief=GROOVE,command=self.search,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=700 ,y=165, height=30,width=200,anchor="w")
        
        lb_search_btn=Button(self.root,text="Clear", bd=6, relief=GROOVE,command=self.clear,font=("times new roman",15,"bold"),fg="yellow",bg="dark blue")
        lb_search_btn.place(x=1110 ,y=163, height=30, width=200,anchor="w")

        Table_Frame=Frame(self.F4,bd=4, relief=RIDGE,bg="#000000")
        Table_Frame.place(x=15,y=0,width=1080,height=480)
        style=ttk.Style(Table_Frame)
        style.configure("Treeview",background="black",fieldbackground="black",foreground="white")


        
        scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
        self.OderHis_table=ttk.Treeview(Table_Frame,columns=("Bill_No","OrderNo","OrderDate","OrderTime","Customer_ID"), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.OderHis_table.yview)
    
        
        self.OderHis_table.column("Bill_No", width=80)
        self.OderHis_table.column("OrderNo", width=100)
        self.OderHis_table.column("OrderDate", width=100)
        self.OderHis_table.column("OrderTime",  width=100)     
        self.OderHis_table.column("Customer_ID", width=100)
  
  
        self.OderHis_table.bind("<ButtonRelease-1>",self.getcursor)
        
        self.fetch_data()
        self.clock()

    def search(self):
        self.OderHis_table.heading("Bill_No", text="Bill_No")
        self.OderHis_table.heading("OrderNo", text="OrderNo")
        self.OderHis_table.heading("OrderDate", text="OrderDate")
        self.OderHis_table.heading("OrderTime", text="OrderTime")
        self.OderHis_table.heading("Customer_ID", text="Customer_ID")
        self.OderHis_table['show']='headings'
  
        self.OderHis_table.pack(fill=BOTH,expand=1)
        self.OderHis_table.bind("<ButtonRelease-1>",self.getcursor)
        self.search_data()

    def search_data(self):
        if self.searchby.get()=="" and self.searchval.get()=="":
            return messagebox.showwarning("Warning","Fields should be filled")
        if self.searchby.get()=="" :
            return messagebox.showwarning("Warning","Shearch By Option Should be filled")
        if self.searchval.get()=="":
            return messagebox.showwarning("Warning","Search box should be filled")
        
        else:
            
            if self.searchby.get() == "Bill_No":
                try:
                    self.conn=sqlite3.connect("bakery.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Order_Hist where Bill_No="+self.searchval.get())
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.OderHis_table.delete(*self.OderHis_table.get_children())
                            for row in rows:
                                    self.OderHis_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()
                    else:
                        return messagebox.showerror("Error","Bill No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
                #self.conn.close()
            if self.searchby.get() == "OrderNo":
                try:
                    self.conn=sqlite3.connect("bakery.db")
                    self.c=self.conn.cursor()
                    self.c.execute("select * from Order_Hist where OrderNo="+self.searchval.get())
                    rows=self.c.fetchall()
                    if len(rows)!=0:
                            self.OderHis_table.delete(*self.OderHis_table.get_children())
                            for row in rows:
                                    self.OderHis_table.insert('',END,values=row)
                            self.conn.commit()
                            self.conn.close()

                    else:
                        return messagebox.showerror("Error","Bill No Not Exist")        
                except Exception:
                    return messagebox.showerror("Error", "Something Wrong")
            

    def fetch_data(self):
        self.conn=sqlite3.connect("bakery.db")
        self.c=self.conn.cursor()
        self.c.execute("select * from Order_Hist")
        rows=self.c.fetchall()
        if len(rows)!=0:
                self.OderHis_table.delete(*self.OderHis_table.get_children())
                for row in rows:
                        self.OderHis_table.insert('',END,values=row)
                self.conn.commit()
        self.conn.close()

    def getcursor(self,ev):
        cursor_row=self.OderHis_table.focus()
        Content=self.OderHis_table.item(cursor_row)
        row=Content['values']
        #print(row)
        self.Item_ID.set(row[0])
        self.Item_name.set(row[1])
        self.Stock_left.set(row[2])
        self.Price.set(row[3])
        

    def clear(self):
        self.OderHis_table.delete(*self.OderHis_table.get_children())
        self.OderHis_table.heading("ItemID", text="")
        self.OderHis_table.heading("Item_name", text="")
        self.OderHis_table.heading("Stock_Left", text="")
        self.OderHis_table.heading("Item_Price", text="")
            
        self.OderHis_table['show']='headings'

    

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
