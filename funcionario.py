import os
from banco import selecao_cliente
from banco import insercao_add_venda
def login_funcionario():
    while(True):
        print("Escolha qual ação deseja realizar")
        print("1 - Realizar venda | 2 - Consultar clientes | 3 - Sair")
        opc_funcionario = int(input("Digite sua escolha: "))
        if opc_funcionario == 1:
            os.system('cls')
            venda()
        elif opc_funcionario == 2:
            os.system('cls')
            selecao_cliente()
        elif opc_funcionario == 3:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Algum erro ocorreu na digitação da opção")
            print("Tente novamente")

def venda():
    
    print("Digite as informações pedidas a seguir.")
    id_funcionario = int(input("Informe o ID do funcionario:  "))
    id_cliente = int(input("Informe o ID do cliente:  "))
    id_remedio = int(input("Informe o ID do remédio:  "))
    valor_final =  float(input("Informe o valor final da compra:  "))
    forma_pagamento = input("Informe a forma de pagamento:  ")
    data_venda = input("Informe a data da venda:  ")
    insercao_add_venda(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda)
    
