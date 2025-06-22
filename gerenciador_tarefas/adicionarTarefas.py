from tkinter import messagebox

def adicionar_tarefas(colecao, titulo, descricao, status):
    if not titulo or not descricao or not status:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos.")
        return

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": status
    }

    try:
        colecao.insert_one(tarefa)
        messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar a tarefa:\n{e}")
