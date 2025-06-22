import tkinter as tk

def limpar_tarefas(entrada_titulo, entrada_descricao, var_status):
    entrada_titulo.delete(0, tk.END)
    entrada_descricao.delete("1.0", tk.END)
    var_status.set("Pendente")