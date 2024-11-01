import psycopg2 
#Função para conectar no banco de dados
def conexao():
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = 'post',
            host = 'localhost',
            port = '5432'
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
#Função para inserir informações de um novo cliente
def insercao_cliente(rg, cpf, nome_cliente, endereco_cliente, telefone_cliente):
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "INSERT INTO clientes (rg, cpf, nome_cliente, endereco_cliente, telefone_cliente) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (rg, cpf, nome_cliente, endereco_cliente, telefone_cliente))
        conn.commit()

        print("Cliente inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o cliente: {e}")
    finally:
        cursor.close()
        conn.close()

#Função para adicionar informações de um novo funcionario
def insercao_funcionario(rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario):
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "INSERT INTO funcionarios (rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario))
        conn.commit()

        print("Funcionario inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o funcionario: {e}")
    finally:
        cursor.close()
        conn.close()

#Função para cadastrar um novo remedio
def insercao_remedio(nome_remedio, marca, tarja, categoria, codigo, preco):
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "INSERT INTO remedios (nome_remedio, marca, tarja, categoria, codigo, preco) VALUES (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (nome_remedio, marca, tarja, categoria, codigo, preco))
        conn.commit()

        print("Remedio inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o remedio: {e}")
    finally:
        cursor.close()
        conn.close()

#Função para inserir uma nova venda
def insercao_venda(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda):
    conn = conexao()
    try: 

        cursor = conn.cursor()     
        query = "INSERT INTO vendas(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda)VALUES(%s, %s, %s, %s, %s, %s);"
        cursor.execute(query,(id_funcionario, id_cliente, id_remedio, valor_final, forma_pagamento, data_venda))       
        conn.commit()
        
        print("Venda informada com sucesso!")
    except Exception as e:
        print(f"Erro ao informar a venda: {e}")
    finally:        
        cursor.close()
        conn.close()

#Função para verificar as informações dos clientes
def selecao_cliente():
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "SELECT * FROM clientes"
        cursor.execute(query)
        selecionar_cliente = cursor.fetchall()
        print(selecionar_cliente)

        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        cursor.close()
        conn.close()

#Função para verificar as informações das vendas feitas
def selecao_venda():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "SELECT * FROM vendas"
        cursor.execute(query)        
        selecionar_venda = cursor.fetchall()
        print(selecionar_venda)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

#Função para verificar as informações do funcionario
def selecao_funcionario():
    conn = conexao()
    try:
        
        cursor = conn.cursor()    
        query = "SELECT * FROM funcionarios"
        cursor.execute(query)
        selecionar_funcionario = cursor.fetchall()
        print(selecionar_funcionario)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

#Função para verificar os remedios que estão cadastrados
def selecao_remedio():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "SELECT * FROM remedios"
        cursor.execute(query)
        selecionar_remedio = cursor.fetchall()
        print(selecionar_remedio)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

