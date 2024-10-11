import os
def login_funcionario():
    while(True):
        print("Escolha qual ação deseja realizar")
        print("1 - Realizar venda | 2 - Sair")
        opc_funcionario = int(input("Digite sua escolha: "))
        if opc_funcionario == 1:
            os.system('cls')
            venda()
        elif opc_funcionario == 2:
            os.system('cls')
            return
        else:
            os.system('cls')
            print("Algum erro ocorreu na digitação da opção")
            print("Tente novamente")

def venda():
    os.system('cls')
    print("função de venda")