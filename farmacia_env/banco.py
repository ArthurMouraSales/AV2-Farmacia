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
def insercao_cliente(cpf, nome_cliente, endereco_cliente, telefone_cliente):
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "INSERT INTO clientes (cpf, nome_cliente, endereco_cliente, telefone_cliente) VALUES (%s, %s, %s, %s, %s);"
        cursor.execute(query, (cpf, nome_cliente, endereco_cliente, telefone_cliente))
        conn.commit()

        print("Cliente inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir o cliente: {e}")
    finally:
        cursor.close()
        conn.close()

#Função para adicionar informações de um novo funcionario
def insercao_funcionario(cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario):
    conn = conexao()
    try:

        cursor = conn.cursor()
        query = "INSERT INTO funcionarios (cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario) VALUES (%s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario))
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


def selecao_geral_vendas():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select v.id_venda, c.nome_cliente, f.nome_funcionario, r.nome_remedio, v.valor_final, v.forma_pagamento, v.data_venda from vendas v inner join clientes c on v.id_cliente = c.id_cliente inner join funcionarios f on v.id_funcionario = f.id_funcionario inner join remedios r on v.id_remedio = r.id_remedio;"
        cursor.execute(query)
        selecionar_geral_vendas = cursor.fetchall()
        print(selecionar_geral_vendas)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()


def selecao_venda_funcionario(id_funcionario):
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select v.id_venda, c.nome_cliente, r.nome_remedio, v.valor_final, v.forma_pagamento, v.data_venda from vendas v inner join clientes c on v.id_cliente = c.id_cliente inner join remedios r on  v.id_remedio = r.id_remedio where v.id_funcionario = %s"
        cursor.execute(query,(id_funcionario))
        selecionar_vendas_funcionario = cursor.fetchall()
        print(selecionar_vendas_funcionario)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_info_funcionario():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select f.id_funcionario, f.nome_funcionario from funcionarios f;"
        cursor.execute(query)
        selecionar_info_funcionarios = cursor.fetchall()
        print(selecionar_info_funcionarios)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_info_cliente():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select c.id_cliente, c.nome_cliente, c.cpf from clientes c;"
        cursor.execute(query)
        selecionar_info_clientes = cursor.fetchall()
        print(selecionar_info_clientes)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_info_remedios():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select r.id_remedio, r.nome_remedio, r.preco_remedio from remedios r;"
        cursor.execute(query)
        selecionar_info_remedios = cursor.fetchall()
        print(selecionar_info_remedios)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_info_vendas():
        conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select v.id_venda, v.data_venda from vendas v;"
        cursor.execute(query)
        selecionar_info_vendas = cursor.fetchall()
        print(selecionar_info_vendas)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()