import os
from adm import acesso_adm
from funcionario import acesso_funcionario
from menus import menu_principal
while(True):
    #Area de escolha onde a pessoa quer acessar
    menu_principal()
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
