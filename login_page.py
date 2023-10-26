import tkinter
import os
import customtkinter as ctk

from PIL import ImageTk, Image
import PySimpleGUI as pg
from tkinter import messagebox as mb
import Functions as fn
import encrypter as en

en.encrypt_folder('pg_chk_fls')


def cred_check():
    if (en.encrypt(entry1.get()) == open("pg_chk_fls/acc_us.txt").read() and
            en.encrypt(entry2.get()) == open("pg_chk_fls/acc_pd.txt").read()):
        if en.encrypt(entry3.get()) == open("pg_chk_fls/acc_email.txt").read():
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


if os.path.exists('pg_chk_fls/acc_us.txt'):
    if open("pg_chk_fls/acc_us.txt").read() == '':
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
app.title('Password_Checker-v2.0')
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

l2 = ctk.CTkLabel(
    master=app,
    text="Password Checker-v2.0",
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
login_button.place(x=50, y=270)
l3 = ctk.CTkLabel(
    master=app,
    text="Created by: Akash",
    font=('Century Gothic', 10))
l3.place(x=980, y=690)
app.mainloop()
