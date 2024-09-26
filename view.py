import sqlite3  # Importando a biblioteca de banco de dados

# Conectando ao banco de dados
def connect():
    return sqlite3.connect('dados.db')

# Função para obter o papel do usuário pelo email
def get_user_role(email):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT papel FROM usuarios WHERE email = ?", (email,))
        result = c.fetchone()
    return result[0] if result else None  # Retorna o papel ou None se o usuário não for encontrado

# Função para inserir novo livro (Apenas Admin)
def insert_book(titulo, autor, editora, ano_publicacao, isbn, valor, email_usuario):
    papel = get_user_role(email_usuario)
    if papel != 'admin':
        print("Acesso negado! Apenas administradores podem inserir novos livros.")
        return

    with connect() as conn:
        conn.execute(
            "INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn, valor) VALUES (?, ?, ?, ?, ?, ?)",
            (titulo, autor, editora, ano_publicacao, isbn, valor),
        )
        conn.commit()
        print("Livro inserido com sucesso!")

# Função para deletar um livro (Apenas Admin)
def delete_book_by_isbn(isbn, email_usuario):
    papel = get_user_role(email_usuario)
    if papel != 'admin':
        print("Acesso negado! Apenas administradores podem deletar livros.")
        return
    
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM livros WHERE isbn = ?''', (isbn,))
        
        if cursor.rowcount > 0:
            print("Livro deletado com sucesso!")
        else:
            print("Livro não encontrado.")
        
        conn.commit()


# Função para inserir usuários
def insert_user(nome, sobrenome, endereco, email, telefone, senha, papel):
    with connect() as conn:
        conn.execute(
            "INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone, senha, papel) VALUES(?, ?, ?, ?, ?, ?, ?)",
            (nome, sobrenome, endereco, email, telefone, senha, papel),
        )
        conn.commit()

# Função para exibir usuários
def get_users():
    with connect() as conn:
        c = conn.cursor()
        # Selecionando apenas os campos desejados
        c.execute("SELECT id, nome, sobrenome, endereco, email, telefone, papel FROM usuarios ORDER BY nome ASC")
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

def validar_login(usuario, senha):
    # Verifica se o usuário é o "mestre"
    if usuario == "admin" and senha == "senhadomestre":
        return True  # Login bem-sucedido para o usuário mestre

    with connect() as conn:
        c = conn.cursor()
        # Verifica se o usuário e a senha (hashed) existem no banco de dados
        c.execute("SELECT * FROM usuarios WHERE nome=? AND senha=?", (usuario, senha))
        result = c.fetchone()
    
    return result is not None  