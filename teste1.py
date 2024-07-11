# TODO: Resposta do desafio 02
lista_tarefas = []
contadorTarefas = 0

while True:
    print("1 - Adicionar tarefa: ")
    print("2 - Listar tarefa: ")
    print("3 - Remover tarefa: ")
    print("4 - Atualizar tarefa: ")
    print("5 - Finalizar programa: ")
    opcao = input("Opção: ")

    # Adicionar Tarefa
    if opcao == '1':
        nome_tarefa = input("Digite a tarefa que deseja adicionar: ")
        if nome_tarefa == "":
            print("Não foi possivél adicionar a tarefa!")
        else:
            lista_tarefas.append(nome_tarefa)
            contadorTarefas += 1
            print("Tarefa adicionada com sucesso!")
    # Listar Tarefa      
    elif opcao == '2':
        print(20*'=', 'Tarefas a fazer', 20*'=')
        if len(lista_tarefas) == 0:
            print("Lista vazia!")
        else:
            for idx, tarefa in enumerate(lista_tarefas): # gera pares de valores (índice, valor) para cada item na lista lista_tarefas
                print(f'ID: {idx} - Tarefa: {tarefa}')
    # Remover Tarefa
    elif opcao == '3':
        print(20*'=', 'Remover tarefa', 20*'=')
        if len(lista_tarefas) == 0:
            print("Não tem tarefas para serem removidas!")
        else:
            remover_tarefa = input("Qual o id da tarefa que deseja remover? ")
            if remover_tarefa.isdigit():
                remover_tarefa = int(remover_tarefa)
                if 0 <= remover_tarefa < len(lista_tarefas):
                    tarefa_removida = lista_tarefas.pop(remover_tarefa)
                    print(f'Tarefa: {tarefa_removida} removida com sucesso!')
                else:
                    print("ID inválido!")
            else:
                print("ID inválido! Digite apenas numeros!")
    # Atualizar Tarefa
    elif opcao == '4':
        print(20*'=', 'Atualizar tarefa', 20*'=')
        if len(lista_tarefas) == 0:
            print("Lista vazia, não há nada para ser atualizada")
        else:
            tarefaId = input("Digite o id da tarefa que deseja atualizar: ")

        if tarefaId.isdigit(): # Verifica se o id é um numero
            tarefaId = int(tarefaId)
            if 0 <= tarefaId < len(lista_tarefas): # Verifica se o id está dentro dos limites da lista
                nova_tarefa = input("Digite a nova tarefa: ")
                lista_tarefas[tarefaId] = nova_tarefa
                print(f'Tarefa ID {tarefaId} atualizada com sucesso!')
            else:
                print("ID inválido!")
        else:
            print("ID inválido! digite um número.")

    elif opcao == '5':
        print("Programa finalizado")
        break
    else:
        print("Opção invalida!")
        continue
