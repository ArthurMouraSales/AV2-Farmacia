import os
from banco import insercao_venda, selecao_info_cliente, selecao_info_funcionario, selecao_info_remedios
from verificacao import login_funcionario, login_adm
from menus import menu_funcionario

def acesso_funcionario():
    if login_funcionario() == True or login_adm() == True:
        while(True):
            menu_funcionario()
    else:
        return

def venda():
    print("Digite as informações pedidas a seguir.")
    selecao_info_funcionario()
    id_funcionario = int(input("Informe o ID do funcionario:  "))
    selecao_info_cliente()
    id_cliente = int(input("Informe o ID do cliente:  "))
    selecao_info_remedios()
    id_remedio = int(input("Informe o ID do remédio:  "))
    valor_final =  float(input("Informe o valor final da compra:  "))
    forma_pagamento = input("Informe a forma de pagamento:  ")
    data_venda = input("Informe a data da venda:  ")
    insercao_venda(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda)
    
