import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

# Funções --
# Checando a existência da lista -
def checkExistênciaBackup():
    if os.path.isfile('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            file.seek(0, os.SEEK_END)
            isempty = file.tell() == 0
            file.seek(0)
        if isempty == False:
            with open("tasks.txt", "r", encoding='utf=8') as backup:
                for list in backup.readlines():
                    data = list
                    item = data.strip('\n')
                    toDo.append(item.capitalize())
        else:
            os.remove('tasks.txt')

# Saindo do programa -
def sair():
    print(
        '\033[31mVocê escolheu sair :(\033[0m\nObrigado por usar o nosso programa!\nSaindo...')
    time.sleep(1.5)
    exit()

# Adcionando itens a lista -
def add():
    print('\033[32mVocê escolheu adcionar uma tarefa.\033[0m')
    addItem = input('O que você gostaria de adicionar? ').strip()
    print()
    if addItem.capitalize() in toDo:
        print('\033[32mVocê já adcionou isto a sua lista!\033[0m')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:  # Adição
        toDo.append(addItem.capitalize())
        print(f'Item - {addItem.capitalize()}, adcionado a sua lista!')
        print('---')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        with open('tasks.txt', 'a', encoding='utf=8') as backup:
            backup.write(addItem.capitalize() + '\n')


# Removendo itens do backup
def removendoDoBackup(toDo, removendo):
    remova = toDo.index(removendo) + 1
    with open("tasks.txt", "r") as backup:
        lines = backup.readlines()
        pointer = 1
        with open('tasks.txt', 'w') as backup:
            for line in lines:
                if pointer != remova:
                    backup.write(line)
                pointer += 1


# Deletando a lista -
def deletandoLista():
    confirmacao = input(
        'Tem certeza que deseja \033[31mapagar toda a lista\033[0m? ').lower()

    if confirmacao.strip() == 'sim':  # Deletando toda lista e backup
        print('Deletando toda sua lista...')
        time.sleep(1)
        toDo.clear()
        open('tasks.txt', 'w')
        print()
        ver()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

    else:
        print('\nUfa..\nEssa foi por pouco 😰')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')


# Removendo itens -
def remover():
    print('\033[31mVocê escolheu remover\033[0m')
    print()
    ver()
    removerItem = input(
        'O que você gostaria de remover (digite del para apagar toda lista)? ').strip()
    print()
    # Garantindo que o item que quer ser reovido existe na lista e no backup
    if removerItem.capitalize() in toDo:
        confirmacao = input(
            f'Você tem certeza que deseja remver o item \033[31m{removerItem}\033[0m? ').lower()
        if confirmacao.strip() == 'sim':
            removendoDoBackup(toDo, removerItem.capitalize())
            print(f'{removerItem} removido')
            time.sleep(1)
            toDo.remove(removerItem.capitalize())
            ver()
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
        else:  # Não removendo item da lista
            print('\033[32mNão removendo item.\033[0m')
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            remover()

    elif removerItem == 'del':
        deletandoLista()

    else:  # Caso o item que desejam remover não se encontre
        print('Item não presente na lista.')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


# Imprimindo a lista -
def ver():
    print('Aqui está sua lista:\n')
    for index in range(len(toDo)):
        print(f'{index+1}: {toDo[index]}')
    print("---\n")


# Editando o backup -
def editandoBackup(editando, novo):
    with open('tasks.txt', 'r') as backup:
        conteudo = backup.read()
    conteudo = conteudo.replace(editando, novo)
    with open('tasks.txt', 'w') as backup:
        backup.write(conteudo)

# Editando a lista -
def editar():
    ver()
    editarItem = input(
        'Informe o item que você gostaria de alterar: ') .strip()

    if editarItem.capitalize() in toDo:
        novo = input(
            f'Você gostaria de mudar \033[34m{editarItem}\033[0m para o que? ') .strip()
        for i in range(len(toDo)):
            if toDo[i] == editarItem.capitalize():
                toDo[i] = novo.capitalize()  # Substituindo o valor de um item por um novo
                print(f'\n{editarItem.capitalize()} alterado para {novo.capitalize()}.')
                editandoBackup(editarItem.capitalize(), novo.capitalize())
    else:
        print(f'\nItem: {editarItem.capitalize()} não encontrado\nTente denovo...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    time.sleep(3)
    os.system('cls')


# Código principal --
toDo = []

checkExistênciaBackup()

print('\033[35mGerenciador de tarefas!\n---\n\033[0m')
print('Gerenciador de tarefas simples para você sempre manter anotado o que você precisa fazer em seu dia!\n')


while True:
    print('O que você gostaria de fazer?')
    menu = input(
        'Adcionar (add), remover, editar, ver ou sair? ').lower()
    print()
    if menu.strip() == 'sair':
        sair()
    elif menu.strip() == 'add' or menu.strip() == 'adcionar':
        add()
    elif menu.strip() == 'remover':
        remover()
    elif menu.strip() == 'ver':
        print('\033[35mVocê escolheu ver!\033[0m\n')
        ver()
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif menu.strip() == 'editar':
        print('\033[34mVocê escolheu editar.\n\033[0m')
        editar()
    else:
        print('\033[31mOpção inválida!\033[0m\nTente novamente...')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
