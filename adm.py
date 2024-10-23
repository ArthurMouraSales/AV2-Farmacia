import os
import psycopg2
from banco import insercao_funcionario
from banco import insercao_cliente
from banco import insercao_remedio
from banco import selecao_cliente
from banco import selecao_funcionario
from banco import selecao_remedio
from verificacao import login_adm

#Função para acessar as possibilidades que o adm tem no sistema
def acesso_adm():
    if login_adm() == True:
        while(True):
            print("Escolha qual ação deseja realizar")
            print("1 - Cadastro novo funcionario | 2 - Cadastro novo cliente | 3 - Cadastro novo remedio | 4 - Listar funcionarios | 5 - Listar clientes | 6 - Listar remedios | 7 - Sair")
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
    else:
        return
#Função para obter as informações de um novo funcionario
def add_funcionario():
    os.system('cls')
    print("Digite as informações pedidas a seguir")
    rg_funcionario = input("Digite o RG: ")
    cpf_funcionario = input("Digite o CPF: ")
    nome_funcionario = input("Digite o nome: ")
    idade_funcionario = int(input("Digite a idade: "))
    salario = float(input("Digite o salario: "))
    turno = input("Digite o turno: ")
    telefone_funcionario = input("Digite o telefone para contato: ")
    insercao_funcionario(rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario)
#Função para obter as informações de um novo cliente   
def add_cliente():
    os.system('cls')
    print("Digite as informações pedidas a seguir")
    rg = input("Digite o RG: ")
    cpf = input("Digite o CPF: ")
    nome_cliente = input("Digite o nome: ")
    endereco_cliente = input("Digite o endereço: ")
    telefone_cliente = input("Digite o telefone para contato: ")
    insercao_cliente(rg, cpf, nome_cliente, endereco_cliente, telefone_cliente)
#Função para obter as informações de um novo remedio
def add_remedio():
    os.system('cls')
    print("Digite as informações pedidas a seguir")
    nome_remedio = input("Digite o nome: ")
    marca = input("Digte a marca: ")
    tarja = input("Digite a cor da tarja: ")
    categoria = input("Digite a categoria: ")
    codigo = input("Digite o codigo: ")
    preco = float(input("Digite o preço: "))
    insercao_remedio(nome_remedio, marca, tarja, categoria, codigo, preco)
