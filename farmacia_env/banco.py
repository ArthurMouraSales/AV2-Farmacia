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
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None

def insercao_add_cliente(rg_cliente, cpf_cliente, nome_cliente, endereco_cliente, telefone_cliente):
    conn = conexao()
    try:

        cursor = conn.cursor()

        query = "INSERT INTO clientes (rg_cliente, cpf_cliente, nome_cliente, endereco_cliente, telefone_cliente) VALUES (%s, %s, %s, %s, %s);"

        cursor.execute(query, (rg_cliente, cpf_cliente, nome_cliente, endereco_cliente, telefone_cliente))

        conn.commit()

        print("Cliente inserido com sucesso!")
    except Exception as e:

        print(f"Erro ao inserir o cliente: {e}")
    finally:

        cursor.close()

        conn.close()

def insercao_add_funcionario(rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario):
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

def insercao_add_remedio(nome_remedio, marca, tarja, categoria, codigo, preco):
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