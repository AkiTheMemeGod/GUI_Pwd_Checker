import tkinter as tk
import customtkinter as ctk
from pages import generate as gn
import Functions as fn
from tkinter import messagebox as mb
import pyperclip as pp


'''def gen_page():
    def generate():
        if int(len_entry.get()) >= 16:
            size = len_entry.get()
            gen_pass = fn.gen(size)
            lab_show.configure(text=gen_pass)
            pp.copy(gen_pass)
            copy_state.configure(text="Password Successfully Copied into the clipboard ✅")
        else:
            mb.showwarning(title="Warning !",
                           message="Length is under 16")

    # TODO:add any appropriate image
    # img = PhotoImage(file=)

    gen_frame = tk.Frame(right_frame)

    label = tk.Label(master=gen_frame,
                     text="Generate Password",
                     font=('Century Gothic', 50, 'bold'))
    label.pack(side=tk.TOP)

    len_lab = tk.Label(master=gen_frame,
                       text="Enter the length \n (more than 16 characters is considered a strong password !)",
                       font=('Century Gothic', 14))
    len_lab.place()
    len_lab.pack(padx=.5, pady=.5)
    len_entry = ctk.CTkEntry(gen_frame,
                             placeholder_text="~ <16 ~",
                             width=230)
    len_entry.place(x=320, y=260)
    len_entry.pack()
    gen_but = ctk.CTkButton(
        gen_frame,
        text="Generate",
        font=('Impact', 40),
        command=generate,
        width=150,
        height=60)
    gen_but.place(x=350, y=310)
    gen_but.pack()

    lab_show = ctk.CTkLabel(master=gen_frame,
                            text='',
                            font=('Impact', 28, 'bold'),
                            width=230,
                            height=30)
    lab_show.place(x=200, y=450)
    lab_show.pack()
    copy_state = tk.Label(master=gen_frame,
                          text='',
                          font=('Century Gothic', 25),
                          width=230,
                          height=30)

    copy_state.place(x=58, y=550)
    copy_state.pack()
    gen_frame.pack()

'''


def show_ind(lb, page):
    hide_ind()
    lb.configure(bg="green")
    page()


def hide_ind():
    man_ind.configure(bg="#c3c3c3")
    gen_ind.configure(bg="#c3c3c3")
    check_ind.configure(bg="#c3c3c3")


ctk.set_default_color_theme("green")
ctk.set_appearance_mode("light")
window = ctk.CTk()
window.title("Password Checker v2.0")
window.geometry("1080x720")


right_frame = tk.Frame(master=window)

right_frame.pack(side=ctk.RIGHT)
right_frame.pack_propagate(False)
right_frame.configure(width=880, height=720)
# right_frame.place()

left_frame = tk.Frame(master=window,
                      bg="#c3c3c3")

left_frame.pack(side=ctk.LEFT)
left_frame.pack_propagate(False)
left_frame.configure(width=200,
                     height=720)

generate_but = ctk.CTkButton(
    left_frame,
    text="Generate",
    command=lambda: show_ind(gen_ind, gn.gen_page))
generate_but.place(x=30, y=220)

check_but = ctk.CTkButton(
    left_frame,
    text="Check",
    command=lambda: show_ind(check_ind))
check_but.place(x=30, y=320)

manage_but = ctk.CTkButton(
    left_frame,
    text="Manage",
    command=lambda: show_ind(man_ind))
manage_but.place(x=30, y=420)

gen_ind = tk.Label(left_frame,
                   text='',
                   bg="#c3c3c3")
gen_ind.place(x=0, y=215, width=5, height=40)

check_ind = tk.Label(left_frame,
                     text='',
                     bg="#c3c3c3")
check_ind.place(x=0, y=315, width=5, height=40)

man_ind = tk.Label(left_frame,
                   text='',
                   bg="#c3c3c3")
man_ind.place(x=0, y=415, width=5, height=40)

# left_frame.place()


window.mainloop()
