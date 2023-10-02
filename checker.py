import Functions as fn
import customtkinter as ctk
from tkinter import messagebox as mb
import tkinter as tk
from tkinter import *


def check_page():
    def check():
        passd = []
        password = str(len_entry.get())
        x, pass_list = fn.checker(password)
        for i in pass_list:
            i = i.replace('{', '')
            i = i.replace('}', '')
            passd.append(i)
        # mb.showinfo("Password", message=passd)
        x = mb.askquestion(message=passd)
        print(x)

    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("light")
    check_win = ctk.CTk()
    check_win.title("Password Checker v2.0")
    check_win.geometry("880x720")

    back_but = PhotoImage(file="back.png")
    next_but = PhotoImage(file="next.png")

    label = ctk.CTkLabel(check_win,
                         text="Check Your Password",
                         font=('Century Gothic', 50, 'bold'))
    label.pack()

    back_button = Button(check_win,
                         image=back_but,
                         width=60,
                         height=60,
                         borderwidth=0,
                         bg='#ebebeb')
    back_button.place(x=30, y=20)

    next_button = Button(check_win,
                         image=next_but,
                         width=60,
                         height=60,
                         borderwidth=0,
                         bg='#ebebeb')
    next_button.place(x=800, y=20)

    len_lab = ctk.CTkLabel(check_win,
                           text="\t      Enter your password and Check",
                           font=('Century Gothic', 14))
    len_lab.place(x=235, y=220)

    gen_but = ctk.CTkButton(
        check_win,
        text="Check",
        font=('Impact', 40),
        width=150,
        height=60,
        hover_color="red",
        command=check)
    gen_but.place(x=350, y=310)

    len_entry = ctk.CTkEntry(check_win,
                             placeholder_text="~ <16 ~",
                             width=230)
    len_entry.place(x=320, y=260)

    '''sec_pass = Label(text='',
                     width=40,
                     font=("impact", 10),
                     bg="#ebebeb")
    sec_pass.place(x=300, y=370)'''

    check_win.mainloop()

check_page()