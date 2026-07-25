print("---lista de tarefas---")

array_principal = []

while True:
    opcao_escolhida = str(input("Escreva 'add' para adicionar, 'lis' para listar e 'mar' para marcar como feita: "))

    if opcao_escolhida == "add":
        item_para_adicionar = str(input("O que quer adicionar: "))
        array_principal.append(item_para_adicionar)
        print("Item adicionar com sucesso!")

    if opcao_escolhida == "lis":
        print(array_principal)
    
    if opcao_escolhida == "mar":
        print(array_principal)
        item_marcado = int(input("Qual item deseja marcar como concluida? coloque o index"))
        array_principal.pop(item_marcado)


