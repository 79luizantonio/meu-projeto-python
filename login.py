import tkinter as tk

def login():
    username = entry_user.get()
    password = entry_pass.get()
    # Aqui você colocaria a lógica de verificação do usuário e senha
    # Por exemplo, comparando com um banco de dados
    if username == "admin" and password == "password":
        label_result.config(text="Login bem-sucedido!")
    else:
        label_result.config(text="Usuário ou senha inválidos.")

# Cria a janela principal
window = tk.Tk()
window.title("Tela de Login")

# Cria os labels e campos de entrada
label_user = tk.Label(window, text="Usuário:")
label_user.pack()
entry_user = tk.Entry(window)
entry_user.pack()

label_pass = tk.Label(window, text="Senha:")
label_pass.pack()
entry_pass = tk.Entry(window, show="*")
entry_pass.pack()

# Botão de login
button_login = tk.Button(window, text="Login", command=login)
button_login.pack()

# Label para mostrar o resultado do login
label_result = tk.Label(window, text="")
label_result.pack()

# Inicia a aplicação
window.mainloop()