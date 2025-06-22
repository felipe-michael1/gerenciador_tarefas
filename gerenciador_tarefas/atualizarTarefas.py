from tkinter import messagebox
from bson.objectid import ObjectId

def atualizar_tarefas(colecao, id_tarefa, titulo, descricao, status):
    if not id_tarefa:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada para atualizar.")
        return

    if not titulo.strip():
        messagebox.showwarning("Aviso", "O título da tarefa não pode estar vazio.")
        return

    dados_atualizacao = {
        "$set": {
            "titulo": titulo.strip(),
            "descricao": descricao.strip(),
            "status": status
        }
    }

    try:
        colecao.update_one({"_id": ObjectId(id_tarefa)}, dados_atualizacao)
        messagebox.showinfo("Sucesso", "Tarefa atualizada com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar a tarefa:\n{e}")
