import os
from banco import selecao_cliente, selecao_geral_vendas, selecao_venda_funcionario
from funcionario import venda

def menu_adm():
    print("Escolha qual ação deseja realizar")
    print("""--------------------------------------
    1 - Cadastro novo funcionario
    2 - Cadastro novo cliente
    3 - Cadastro novo remedio
    4 - Listar funcionarios
    5 - Listar clientes
    6 - Listar remedios
    7 - Sair
    --------------------------------------""")

def menu_principal():
    print("Seja bem vindo ao sistema interno de nossa empresa!")
    print(""" --------------------------------------
    1 - Login ADM
    2 - Login Funcionario
    3 - Finalizar
    --------------------------------------""")

def menu_funcionario():
    print("Escolha qual ação deseja realizar")
    print("""--------------------------------------
    1 - Realizar venda
    2 - Consultar clientes
    3 - Selecionar todas as vendas
    4 - Sair
    --------------------------------------""")
    opc_funcionario = int(input("Digite sua escolha: "))
    if opc_funcionario == 1:
        os.system('cls')
        venda()
    elif opc_funcionario == 2:
        os.system('cls')
        selecao_cliente()
    elif opc_funcionario == 3:
        os.system('cls')
        selecao_geral_vendas()
    elif opc_funcionario == 4:
        os.system('cls')
        id_funcionario = input("Digite do id do funcionario que voce deseja verificar: ")
        selecao_venda_funcionario(id_funcionario)
    elif opc_funcionario == 5:
        os.system('cls')
        return
    else:
        os.system('cls')
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")