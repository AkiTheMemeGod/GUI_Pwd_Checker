import customtkinter as ctk
import Functions as fn
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.title("Password Checker v2.0")
window.geometry("1080x720")

label = ctk.CTkLabel(
    window,
    text="Password Checker v2.0",
    text_color="White")
label.pack()

generate_butt = ctk.CTkButton(
    window,
    text="Generate",
    command=fn.gen(16)
)
window.mainloop()