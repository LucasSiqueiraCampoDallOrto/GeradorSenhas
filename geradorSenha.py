import random
import customtkinter as ctk
from tkinter import messagebox

def change_label_result(password):
    label_result.configure(text=''.join(password))

def generate_password():
    try:
        max_length = int(entry_size.get())

        if max_length < 4 or max_length > 30:
            messagebox.showwarning("Erro", "A senha deve ter entre 4 e 30 caracteres")
            return
        
        numbers = list(range(0,10)) 
        letters = list("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz")
        symbols = ["!", "@", "#", "$", "%", "&", "?"]
        password = []

        num_letters = (max_length - 1) // 2 #Reserva 1 espaço para o símbolo
        num_numbers = max_length - 1 - num_letters #Reserva 1 espaço para o símbolo

        for i in range(num_numbers):
            password.append(str(random.choice(numbers)))
        
        for i in range(num_letters):
            password.append(random.choice(letters))

        password.append(random.choice(symbols))
        random.shuffle(password)
        change_label_result(password)

    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido")

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

# Widgets
label_size = ctk.CTkLabel(
    lower_frame, 
    text="🔢 Tamanho da senha [4-30] :",
    font=LABEL_FONT,
    text_color="#4e4376"
)
label_size.pack(pady=(25, 5))

entry_size = ctk.CTkEntry(
    lower_frame, 
    placeholder_text="Ex.: 12", 
    width=220, 
    height=40,
    font=ENTRY_FONT,
    corner_radius=10,
    border_color="#4e4376",
    fg_color=("gray95", "gray10")
)
entry_size.pack(pady=5)

button = ctk.CTkButton(
    lower_frame, 
    text="⚡ Gerar Senha", 
    width=180, 
    height=40,
    font=BUTTON_FONT, 
    fg_color="#4e4376", 
    hover_color="#2b5876",
    corner_radius=10,
    border_width=2,
    border_color="#2b5876",
    command=generate_password
)
button.pack(pady=20)

label_password = ctk.CTkLabel(
    lower_frame, 
    text="🔑 Senha Gerada:", 
    font=LABEL_FONT,
    text_color="#4e4376"
)
label_password.pack(pady=(10, 5))

label_result = ctk.CTkLabel(
    lower_frame, 
    text="", 
    font=RESULT_FONT,
    text_color="#2b5876",
    bg_color=("gray95", "gray10"),
    corner_radius=8,
    width=300,
    height=40,
    anchor="center"
)
label_result.pack(pady=(0, 20))

# Rodapé
footer = ctk.CTkLabel(
    app, 
    text="© 2025 Gerador de Senhas Seguras | Desenvolvido com Python",
    font=("Open Sans", 10),
    text_color="gray50"
)
footer.pack(side="bottom", pady=5)

app.mainloop()