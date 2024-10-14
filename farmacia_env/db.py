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

def insercao_add_funcionario(rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario):
    conn = conexao()

    try:

        cursor = conn.cursor()

        query = "INSERT INTO funcionarios (rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario) VALUES (%s, %s, %s, %s, %s, %s, %s);"

        cursor.execute(query, (rg_funcionario, cpf_funcionario, nome_funcionario, idade_funcionario, salario, turno, telefone_funcionario))

        conn.commit()

        print("Usuário inserido com sucesso!")

    except Exception as e:

        print(f"Erro ao inserir usuário: {e}")

    finally:

        cursor.close()

        conn.close()