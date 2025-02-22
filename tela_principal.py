import tkinter as tk


def abrir_tela_principal():
    global tela_principal
    tela_principal = tk.Tk()
    tela_principal.title("gerenciador de senhas")
    tela_principal.geometry("600x400")
    tk.Button(tela_principal, text="+", command=add_senha).pack()
    tela_principal.configure(bg="lightgray")
    tela_principal.mainloop()
    
def add_senha():
    nova_senha_entry = tk.Entry(tela_principal) 
    nova_senha_entry.pack(pady=5, anchor="w", padx=3)

   
    
    