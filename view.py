import sqlite3

# conectar ao bd
def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# função para inserir novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute(
        "INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
        (titulo, autor, editora, ano_publicacao, isbn),
    )
    conn.commit()
    conn.close()

# função para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute(
        "INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES(?, ?, ?, ?, ?)",
        (nome, sobrenome, endereco, email, telefone),
    )
    conn.commit()
    conn.close()

#funcao para exibir usuarios
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# função para exibir livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()

    return livros
exibir_livros()

def insert_loan(id, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id, id_usuario, data_emprestimo, data_devolucao)\
                 VALUES(?, ?, ?, ?)", (id, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

def geet_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao\
                          FROM livros\
                          INNER JOIN emprestimos ON livros.id = emprestimos.id_livro\
                          INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario\
                          WHERE emprestimos.data_devolucao IS NULL").fetchall()
    
    conn.close()
    return result

def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()