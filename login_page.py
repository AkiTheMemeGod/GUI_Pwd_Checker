import tkinter
import customtkinter as ctk
from PIL import ImageTk, Image
import os
from tkinter import messagebox as mb

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1080x720")
app.title('Login-Password_Checker-v2.0')


def cred_check():
    if entry1.get() == open("pg_chk_fls/acc_us.txt").read() and entry2.get() == open("pg_chk_fls/acc_pd.txt").read():
        mb.showinfo("Successful login", message="SUCCESSFUL LOGIN")
        login()
    else:
        mb.showerror("Try Again", message="INCORRECT LOGIN CREDENTIALS")


def login():
    app.destroy()
    with open("Gui_main.py") as file:
        exec(file.read())


img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))

l1 = ctk.CTkLabel(master=app, image=img1)
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

# textvariable=password)
entry2.place(x=50, y=165)


login_button = ctk.CTkButton(
    master=frame,
    width=220,
    text="Login",
    command=cred_check,
    corner_radius=6)
login_button.place(x=50, y=240)
l3 = ctk.CTkLabel(
    master=app,
    text="Created by: Akash",
    font=('Century Gothic', 10))
l3.place(x=980, y=690)
app.mainloop()