import os
from banco import insercao_venda, selecao_info_cliente, selecao_info_funcionario, selecao_info_remedios, selecao_cliente, selecao_geral_vendas, selecao_venda_funcionario, selecao_nao_vendidos, selecao_compras_cliente, selecao_clientes_remedio, selecao_remedio_pdia, selecao_clientes_mais_um_remedio
from verificacao import login_funcionario, login_adm

def acesso_funcionario():
    if login_funcionario() == True or login_adm() == True:
        while(True):
            print("Escolha qual ação deseja realizar")
            print("""
            --------------------------------------
            1 - Realizar venda
            2 - Consultar clientes
            3 - Selecionar todas as vendas
            4 - Vendas diaria do funcionario
            5 - Consultar remedios que não foram vendidos
            6 - Consultar compras realizadas por determinado cliente
            7 - Consultar clientes que compraram determinado remedio
            8 - Consultar remedios vendidos mais de uma vez no mesmo dia
            9 - Consultar remedios que foram comprados mais de uma unidade por cliente
            10 - Sair
            --------------------------------------
            """)
            
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
                selecao_nao_vendidos()
            elif opc_funcionario == 6:
                os.system('cls')
                selecao_info_cliente
                id_cliente = input("Digite o id do cliente que você deseja verificar: ")
                selecao_compras_cliente(id_cliente)
            elif opc_funcionario == 7:
                os.system('cls')
                selecao_info_remedios
                nome_remedio = input("Digite o id do cliente que você deseja verificar: ")
                selecao_clientes_remedio(nome_remedio)
            elif opc_funcionario == 8:
                os.system('cls')
                selecao_remedio_pdia()
            elif opc_funcionario == 9:
                os.system('cls')
                selecao_clientes_mais_um_remedio()
            elif opc_funcionario == 10:
                os.system('cls')
                return
            else:
                os.system('cls')
                print("Algum erro ocorreu na digitação da opção")
                print("Tente novamente")
    else:
        return

def venda():
    valor_remedio = 0
    valor_parcial = 0
    print("Digite as informações pedidas a seguir.")
    selecao_info_funcionario()
    id_funcionario = int(input("Informe o ID do funcionario:  "))
    selecao_info_cliente()
    id_cliente = int(input("Informe o ID do cliente:  "))
    selecao_info_remedios()
    id_remedio = int(input("Informe o ID do remédio:  "))
    valor_remedio = float(input("Digite o valor do remedio: "))
    valor_parcial += valor_remedio
    forma_pagamento = input("Informe a forma de pagamento:  ")
    data_venda = input("Informe a data da venda:  ")
    valor_final = valor_parcial
    print(f"Valor final da compra: {valor_final} ")
    insercao_venda(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda)
    
