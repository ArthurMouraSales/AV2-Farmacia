#Lista de cadastros adm com acesso
cadastros_admin = [
        {
            "email": "arthur.sales@gmail.com",
            "senha": "admin01"
        },
        {
            "email": "leonardo.salamoni@gmail.com",
            "senha": "admin02"   
        },
    ]
#Lista de cadastros funcionarios com acesso
cadastros_funcionario = [        
        {
            "email": "funcionario.01@gmail.com",
            "senha": "func01"   
        },
        {
            "email": "funcionario.02@gmail.com",
            "senha": "func02"   
        },
    ]
#Função para o adm entrar no sistema
def login_adm():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for login in cadastros_admin:
        if login['email'] == email and login['senha'] == senha:
            print("Acesso liberado!")
            return True
        else:
            print("Acesso negado!")
            return False
#Função para o funcionario entrar no sistema
def login_funcionario():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for login in cadastros_funcionario:
        if login['email'] == email and login['senha'] == senha:
            print("Acesso liberado!")
            return True
        else:
            print("Acesso negado!")
            return False
    