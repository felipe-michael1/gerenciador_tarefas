def aplicar_filtro(arvore_tarefas, colecao, filtro_status=None):
    from bson.objectid import ObjectId

    # empty the filters in the three
    for item in arvore_tarefas.get_children():
        arvore_tarefas.delete(item)

    # prepare the consultant
    consulta = {}
    if filtro_status in ["Pendente", "Concluída"]:
        consulta = {"status": filtro_status}

    # execute the search
    tarefas = colecao.find(consulta)

    # Populate Treeview with filters
    for tarefa in tarefas:
        arvore_tarefas.insert(
            "",
            "end",
            iid=str(tarefa["_id"]),
            values=(tarefa["titulo"], tarefa["descricao"], tarefa["status"])
        )
