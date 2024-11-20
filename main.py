from funcionario import acesso_funcionario
from verificacao import acessar_adm, acessar_func

while(True):
    print("Seja bem vindo ao sistema interno de nossa empresa!")
    print(""" 
    --------------------------------------
    1 - Login ADM
    2 - Login Funcionario
    3 - Finalizar
    --------------------------------------
    """)

    opcao = int(input("Digite uma das opções sinalizadas acima: "))
    if opcao == 1:
        acessar_adm()
    elif opcao == 2:
        print("Digite 1 para entrar como adm e 2 para entrar como funcionario")
        opc_acesso = int(input("Digite o tipo de acesso: "))
        if opc_acesso == 1:
            acessar_adm()
        elif opc_acesso == 2:
            acessar_func()
        else:
            print("Erro na escolha da opção")
    elif opcao == 3:
        break
    else:
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")