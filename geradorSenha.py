import random
import customtkinter as ctk
from tkinter import messagebox

# Configuração de aparência
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("500x550")
app.title("Gerador de Senhas Seguras")

# Configuração de estilo
TITLE_FONT = ("Roboto", 24, "bold")
LABEL_FONT = ("Open Sans", 14)
BUTTON_FONT = ("Open Sans", 14, "bold")
ENTRY_FONT = ("Open Sans", 13)
RESULT_FONT = ("Consolas", 18)

# Frame superior 
upper_frame = ctk.CTkFrame(
    app, 
    corner_radius=20,
    border_width=2,
    border_color="#4e4376",
    fg_color=("gray90", "gray13")
)
upper_frame.pack(pady=15, padx=15, fill="x")

label_title = ctk.CTkLabel(
    upper_frame, 
    text="🔐 Gerador de Senhas Seguras",
    font=TITLE_FONT,
    text_color="#4e4376"
)
label_title.pack(pady=15)

# Frame inferior
lower_frame = ctk.CTkFrame(
    app, 
    corner_radius=20,
    border_width=2,
    border_color="#4e4376",
    fg_color=("gray90", "gray13")
)
lower_frame.pack(pady=5, padx=15, fill="both", expand=True)



app.mainloop()