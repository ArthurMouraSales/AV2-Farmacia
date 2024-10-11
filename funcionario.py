def login_funcionario():
    while(True):
        print("Escolha qual ação deseja realizar")
        print("1 - Realizar venda | 2 - Sair")
        opc_funcionario = int(input("Digite sua escolha: "))
        if opc_funcionario == 1:
            print("venda")
            venda()
        elif opc_funcionario == 2:
            print("deveria sair")
        else:
            print("Algum erro ocorreu na digitação da opção")
            print("Tente novamente")

def venda():
    print("função de venda")