from tkinter import PhotoImage
from tkinter import Button, Label
from tkinter import messagebox as mb
import PySimpleGUI as pg
import customtkinter as ctk
import pyperclip as pp
import Functions as fn
from checker import check_page
from manage import manager
global gen_pass


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
                save_but.configure(image=save_butt)

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

    def nextp():
        gen_win.destroy()
        manager()

    def show(gen_pass):
        if lab_show.cget('text') == gen_pass:
            lab_show.config(text="***********************************************************")
            eye_but.configure(image=eye_open)
        else:
            lab_show.config(text=gen_pass)
            eye_but.configure(image=eye_close)

    def save_pwd(pd):

        choice = mb.askquestion(title='SAVE PASSWORD',
                                message='Do you want to save this password ? ')
        if choice == 'yes':
            us = pg.popup_get_text(icon='image.ico',
                                   button_color="#2cc985",
                                   background_color='#c6c6c6',
                                   text_color='black',
                                   message="Please Enter the username"
                                   )
            fn.save(pd, us)
            save_but.configure(image=saved_butt)

    ctk.set_default_color_theme("green")
    ctk.set_appearance_mode("light")
    gen_win = ctk.CTk()
    gen_win.title("Password Checker v2.0")
    gen_win.geometry("880x720+500+100")
    gen_win.after(201, lambda: gen_win.iconbitmap('assets/image.ico'))

    eye_close = PhotoImage(file="assets/invisible.png")
    eye_open = PhotoImage(file="assets/view.png")
    copy_but = PhotoImage(file="assets/clipboard.png")
    save_butt = PhotoImage(file="assets/save.png")
    saved_butt = PhotoImage(file="assets/saved.png")
    # but_state = eye_close
    label = ctk.CTkLabel(gen_win,
                         text="Generate Password",
                         font=('Century Gothic', 50, 'bold'))
    label.pack(pady=25)

    back_button = ctk.CTkButton(
        gen_win,
        text="Checker",
        font=('Impact', 40),
        width=150,
        height=60,
        command=prev,
        hover_color='dark green')
    back_button.place(x=30, y=20)

    next_button = ctk.CTkButton(gen_win,
                                text="Manage",
                                font=('Impact', 40),
                                width=150,
                                height=60,
                                command=nextp,
                                hover_color='dark green')
    next_button.place(x=700, y=20)

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
    eye_but.place(x=515, y=310)

    save_but = Button(gen_win,
                      image=save_butt,
                      width=60,
                      height=60,
                      borderwidth=0,
                      bg='#ebebeb',
                      command=lambda: save_pwd(gen_pass))
    save_but.place(x=575, y=310)

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
