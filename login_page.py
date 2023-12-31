import tkinter
import os
import customtkinter as ctk

from PIL import ImageTk, Image
import PySimpleGUI as pg
from tkinter import messagebox as mb
import Functions as fn
import encrypter as en
# TODO add a separate user database for each users
# TODO add a pdf and excel downloading system for the current user's pwd database
en.encrypt_folder('pg_chk_fls')


def cred_check():
    """print(en.encrypt(entry1.get()+'\n'))
    print(fn.get_account_string("pg_chk_fls/acc_us.txt"))"""
    if (en.encrypt(entry1.get()+'\n') in fn.get_account_string("pg_chk_fls/acc_us.txt") and
            en.encrypt(entry2.get()+'\n') in fn.get_account_string("pg_chk_fls/acc_pd.txt")):
        if en.encrypt(entry3.get()+'\n') in fn.get_account_string("pg_chk_fls/acc_email.txt"):
            gmail = entry3.get()
            x = int(fn.verify_otp(gmail))
            while True:
                otp = int(pg.popup_get_text(no_titlebar=True,
                                            button_color="#2cc985",
                                            background_color='#ebebeb',
                                            text_color='black',
                                            message="Please Enter your 6-Digit OTP",
                                            size=(50, 50)))
                if otp == x:
                    mb.showinfo("Successful login", message="SUCCESSFUL LOGIN")
                    fn.write_session(entry1.get())
                    login()
                    break
                else:
                    mb.showerror("Try Again", message="INCORRECT LOGIN CREDENTIALS")
                    continue
        else:
            mb.showerror("Try Again", message="enter a vaild email")
    else:
        mb.showerror("Try Again", message="INCORRECT LOGIN CREDENTIALS")


def login():
    app.destroy()
    os.system('python generate.py')


def signup():
    app.destroy()
    os.system('python C:/PROJECTS/GUI_Pwd_Checker/SignUp.py')


if os.path.exists('pg_chk_fls/acc_us.txt'):
    if open("pg_chk_fls/acc_us.txt").read() == '':
        mb.showerror(title='ACCOUNT DOESNT EXIST',
                     message="There is no account detected in this machine! Try Signing Up :)")
        os.system('python SignUp.py')
        exit()
    else:
        pass

else:
    os.system('python SignUp.py')
    exit()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.geometry("1080x720+400+100")
app.title('Password_Generator-v2.0')
app.after(201, lambda: app.iconbitmap('assets/image.ico'))

img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
# img1 = CTkImage(light_image="assets/pattern.png")
l1 = ctk.CTkLabel(master=app,
                  image=img1)
l1.pack()

frame = ctk.CTkFrame(
    master=l1,
    width=320,
    height=360,
    corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# comments line
l2 = ctk.CTkLabel(
    master=app,
    text="Password_Generator-v2.0",
    font=('Century Gothic', 50))
l2.place(x=290, y=35)

l2 = ctk.CTkLabel(
    master=frame,
    text="Log into your Account",
    font=('Century Gothic', 20))
l2.place(x=50, y=45)

# username = ctk.StringVar()

entry1 = ctk.CTkEntry(
    master=frame,
    width=220,
    placeholder_text='Username')
# textvariable=username)
entry1.place(x=50, y=110)
# password = ctk.StringVar()

entry2 = ctk.CTkEntry(
    master=frame,
    width=220,
    placeholder_text='Password',
    show="*")

entry2.place(x=50, y=165)

entry3 = ctk.CTkEntry(
    master=frame,
    width=220,
    placeholder_text='e-mail')

entry3.place(x=50, y=220)

login_button = ctk.CTkButton(
    master=frame,
    width=220,
    text="Login",
    command=cred_check,
    corner_radius=6,
    hover_color='red')
login_button.place(x=50, y=260)

sign_up_button = ctk.CTkButton(
    master=frame,
    width=220,
    text="New here? Signup",
    command=signup,
    corner_radius=6,
    hover_color='lime')
sign_up_button.place(x=50, y=300)

l3 = ctk.CTkLabel(
    master=app,
    text="Created by: Akash",
    font=('Century Gothic', 10))
l3.place(x=980, y=690)
app.mainloop()
