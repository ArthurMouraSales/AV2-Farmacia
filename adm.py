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
        else:
            print("Algum erro ocorreu na digitação da opção")
            print("Tente novamente")

def add_funcionario():
    print("a")

def add_cliente():
    print("b")

def add_remedio():
    print("c")