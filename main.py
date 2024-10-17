import os
from adm import acesso_adm
from funcionario import acesso_funcionario
while(True):
    print("1 - Login ADM | 2 - Login Funcionario | 3 - Finalizar")
    opcao = int(input("Digite uma das opções sinalizadas acima: "))
    if opcao == 1:
        print("Você esta na aba de administrador")
        acesso_adm()
    elif opcao == 2:
        print("Você esta na aba de funcionario")
        acesso_funcionario()
    elif opcao == 3:
        break
    else:
        print("Algum erro ocorreu na digitação da opção")
        print("Tente novamente")
