import customtkinter as ctk
import tkinter as tk
import Functions as fn


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


tit = ctk.CTkLabel(
    master=right_frame,
    text="Password Checker-v2.0",
    font=('Century Gothic', 50, 'bold'))
tit.place(x=180, y=40)
# tit.pack()


left_frame = tk.Frame(master=window,
                      bg="#c3c3c3")

left_frame.pack(side=ctk.LEFT)
left_frame.pack_propagate(False)
left_frame.configure(width=200,
                     height=720)

generate_but = ctk.CTkButton(
    left_frame,
    text="Generate",
    command=lambda: fn.gen(16))
generate_but.place(x=30, y=220)

check_but = ctk.CTkButton(
    left_frame,
    text="Check")
check_but.place(x=30, y=320)

manage_but = ctk.CTkButton(
    left_frame,
    text="Manage")
manage_but.place(x=30, y=420)

gen_ind = tk.Label(left_frame,
                   text='',
                   bg="green")
gen_ind.place(x=0, y=215, width=5, height=40)

check_ind = tk.Label(left_frame,
                     text='',
                     bg="green")
check_ind.place(x=0, y=315, width=5, height=40)

man_ind = tk.Label(left_frame,
                   text='',
                   bg="green")
man_ind.place(x=0, y=415, width=5, height=40)



# left_frame.place()


window.mainloop()
