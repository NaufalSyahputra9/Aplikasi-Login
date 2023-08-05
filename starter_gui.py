# Register and Login GUI for Water Intake Tracker App
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import os
import re
import time
import datetime as dt

if os.path.isfile(r'E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\data_user.txt'):
    with open(r'E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\data_user.txt', 'r') as f:
        alls = f.read().split('\n')
        alls = [x for x in alls if x.strip()]

def validator(password):
        c = 0
        if len(password) >= 8:
            c+=1
        if re.search('[0-9]+', password):
            c += 1
        if re.search('[a-z]', password):
            c+=1
        if re.search('[A-Z]', password):
            c+=1

        if c == 4:
            return True

class Register(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Register page")
        self.geometry("1200x650")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)  
        self.configure(fg_color='#F2FAFF')

        self.main_frame = ctk.CTkFrame(self, fg_color='white', 
                                        width=480, height=570, 
                                        border_color='black', border_width=1,
                                        corner_radius=5)
        self.main_frame.place(x=370, y=35)

        self.title_frame = ctk.CTkLabel(self.main_frame, 
                                        text='Get Started',
                                        font=('Lucida Sans', 40, 'bold'),
                                        fg_color='white',
                                        width=100,
                                        justify='center')
        self.title_frame.place(x=120, y=30)

        self.label_name = ctk.CTkLabel(self.main_frame, 
                                        text='Username',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_name.place(x=60, y=90)

        self.name_entry = ctk.CTkEntry(self.main_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.name_entry.place(x=60, y=120)

        self.label_email = ctk.CTkLabel(self.main_frame, 
                                        text='Email',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_email.place(x=60, y=190)

        self.email_entry = ctk.CTkEntry(self.main_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.email_entry.place(x=60, y=220)

        self.label_pass = ctk.CTkLabel(self.main_frame, 
                                        text='Password',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_pass.place(x=60, y=290)

        self.pass_entry = ctk.CTkEntry(self.main_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6',
                                     placeholder_text='8 characters, number, lowercase, uppercase'
                                    )
        self.pass_entry.place(x=60, y=320)

        self.label_confirm = ctk.CTkLabel(self.main_frame, 
                                        text='Confirm Password',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_confirm.place(x=60, y=390)

        self.confirm_entry = ctk.CTkEntry(self.main_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6',
                                     placeholder_text='8 characters, number, lowercase, uppercase'
                                    )
        self.confirm_entry.place(x=60, y=420)

        self.regist_button = ctk.CTkButton(self.main_frame, 
                                        text='Register',
                                        font=('Lucida Sans', 16, 'bold'),
                                        fg_color='#1520A6',
                                        width=360,
                                        height=50,
                                        text_color='white',
                                        corner_radius=5,
                                        hover_color='#1338BE',
                                        command=self.check)
        self.regist_button.place(x=60, y=495)


        self.back_button = ctk.CTkButton(self,
                                         text='Back',
                                         width=60,
                                         height=40,
                                         font=('Lucida Sans', 15, 'bold'),
                                         fg_color='#1520A6',
                                         text_color='white',
                                         command=self.login
        )
        self.back_button.place(x=20, y=590)
    
    def check(self):
        username = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.pass_entry.get().strip()
        confirm = self.confirm_entry.get().strip()

        emails = [x.split(',')[1] for x in alls]
        names = [x.split(',')[0] for x in alls]

        if username == '' or email == '' or password == '' or confirm == '':
            messagebox.showerror('Error', 'All fields are required', parent=self)
        elif len(username) > 15:
            messagebox.showerror('Error', 'Username too long!', parent=self)
        elif len(username) < 3:
            messagebox.showerror('Error', 'Username too short!', parent=self)
        elif len(re.findall('\S+@\S+', email)) == 0:
            messagebox.showerror('Error', 'Email not valid!', parent=self)
        elif email in emails:
            messagebox.showerror('Error', 'Email already exist!', parent=self)
        elif username in names:
            messagebox.showerror('Error', 'Username already exist!', parent=self)
        elif validator(password) != True:
            messagebox.showerror('Error', 'Password must contain at least 8 characters, number, uppercase and lowercase letter', parent=self)
        elif password != confirm:
            messagebox.showerror('Error', 'Passwords do not match', parent=self)
        else:
            time = str(dt.datetime.now())
            data = [username, email, password, time]
            alls.append(','.join(data))
            with open(r'E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\data_user.txt', 'r+') as db:
                for single in alls:
                    db.write(f"{single}\n")
            
            try:
                with open(r"E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\database\\"+username+".txt", 'x') as f:
                    user_input = [','.join(data),
                                  'goal :',
                                  'intake :',
                                  'age :',
                                  'weight :',
                                  'activity :',
                                  'image :',
                                  'reward :'
                                  ]
                    for _ in user_input:
                        f.write(_+'\n')
            except:
                messagebox.showerror('Error', 'Username already exist!', parent=self)

            messagebox.showinfo('Info', 'Register successfull')

            self.login()

    def login(self):
        time.sleep(0.5)
        self.destroy()
        
        app = Login()
        app.mainloop()

class ResetPassword(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Reset password page")
        self.geometry("370x450")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)  
        self.configure(fg_color='#c4c6f5')
        self.title = ctk.CTkLabel(self,
                                  text='Reset Password',
                                  font=('Lucida Sans', 30, 'bold'),
                                  fg_color='#c4c6f5')
        self.title.place(x=65, y=30)

        self.label_user = ctk.CTkLabel(self, 
                                        text='Email or Username',
                                        font=('Lucida Sans', 15),
                                        fg_color='#c4c6f5',
                                        text_color='black')
        self.label_user.place(x=35, y=90)

        self.user_entry = ctk.CTkEntry(self, 
                                     width=300,
                                     height=45,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.user_entry.place(x=35, y=120)

        self.label_new_pass = ctk.CTkLabel(self, 
                                        text='New password',
                                        font=('Lucida Sans', 15),
                                        fg_color='#c4c6f5',
                                        text_color='black')
        self.label_new_pass.place(x=35, y=180)

        self.new_pass_entry = ctk.CTkEntry(self, 
                                     width=300,
                                     height=45,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.new_pass_entry.place(x=35, y=210)

        self.label_new_confirm = ctk.CTkLabel(self, 
                                        text='Confirm new password',
                                        font=('Lucida Sans', 15),
                                        fg_color='#c4c6f5',
                                        text_color='black')
        self.label_new_confirm.place(x=35, y=280)

        self.new_confirm_entry = ctk.CTkEntry(self, 
                                     width=300,
                                     height=45,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.new_confirm_entry.place(x=35, y=310)

        self.change_button = ctk.CTkButton(self, 
                                        text='SUMBIT',
                                        font=('Lucida Sans', 16, 'bold'),
                                        fg_color='#5ba6c9',
                                        width=300,
                                        height=45,
                                        text_color='black',
                                        corner_radius=5,
                                        hover_color='#75bee0',
                                        command=self.change_password)
        self.change_button.place(x=35, y=380)
    
    def change_password(self):
        user = self.user_entry.get().strip()
        password = self.new_pass_entry.get().strip()
        confirm = self.new_confirm_entry.get().strip()

        emails = [x.split(',')[1] for x in alls]
        names = [x.split(',')[0] for x in alls]

        if user == '' or password == '' or confirm == '':
            messagebox.showerror('Error', 'All fields are required', parent=self)
        elif '@' in user and user not in emails:
            messagebox.showerror('Error', "Email doesn't exists", parent=self)
        elif '@' not in user and user not in names:
            messagebox.showerror('Error', "Username doesn't exists", parent=self)
        elif validator(password) != True:
            messagebox.showerror('Error', 'Password must contain at least 8 characters, number, uppercase and lowercase letter', parent=self)
        elif password != confirm:
            messagebox.showerror('Error', 'Passwords do not match', parent=self)
        else:
            for each in alls:
                username2, email2, password2, time = each.split(',')
                if user == email2 or user == username2:
                    messagebox.showinfo('Info', "Reset password successfull", parent=self)                 
                    pos = alls.index(each)
                    self.result = [username2, email2, password, time]
                    alls[pos] = ','.join(self.result)
                    with open(r'E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\data_user.txt', 'r+') as db:
                        for single in alls:
                            db.write(f"{single}\n")
                    
                    with open(r"E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\database\\"+username2+".txt", 'r+') as f:
                        users = f.readlines()
                        users[0] = ','.join(self.result)+'\n'
                    
                    with open(r"E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\database\\"+username2+".txt", 'r+') as f:
                        for _ in users:
                            f.write(_)

                    self.destroy()
                    break

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login page")
        self.geometry("1200x650")
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.destroy)  
        self.configure(fg_color='#F2FAFF')
        self.start = False
        self.result = None
        

        # Adding widgets in right side

        self.right_frame = ctk.CTkFrame(self, fg_color='white', 
                                        width=500, height=450, 
                                        border_color='black', border_width=1)
        self.right_frame.place(x=600, y=80)

        self.title_frame = ctk.CTkLabel(self.right_frame, 
                                        text='Login Here',
                                        font=('Lucida Sans', 40, 'bold'),
                                        fg_color='white')
        self.title_frame.place(x=37, y=30)

        self.title_member = ctk.CTkLabel(self.right_frame, 
                                        text='Members Login Area',
                                        font=('Lucida Sans', 15),
                                        fg_color='white')
        self.title_member.place(x=40, y=90)

        self.label_email = ctk.CTkLabel(self.right_frame, 
                                        text='Email or Username',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_email.place(x=40, y=140)

        self.email_entry = ctk.CTkEntry(self.right_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6'
                                    )
        self.email_entry.place(x=40, y=170)

        self.label_password = ctk.CTkLabel(self.right_frame, 
                                        text='Password',
                                        font=('Lucida Sans', 15),
                                        fg_color='white',
                                        text_color='#363636')
        self.label_password.place(x=40, y=240)

        self.password_entry = ctk.CTkEntry(self.right_frame, 
                                     width=360,
                                     height=50,
                                     border_width=1,
                                     font=('Lucida Sans', 15),
                                     corner_radius=0,
                                     fg_color='#E7E6E6',
                                     show='*'
                                    )
        self.password_entry.place(x=40, y=270)

        self.closeeye_img = ctk.CTkImage(light_image=Image.open(r"E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\closeeye.png"), 
                               size=(26, 24))

        self.openeye_img = ctk.CTkImage(light_image=Image.open(r"E:\BACKUP C\DOCUMENTS\journey of coding python mmmm\02 Template\water tracker\openeye.png"), 
                               size=(26, 24))
        
        self.hide_button = ctk.CTkButton(self.right_frame,
                                         image=self.closeeye_img,
                                         text='',
                                         width=10,
                                         height=32,
                                         corner_radius=0,
                                         hover='disabled',
                                         fg_color='#E7E6E6',
                                         command=self.show)
        self.hide_button.place(x=350, y=280)

        self.new_window = None

        self.forgot_password = ctk.CTkButton(self.right_frame, 
                                        text='I forgot my password',
                                        font=('Lucida Sans', 14, 'bold'),
                                        fg_color='transparent',
                                        text_color='#1520A6',
                                        corner_radius=5,
                                        hover_color='white',
                                        command=self.forgot_window)
        self.forgot_password.place(x=40, y=340)

        self.login_button = ctk.CTkButton(self.right_frame, 
                                        text='Login',
                                        font=('Lucida Sans', 16, 'bold'),
                                        fg_color='#1520A6',
                                        width=80,
                                        height=40,
                                        text_color='white',
                                        corner_radius=5,
                                        hover_color='#1338BE',
                                        command=self.run)
        self.login_button.place(x=40, y=380)

        # Register widgets
        self.register_frame = ctk.CTkFrame(self, fg_color='transparent', width=100, height=40)
        self.register_frame.place(x=640, y=550)

        self.label_register = ctk.CTkLabel(self.register_frame, 
                                        text='Not a member yet?',
                                        font=('Lucida Sans', 15),
                                        fg_color='transparent',
                                        text_color='black')
        self.label_register.pack(side='left')

        self.regist_button = ctk.CTkButton(self.register_frame, 
                                        text='Register',
                                        font=('Lucida Sans', 15, 'bold', 'underline'),
                                        fg_color='transparent',
                                        width=5,
                                        text_color='#1520A6',
                                        corner_radius=5,
                                        hover_color='#F2FAFF',
                                        command=self.start_register)
        self.regist_button.pack(side='right')

        # Adding widgets in left side

        self.left_frame = ctk.CTkFrame(self, fg_color='white', width=550, height=650, border_color='black', border_width=5)
        self.left_frame.place(x=0, y=0)

        self.main_img = ctk.CTkImage(light_image=Image.open(r"C:\Users\ASUS\Pictures\Screenshots\drink2.png"),
                        size=(550, 720))

        text_bottom = "Track your daily water intake\nwith just a few taps!"
        title = 'Water Intake Tracker'

        self.label_main_img = ctk.CTkLabel(self.left_frame, 
                                           image=self.main_img, 
                                           text='\n'*14+text_bottom ,
                                           text_color='white',
                                           font=('Lucida Sans', 22)
                                           )
        self.label_main_img.pack()

        self.title = ctk.CTkLabel(self.left_frame, fg_color='#2b7380', 
                                 text=title, font=("Verdana", 
                                 35, 'bold'), text_color='#4ADEDE')
        self.title.place(x=60,y=50)
    
    def start_register(self):
        self.destroy()

        regist = Register()
        regist.mainloop()
    
    def run(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        emails = [x.split(',')[1] for x in alls]
        names = [x.split(',')[0] for x in alls]

        if email == '' or password == '':
            messagebox.showerror('Error', 'All fields are required', parent=self)
        elif '@' in email and email not in emails:
            messagebox.showerror('Error', "Email doesn't exists", parent=self)
        elif '@' not in email and email not in names:
            messagebox.showerror('Error', "Username doesn't exists", parent=self)
        else:
            for each in alls:
                username2, email2, password2, time = each.split(',')
                if email == email2 and password == password2 or email == username2 and password == password2:
                    messagebox.showinfo('Info', "Login successfull", parent=self)
                    self.start = True
                    self.result = [username2, email2, password2, time]
                    self.destroy()
                    break
            else:
                messagebox.showerror('Error', "Wrong password!", parent=self)

    def hide(self):
        self.hide_button.configure(image=self.closeeye_img)
        self.password_entry.configure(show='*')
        self.hide_button.configure(command=self.show)

    def show(self):
        self.hide_button.configure(image=self.openeye_img)
        self.password_entry.configure(show='')
        self.hide_button.configure(command=self.hide)

    def forgot_window(self):
        try:
            if self.new_window == None or not self.new_window.winfo_exists():
               self.new_window = ResetPassword() # create window if its None or destroyed
               self.new_window.mainloop()
            else:
                self.new_window.focus()
        except:
            self.new_window = ResetPassword()
            self.new_window.mainloop()
