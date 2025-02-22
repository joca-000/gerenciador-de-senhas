import tkinter as tk
import tela_principal

def validar_senha():
    senha = senha_entry.get() #pega oque foi digitado
    if senha == "1234":
        root.destroy() # fecha a tela de login
        tela_principal.abrir_tela_principal() # abre a tela principal
    else:
        print("senha incorreta!") # temporario para debug

# executar aplicação
def iniciar_login():
    global root, senha_entry
    root = tk.Tk()
    root.title("login")
    root.configure(bg="lightgray")
    root.geometry("300x200")

    tk.Label(root, text="senha mestre:", font="Arial").pack()
    senha_entry = tk.Entry(root, show="*")
    senha_entry.pack()

    tk.Button(root, text="Entrar", command=validar_senha).pack()
    root.bind("<Return>", lambda event: validar_senha())
    root.mainloop()
