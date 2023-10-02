import Functions as fn
import customtkinter as ctk
from tkinter import messagebox as mb
import pyperclip as pp
import tkinter as tk
from tkinter import *
global gen_pass


def check_page():
    def check():
        password = str(len_entry.get())
        x, pass_list = fn.checker(password)
        print(pass_list)
        sec_pass.configure(text=pass_list)

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

    sec_pass = Label(text='',
                     width=40,
                     font=("impact", 10),
                     bg="#ebebeb")
    sec_pass.place(x=300, y=370)

    check_win.mainloop()


def gen_page():
    def generate():
        size = int(len_entry.get())
        try:
            if size >= 16:
                global gen_pass
                gen_pass = fn.gen(size)
                print(gen_pass)
                lab_show.config(text="***********************************************************")
                # lab_show.config(width=size + 4)
                copy_state.configure(text='')

            else:
                mb.showwarning(title="Warning !",
                               message="Length is under 16")
        except ValueError:
            mb.showwarning(title="Warning !",
                           message="Invalid input")

    def copy():
        pp.copy(gen_pass)
        copy_state.configure(text="Password Successfully Copied into the clipboard ✅")

    def prev():
        gen_win.destroy()
        check_page()

    def show(gen_pass):
        if lab_show.cget('text') == gen_pass:
            lab_show.config(text="***********************************************************")
            eye_but.configure(image=eye_open)
        else:
            lab_show.config(text=gen_pass)
            eye_but.configure(image=eye_close)

    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("light")
    gen_win = ctk.CTk()
    gen_win.title("Password Checker v2.0")
    gen_win.geometry("880x720")

    eye_close = PhotoImage(file="invisible.png")
    eye_open = PhotoImage(file="view.png")
    copy_but = PhotoImage(file="clipboard.png")
    back_but = PhotoImage(file="back.png")
    next_but = PhotoImage(file="next.png")
    # but_state = eye_close
    label = ctk.CTkLabel(gen_win,
                         text="Generate Password",
                         font=('Century Gothic', 50, 'bold'))
    label.pack()

    back_button = Button(gen_win,
                         image=back_but,
                         width=60,
                         height=60,
                         borderwidth=0,
                         bg='#ebebeb',
                         command=prev)
    back_button.place(x=30, y=20)

    next_button = Button(gen_win,
                         image=next_but,
                         width=60,
                         height=60,
                         borderwidth=0,
                         bg='#ebebeb')
    next_button.place(x=800, y=20)

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

    lab_show = Label(master=gen_win,
                     text='',
                     font=('Impact', 21, 'italic'),
                     width=45,
                     bg="#ebebeb")

    lab_show.place(x=140, y=410)
    # lab_show.pack(padx=170,pady=390)

    eye_but = Button(gen_win,
                     image=eye_open,
                     width=60,
                     height=60,
                     borderwidth=0,
                     bg='#ebebeb',
                     command=lambda: show(gen_pass))
    eye_but.place(x=540, y=310)

    copy_button = Button(master=gen_win,
                         image=copy_but,
                         width=50,
                         height=50,
                         borderwidth=0,
                         bg="#ebebeb",
                         command=copy)
    copy_button.place(x=290, y=310)
    copy_state = ctk.CTkLabel(gen_win,
                              text='',
                              font=('Century Gothic', 30),
                              width=230,
                              height=30, )

    copy_state.place(x=58, y=550)
    gen_win.mainloop()


gen_page()
