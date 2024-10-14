import os
import psycopg2
from db import insercao_add_funcionario
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
    rg_funcionario = input("Digite o RG: ")
    cpf_funcionario = input("Digite o CPF: ")
    nome_funcionario = input("Digite o nome: ")
    idade_funcionario = int(input("Digite a idade: "))
    salario = float(input("Digite o salario: "))
    turno = input("Digite o turno: ")
    telefone_funcionario = input("Digite o telefone para contato: ")
    insercao_add_funcionario(rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario)


    

def add_cliente():
    print("Digite as informações pedidas a seguir")
    rg_cliente = input("Digite o RG: ")
    cpf_cliente = input("Digite o CPF: ")
    nome_cliente = input("Digite o nome: ")
    endereco_cliente = input("Digite o endereço: ")
    telefone_cliente = input("Digite o telefone para contato: ")

def add_remedio():
    print("Digite as informações pedidas a seguir")
    nome_remedio = input("Digite o nome: ")
    marca = input("Digte a marca: ")
    tarja = input("Digite a cor da tarja: ")
    categoria = input("Digite a categoria: ")
    codigo = input("Digite o codigo: ")
    preco = float(input("Digite o preço: "))