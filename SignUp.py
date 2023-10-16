import tkinter
import os
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import ImageTk, Image
import PySimpleGUI as pg
from tkinter import messagebox as mb
import Functions as fn


if open("pg_chk_fls/acc_us.txt").read() == '':
    os.remove("pg_chk_fls/acc_us.txt")
    os.remove("pg_chk_fls/acc_pd.txt")
    os.remove("pg_chk_fls/acc_email.txt")
else:
    mb.showwarning(title="ACCOUNT ALREADY EXISTS ! ",
                   message="Account Already Exists in this machine TRY LOGGING IN ")
    fn.notif(message="Account Already Exists in this machine TRY LOGGING IN ")
    os.system("python login_page.py")
    exit()

def cred_check():
    with open("pg_chk_fls/acc_us.txt", "w") as f:
        f.write(entry1.get())
    with open("pg_chk_fls/acc_pd.txt", "w") as f:
        f.write(entry2.get())
    with open("pg_chk_fls/acc_email.txt", "w") as f:
        f.write(entry3.get())

    fn.notif("Account Created Successfully ")
    login()


def login():
    app.destroy()
    os.system('python login_page.py')


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1080x720+400+100")
app.title('Password_Checker-v2.0')
app.after(201, lambda: app.iconbitmap('assets/image.ico'))

img1 = ImageTk.PhotoImage(Image.open("./assets/pattern.png"))
# img1 = CTkImage(light_image="assets/pattern.png")
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
    text="SignUp your Account",
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
    text="SignUp",
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

