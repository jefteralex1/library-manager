import sqlite3

# Conectar ao BD ou criar um novo
with sqlite3.connect('dados.db') as con:

    # Criar tabela de livros, se não existir
    con.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        editora TEXT NOT NULL,
        ano_publicacao INTEGER,
        isbn TEXT UNIQUE NOT NULL,
        valor INTEGER
    )
    ''')

    # Criar tabela de usuários, se não existir
    con.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        endereco TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone TEXT NOT NULL,
        senha TEXT NOT NULL,
        papel TEXT NOT NULL CHECK(papel IN ('admin', 'usuario'))
    )
    ''')

# Criar tabela de empréstimos, se não existir
con.execute('''
CREATE TABLE IF NOT EXISTS emprestimos (
    id INTEGER PRIMARY KEY,
    id_livro INTEGER,
    id_usuario INTEGER,
    data_emprestimo TEXT,
    data_devolucao TEXT,
    FOREIGN KEY(id_livro) REFERENCES livros(id),
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id)
)
''')

# Fechar a conexão-
con.close()