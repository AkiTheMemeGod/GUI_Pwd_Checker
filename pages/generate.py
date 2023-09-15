import Functions as fn
import customtkinter as ctk
from tkinter import messagebox as mb
import pyperclip as pp
import tkinter as tk
from tkinter import *


def gen_page():
    def generate():
        try:
            if int(len_entry.get()) >= 16:
                size = len_entry.get()
                gen_pass = fn.gen(size)
                lab_show.configure(text=gen_pass)
                pp.copy(gen_pass)
                copy_state.configure(text="Password Successfully Copied into the clipboard ✅")

            else:
                mb.showwarning(title="Warning !",
                               message="Length is under 16")
        except ValueError:
            mb.showwarning(title="Warning !",
                           message="Invalid input")


    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("light")
    gen_win = ctk.CTk()
    gen_win.title("Password Checker v2.0")
    gen_win.geometry("880x720")

    label = ctk.CTkLabel(gen_win,
                         text="Generate Password",
                         font=('Century Gothic', 50, 'bold'))
    label.pack()

    len_lab = ctk.CTkLabel(gen_win,
                           text="Enter the length \n (more than 16 characters is considered a strong password !)",
                           font=('Century Gothic', 14))
    len_lab.place(x=235, y=190)

    len_entry = ctk.CTkEntry(gen_win,
                             placeholder_text="~ <16 ~",
                             width=230)
    len_entry.place(x=320, y=260)

    gen_but = ctk.CTkButton(
        gen_win,
        text="Generate",
        font=('Impact', 40),
        command=generate,
        width=150,
        height=60)
    gen_but.place(x=350, y=310)

    lab_show = ctk.CTkLabel(gen_win,
                            text='',
                            font=('Impact', 28, 'bold'),
                            width=230,
                            height=30)
    lab_show.place(x=200, y=450)

    eye_close = PhotoImage(file='assets/view.png')
    eye_but = ctk.CTkButton(gen_win,
                            image=eye_close,
                            )
    eye_but.pack(padx=20)

    copy_state = ctk.CTkLabel(gen_win,
                              text='',
                              font=('Century Gothic', 30),
                              width=230,
                              height=30)

    copy_state.place(x=58, y=550)

    gen_win.mainloop()


gen_page()
