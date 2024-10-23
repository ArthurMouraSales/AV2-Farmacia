import os
#Lista de cadastros adm com acesso
cadastros_admin = [
        {
            "email_adm": "arthur.sales@gmail.com",
            "senha_adm": "admin01"
        },
        {
            "email_adm": "admin",
            "senha_adm": "admin"
        }
    ]
#Lista de cadastros funcionarios com acesso
cadastros_funcionario = [        
        {
            "email_func": "funcionario.01@gmail.com",
            "senha_func": "func01"   
        },
    ]
#Função para o adm entrar no sistema
def login_adm():
    email_adm = input("Digite seu email: ")
    senha_adm = input("Digite sua senha: ")

    for login_adm in cadastros_admin:
        if login_adm['email_adm'] == email_adm and login_adm['senha_adm'] == senha_adm:
            print("Acesso liberado!")
            os.system('cls')
            return True
        else:
            print("Acesso negado!")
            return False
#Função para o funcionario entrar no sistema
def login_funcionario():
    email_func = input("Digite seu email: ")
    senha_func = input("Digite sua senha: ")

    for login_funcionario in cadastros_funcionario:
        if login_funcionario['email_func'] == email_func and login_funcionario['senha_func'] == senha_func:
            print("Acesso liberado!")
            return True
        else:
            print("Acesso negado!")
            return False
    