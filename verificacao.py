cadastros = [
        {
            "email": "arthur.sales@gmail.com",
            "senha": "admin01"
        },
        {
            "email": "leonardo.salamoni@gmail.com",
            "senha": "admin02"   
        },
        {
            "email": "funcionario.01@gmail.com",
            "senha": "func01"   
        },
        {
            "email": "funcionario.02@gmail.com",
            "senha": "func02"   
        },
    ]

def login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for login in cadastros:
        if login['email'] == email and login['senha'] == senha:
            print("Acesso liberado!")
            return
        else:
            print("Acesso negado!")
            return 

login()
    