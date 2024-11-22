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
        acessar_func()
    elif opcao == 3:
        break
    else:
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")