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


app.mainloop()