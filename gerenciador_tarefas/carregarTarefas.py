import tkinter as tk

def carregar_tarefas(arvore_tarefas, colecao, filtro_status=None):
    for item in arvore_tarefas.get_children():
        arvore_tarefas.delete(item)

    consulta = {}
    if filtro_status and filtro_status in ["Pendente", "Concluída"]:
        consulta = {"status": filtro_status}

    tarefas = colecao.find(consulta)

    for tarefa in tarefas:
        arvore_tarefas.insert(
            "", tk.END,
            values=(tarefa["titulo"], tarefa["descricao"], tarefa["status"]),
            iid=str(tarefa["_id"])
        )
