import os
os.system('cls')
from cryptography.fernet import Fernet

#Funções e organização -- 
sair = "não"

#Encriptação -
'''
def criarkey():
    key = Fernet.generate_key()
    with open("chave.key", "wb") as sheet_key:
        sheet_key.write(key)'''

def abrirkey():
    file = open("chave.key", "rb")
    chave = file.read()
    return chave

#Ver - 
def ver():
    print()
    with open("loginsheet.txt", "r") as sheet:
    
        for list in sheet.readlines():
            data = list
            login, user, senha = data.split("|")
            print(login, "-" "\n" "User:", user)
            print("Senha:", fer.decrypt(senha.encode()).decode(), "\n")
    
    continuar = input("Deseja continuar usando o porgrama? ")
    if continuar != "sim":
        exit()

#Add - 
def add():
    print()
    onde = input("Salvar nome do login como: ")
    name = input("Nome da conta: ")
    pwd = input("Senha da conta: ")
    print()
    
    with open("loginsheet.txt", "a") as sheet:
        sheet.write(onde + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
    
    mais = input("Deseja adicionar mais? ")
    if mais != "sim":
        print()
        check = input("Deseja ver os logins adicionados? ")
        
        if check == "sim":
            ver()
        else: 
            print("\033[31m""Saindo do programa...""\033[0m")
            exit()
    
    else: 
        add()

#Código -- 
print("\033[35m""Gerenciador pessoal de senhas")
print("---""\033[0m")

chave = abrirkey()
fer = Fernet(chave)

while sair != "sim":
    print()
    print("\033[34m""Bem vindo!""\033[0m")
    print()
    print("O que você gostaria de fazer:")
    mode = input("Ver logins existentes (ver), adicionar uma senha nova (add)? ")
    if mode == "add":
        add()
    elif mode == "ver":
        ver()
    else:
        print()
        print("\033[31m""Desculpe não entendi o que você deseja")
        sair = input("Deseja sair? ""\033[0m")
        continue 

