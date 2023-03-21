import os, time
os.system("cls")
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
    print("\033[34m"'Você escolheu - ver:'"\033[0m")
    print()
    with open("loginsheet.txt", "r") as sheet:
    
        for list in sheet.readlines():
            data = list
            login, user, senha = data.split("|")
            print(login, "-" "\n" "User:", user)
            print("Senha:", fer.decrypt(senha.encode()).decode(), "\n")
            time.sleep(0.5)
    
    continuar = input("Deseja continuar usando o porgrama? ")
    os.system("cls")
    
    if continuar != "sim":
        print()
        print("\033[34m""Obrigado por me usar!""\033[0m")
        print("\033[31m""Encerrando operações...""\033[0m")
        time.sleep(1)
        exit()

#Add - 
def add():
    print()
    print("\033[35m"'Você escolheu - adicionar (add):'"\033[0m")
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
            time.sleep(1)
            os.system("cls")
            ver()
        else: 
            print("\033[31m""Saindo do programa...""\033[0m")
            exit()
    
    else: 
        time.sleep(1)
        os.system("cls")
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
        os.system("cls")
        continue 
print()
print("Saindo...")
exit()
