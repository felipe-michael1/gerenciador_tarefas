from tkinter import messagebox
from bson.objectid import ObjectId

def excluir_tarefas(colecao, id_tarefa):
    if not id_tarefa:
        messagebox.showwarning("Aviso", "Nenhuma tarefa selecionada para excluir.")
        return

    confirmar = messagebox.askyesno("Confirmar Exclusão", "Deseja realmente excluir esta tarefa?")

    if confirmar:
        try:
            colecao.delete_one({"_id": ObjectId(id_tarefa)})
            messagebox.showinfo("Sucesso", "Tarefa excluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir tarefa:\n{e}")
