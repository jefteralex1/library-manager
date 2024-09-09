import sqlite3  # Importando a biblioteca de banco de dados

# Conectando ao banco de dados
def connect():
    return sqlite3.connect('dados.db')

# Função para inserir novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn, valor):
    with connect() as conn:
        conn.execute(
            "INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn, valor) VALUES (?, ?, ?, ?, ?, ?)",
            (titulo, autor, editora, ano_publicacao, isbn, valor),
        )
        conn.commit()

# Função para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    with connect() as conn:
        conn.execute(
            "INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES(?, ?, ?, ?, ?)",
            (nome, sobrenome, endereco, email, telefone),
        )
        conn.commit()

# Função para exibir usuários
def get_users():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios")
        users = c.fetchall()
    return users

# Função para exibir livros e total do estoque
def exibir_livros():
    with connect() as conn:
        livros = conn.execute("SELECT * FROM livros").fetchall()
        result = conn.execute(
            "SELECT SUM(valor) AS total_estoque FROM livros"
        ).fetchone()
    return livros, result[0] if result[0] is not None else 0  # Retorna 0 se o resultado for None

# Função para inserir um empréstimo
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    with connect() as conn:
        conn.execute(
            "INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES(?, ?, ?, ?)",
            (id_livro, id_usuario, data_emprestimo, data_devolucao)
        )
        conn.commit()

# Função para obter livros em empréstimo
def get_books_on_loan():
    with connect() as conn:
        result = conn.execute(
            "SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
             FROM livros\
             INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
             INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
             WHERE emprestimos.data_devolucao IS NULL"
        ).fetchall()
    return result

# Função para atualizar a data de devolução do empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    with connect() as conn:
        conn.execute(
            "UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",
            (data_devolucao, id_emprestimo)
        )
        conn.commit()

# Função para obter o total do estoque
def inventario():
    with connect() as conn:
        result = conn.execute(
            "SELECT SUM(valor) AS total_estoque FROM livros"
        ).fetchone()
    return result[0] if result[0] is not None else 0  # Retorna 0 se o resultado for None
