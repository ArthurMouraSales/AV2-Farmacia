import psycopg2 

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


def selecao_nao_vendidos():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select r.nome_remedio from remedios r left join vendas v on r.id_remedio = v.id_remedio where v.id_venda is null;"
        cursor.execute(query)
        selecionar_nao_vendidos = cursor.fetchall()
        print(selecionar_nao_vendidos)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_compras_cliente(id_cliente):
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select v.id_venda, f.nome_funcionario,  r.nome_remedio, v.valor_final, v.forma_pagamento, v.data_venda from vendas v inner join funcionarios f on v.id_funcionario = f.id_funcionario inner join remedios r on v.id_remedio = r.id_remedio where v.id_cliente = %s;"
        cursor.execute(query,(id_cliente))
        selecionar_compras_cliente = cursor.fetchall()
        print(selecionar_compras_cliente)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_clientes_remedio(nome_remedio):
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select c.nome_cliente, v.id_venda, v.valor_final, v.forma_pagamento, v.data_venda from vendas v inner join clientes c on v.id_cliente = c.id_cliente inner join remedios r on v.id_remedio = r.id_remedio where r.nome_remedio = %s;"
        cursor.execute(query,(nome_remedio))
        selecionar_clientes_remedio = cursor.fetchall()
        print(selecionar_clientes_remedio)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_remedio_pdia():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select r.nome_remedio, v.data_venda, COUNT(v.id_venda) as quantidade vendida from vendas v inner join remedios r on v.id_remedio = r.id_remedio group by r.nome_remedio, v.data_venda having COUNT(v.id_venda) > 1;"
        cursor.execute(query)
        selecionar_remedios_pdia = cursor.fetchall()
        print(selecionar_remedios_pdia)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()

def selecao_clientes_mais_um_remedio():
    conn = conexao()
    try:
        
        cursor = conn.cursor()
        query = "select c.nome_cliente, COUNT(DISTINCT v.id_remedio) as total remédios from vendas v inner join clientes c on v.id_cliente = c.id_cliente group by c.nome_cliente having COUNT(DISTINCT v.id_remedios) > 1;"
        cursor.execute(query)
        selecionar_clientes_mais_um_remedio = cursor.fetchall()
        print(selecionar_clientes_mais_um_remedio)
        
        conn.commit()
    except Exception as e:
        print(f"Erro: {e}")  
    finally:
        cursor.close()
        conn.close()