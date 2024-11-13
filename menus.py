import os
from banco import selecao_cliente, selecao_geral_vendas, selecao_venda_funcionario, selecao_info_funcionario, selecao_cliente, selecao_funcionario, selecao_remedio
from funcionario import venda
from adm import acesso_adm, add_cliente, add_funcionario, add_remedio
from funcionario import acesso_funcionario

def menu_adm():
    print("Escolha qual ação deseja realizar")
    print("""
    --------------------------------------
    1 - Cadastro novo funcionario
    2 - Cadastro novo cliente
    3 - Cadastro novo remedio
    4 - Listar funcionarios
    5 - Listar clientes
    6 - Listar remedios
    7 - Sair
    --------------------------------------""")

    opc_adm = int(input("Digite sua escolha: "))
    if opc_adm == 1:
        add_funcionario()
    elif opc_adm == 2:
        add_cliente()
    elif opc_adm == 3:
        add_remedio()
    elif opc_adm == 4:
        selecao_funcionario()
    elif opc_adm == 5:
        selecao_cliente()
    elif opc_adm == 6:
        selecao_remedio()
    elif opc_adm == 7:
        print("Sair")
        return
    else:
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")


def menu_principal():
    print("Seja bem vindo ao sistema interno de nossa empresa!")
    print(""" 
    --------------------------------------
    1 - Login ADM
    2 - Login Funcionario
    3 - Finalizar
    --------------------------------------""")

    opcao = int(input("Digite uma das opções sinalizadas acima: "))
    if opcao == 1:
        print("Você esta na aba de administrador")
        acesso_adm()
    elif opcao == 2:
        print("Você esta na aba de funcionario")
        acesso_funcionario()
    elif opcao == 3:
        return
    else:
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")

def menu_funcionario():
    print("Escolha qual ação deseja realizar")
    print("""
    --------------------------------------
    1 - Realizar venda
    2 - Consultar clientes
    3 - Selecionar todas as vendas
    4 - Vendas diaria do funcionario
    5 - 
    10 - Sair
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
        selecao_info_funcionario()
        id_funcionario = input("Digite do id do funcionario que voce deseja verificar: ")
        selecao_venda_funcionario(id_funcionario)
    elif opc_funcionario == 5:
        os.system('cls')
    elif opc_funcionario == 10:
        os.system('cls')
        return
    else:
        os.system('cls')
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")