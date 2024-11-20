from banco import login_adm, login_func
from adm import acesso_adm
from funcionario import acesso_funcionario
import pwinput

def acessar_adm():
    is_authenticated_adm = False
    while(not is_authenticated_adm):
        username = input("Digite seu usuario: ")
        password = pwinput.pwinput(prompt="Digite sua senha: ", mask='*')
        user = login_adm(username, password)
        if user:
            print("Acesso Liberado!")
            is_authenticated_adm = True
            acesso_adm()
        else:
            print("Usuário e/ou senhas inválidos")
        
def acessar_func():
    is_authenticated_func = False
    while(not is_authenticated_func):
        username = input("Digite seu usuario: ")
        password = pwinput.pwinput(prompt="Digite sua senha: ", mask='*')
        user = login_func(username, password)
        if user:
            print("Acesso Liberado!")
            is_authenticated_func = True
            acesso_funcionario()
        else:
            print("Usuário e/ou senhas inválidos")
