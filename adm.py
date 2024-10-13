import os
def login_adm():
    while(True):
        print("Escolha qual ação deseja realizar")
        print("1 - Cadastro novo funcionario | 2 - Cadastro novo cliente | 3 - Cadastro novo remedio | 4 - Sair")
        opc_adm = int(input("Digite sua escolha: "))
        if opc_adm == 1:
            add_funcionario()
        elif opc_adm == 2:
            add_cliente()
        elif opc_adm == 3:
            add_remedio()
        elif opc_adm == 4:
            print("opção 4 adm")
            return
        else:
            print("Algum erro ocorreu na digitação da opção")
            print("Tente novamente")

def add_funcionario():
    print("Digite as informações pedidas a seguir")

def add_cliente():
    clientes = []
    print("Digite as informações pedidas a seguir")
    rg_cliente = input("Digite o RG: ")
    cpf_cliente = input("Digite o CPF: ")
    nome_cliente = input("Digite o nome: ")
    endereco_cliente = input("Digite o endereço: ")
    telefone_cliente = input("Digite o telefone para contato: ")

def add_remedio():
    remedios = []
    print("Digite as informações pedidas a seguir")
    nome_remedio = input("Digite o nome: ")
    marca_remedio = input("Digte a marca: ")
    tarja_remedio = input("Digite a cor da tarja: ")