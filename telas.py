#EM TESTES
'''from ttkbootstrap.constants import *
from tkinter import *
from ttkbootstrap import *
import tkinter as tk
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
#Titulo do sistema e tamanho que a tela vai abrir sempre
root.title("BOA FARMA")
root.geometry('700x700')
logo = tk.PhotoImage(file="C:/Users/arthu/Downloads/logo_teste.png")
#Imagem
root.iconphoto(True, logo)


cadastros = [
    {
        "user":"arthur",
        "senha":"12345"
    },
]


#Functions

def speak():
    username_input = username.get()
    password_input = password.get()
    for speak in cadastros:
        if username_input == cadastros[0]["user"] and password_input == cadastros[0]["senha"]:
            msg = tb.Label(root, text="Acesso Liberado!")
            msg.pack(pady=5)
        else:
            msg2 = tb.Label(root, text="Acesso Negado!")
            msg2.pack(pady=5)


#Possible styles:
# default, primary, secondary, success, info, warning, danger, light, dark


#Widgets de entrada/Componentes da tela
label1 = tb.Label(root, text="Enter your username")
label1.pack(pady=5)
username = tb.Entry(root)
username.pack(pady=40)

label3 = tb.Label(root, text="")
label3.pack(pady=5)

label2 = tb.Label(root, text="Enter your password")
label2.pack(pady=5)
password = tb.Entry(root, show="*")
password.pack(pady=40)

label4 = tb.Label(root, text="")
label4.pack(pady=5)

#Botão
my_button = tb.Button(text="Acessar", bootstyle="danger", command=speak)
my_button.pack(pady=20)

root.mainloop()'''