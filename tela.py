from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from datetime import date, datetime
from view import *

hoje = datetime.today()

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#E9A178"


# função de criar novo usuario
def novo_usuario():

    global img_salvar

    def add():
        first_name = e_p_nome.get()
        last_name = e_sobrenome.get()
        adress = e_endereco.get()
        email = e_email.get()
        phone = e_numero.get()
        senha = e_senha.get()
        papel = e_papel.get()


        lista = [first_name, last_name, adress, email, phone, senha, papel]

        #verificando caso algum campo esteja em branco
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        #inserindo os dados no bd
        insert_user(first_name, last_name, adress, email, phone, senha, papel)

        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso')

        #limpando os campos após inserir
        e_p_nome.delete(0,END)
        e_sobrenome.delete(0,END)
        e_endereco.delete(0,END)
        e_email.delete(0,END)
        e_numero.delete(0,END)
        e_senha.delete(0,END)
        e_papel.delete(0,END)

    app_ = Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, font=("verdana 12 "), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)

    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=("Verdana 1"), fg=co1, bg=co3)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    #formularios
    l_p_nome = Label(frameDireita, text="Primeiro nome*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_p_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_p_nome = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_p_nome.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #sobrenome
    l_sobrenome = Label(frameDireita, text="Sobrenome*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_sobrenome = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_sobrenome.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #endereco
    l_endereco = Label(frameDireita, text="Endereco do usario*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_endereco.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    #email
    l_email = Label(frameDireita, text="Endereco de email do usuário:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_email.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    #numero
    l_numero = Label(frameDireita, text="Numero de telefone do usuário:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_numero.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)
    e_numero = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_numero.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)

    #senha
    l_senha = Label(frameDireita, text="senha do usuário:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_senha.grid(row=7, column=0, padx=5, pady=10, sticky=NSEW)
    e_senha = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_senha.grid(row=7, column=1, padx=5, pady=10, sticky=NSEW)

    #papel
    l_papel = Label(frameDireita, text="papel do usuário:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_papel.grid(row=8, column=0, padx=5, pady=10, sticky=NSEW)
    e_papel = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_papel.grid(row=8, column=1, padx=5, pady=10, sticky=NSEW)

    #botao de salvar
    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, anchor=NW, width=100, text=" Salvar ", bg=co1, fg=co4, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=9, column=1, pady=10, sticky=NSEW)


# função para vizualizar novos usuarios
def ver_usuarios():

    app_ = Label(frameDireita, text="Ver os usuarios", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_users()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Sobrenome','Endereço','Email','Telefone', 'Papel']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","nw", "nw"]
    h=[20,80,80,120,120,76,100, 76]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


# função para adicionar novos livros
def novo_livro():
    global img_salvar, img_deletar

    def add():
        title = e_titulo.get()
        autor = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()
        valor = e_valor.get()
        email = e_email.get()

        lista = [title, autor, publisher, year, isbn, valor, email]

        # Verificando caso algum campo esteja em branco
        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        # Verificar o papel do usuário antes de inserir
        papel = get_user_role(email)
        if papel != 'admin':
            messagebox.showerror('Erro', 'Acesso negado! Apenas administradores podem inserir novos livros.')
            return

        # Inserindo os dados no banco de dados
        try:
            insert_book(title, autor, publisher, year, isbn, valor, email)
            messagebox.showinfo('Sucesso', 'Livro inserido com sucesso')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao inserir livro: {e}')

        limpar_campos()

    def delete():
        isbn = e_isbn.get()
        email = e_email.get()

        if isbn == '':
            messagebox.showerror('Erro', 'Por favor, insira o ISBN para deletar um livro')
            return

        # Verificar o papel do usuário antes de deletar
        papel = get_user_role(email)
        if papel != 'admin':
            messagebox.showerror('Erro', 'Acesso negado! Apenas administradores podem deletar livros.')
            return

        # Deletar o livro usando o ISBN
        try:
            delete_book_by_isbn(isbn, email)
            messagebox.showinfo('Sucesso', 'Livro deletado com sucesso')
        except Exception as e:
            messagebox.showerror('Erro', f'Erro ao deletar livro: {e}')

        limpar_campos()

    def limpar_campos():
        e_titulo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)
        e_valor.delete(0, END)
        e_email.delete(0, END)

    # Botão de deletar
    img_deletar = Image.open('img/book.png')
    img_deletar = img_deletar.resize((18, 18))
    img_deletar = ImageTk.PhotoImage(img_deletar)
    b_deletar = Button(frameDireita, command=delete, image=img_deletar, compound=LEFT, anchor=NW, width=100, text=" Deletar ", bg=co1, fg=co4, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_deletar.grid(row=10, column=1, pady=10, sticky=NSEW)

    app_ = Label(frameDireita, text="Inserir um Novo livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Formulários
    l_titulo = Label(frameDireita, text="Título do livro*", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_titulo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_titulo = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_titulo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    l_autor = Label(frameDireita, text="Autor do livro*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_autor.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    l_editora = Label(frameDireita, text="Editora do Livro*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_editora.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)

    l_ano = Label(frameDireita, text="Ano de Publicação do livro:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_ano.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

    l_isbn = Label(frameDireita, text="ISBN do livro:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_isbn.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)
    e_isbn = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_isbn.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)

    l_valor = Label(frameDireita, text="Valor do livro:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_valor.grid(row=7, column=0, padx=5, pady=10, sticky=NSEW)
    e_valor = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_valor.grid(row=7, column=1, padx=5, pady=10, sticky=NSEW)

    l_email = Label(frameDireita, text="Email do usuário:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_email.grid(row=8, column=0, padx=5, pady=10, sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_email.grid(row=8, column=1, padx=5, pady=10, sticky=NSEW)

    #botao de salvar
    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, anchor=NW, width=100, text=" Salvar ", bg=co1, fg=co4, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=9, column=1, pady=10, sticky=NSEW)


# função para ver os livros
def ver_livros():
    # Cabeçalho da seção de livros
    app_ = Label(frameDireita, text="Todos os livros", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)

    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    # Obtendo os dados dos livros e o valor total do estoque
    livros, total_estoque = exibir_livros()

    # Criando o Treeview com barras de rolagem
    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISBN', 'Valor']
    
    global tree
    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")

    # Barra de rolagem vertical
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    # Barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    # Definindo o alinhamento e largura das colunas
    hd = ["nw", "nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 165, 110, 100, 50, 100, 80]  # Largura das colunas
    n = 0

    # Configurando os cabeçalhos e colunas
    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # Inserindo os dados dos livros no Treeview
    for item in livros:
        tree.insert('', 'end', values=item)

    # Exibindo o valor total do estoque
    total_label = Label(frameDireita, text=f"Valor total do inventário: R$ {total_estoque:.2f}", font=('Verdana 10 bold'), bg=co1, fg=co4)
    total_label.grid(row=4, column=0, columnspan=3, pady=10, sticky=NSEW)


# função para realizar um emprestimo
def realizar_emprestimo():
    global img_salvar

    def add():
        user_id = e_id_usuario.get()
        book_id = e_id_livro.get()

        lista = [user_id, book_id]

        #verificando caso algum campo esteja em branco
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        #inserindo os dados no bd
        insert_loan(user_id, book_id, hoje, None)

        messagebox.showinfo('Sucesso', 'Emprestimo realizado com sucesso')

        #limpando os campos após inserir
        e_id_usuario.delete(0,END)
        e_id_livro.delete(0,END)
        

    app_ = Label(frameDireita, text="Realizar um emprestimo", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)


    #id do usuario
    l_id_usuario = Label(frameDireita, text="Digite o ID do usuario*", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_id_usuario.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_id_usuario.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #id do livro
    l_id_livro = Label(frameDireita, text="Digite o ID do livro*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_id_livro.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_id_livro.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #botao de salvar
    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, anchor=NW, width=100, text=" Salvar ", bg=co1, fg=co4, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=10, sticky=NSEW)


# função para ver os livros emprestados no momento
def ver_livros_emprestados():
    app_ = Label(frameDireita, text="Livros emprestados no momento", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []

    books_on_loan = get_books_on_loan()

    for book in books_on_loan:
        dado = [f"{book[0]}", f"{book[1]}", f" {book[2]} {book[3]}", f"{book[4]}", f"{book[5]}" ]
        dados.append(dado)

    #creating a treeview with dual scrollbars
    list_header = ['ID','Título','Nome do usuario','D. emprestimo','D. devolução']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
   
    #vertical scrollbar
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","ne","ne"]
    h=[20,175,120,90,90,100,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


# função para devolução de um livro
def devolucao_emprestimo():
    global img_salvar

    def add():
        loan_id = int(e_id_emprestimo.get())
        return_date = e_data_retorno.get()
        lista = [loan_id, return_date]

        #verificando caso algum campo esteja em branco
        for i in lista:
            if i=='':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        
        #inserindo os dados no bd
        update_loan_return_date(loan_id, return_date)

        messagebox.showinfo('Sucesso', 'Devolução realizada com sucesso')

        #limpando os campos após inserir
        e_id_emprestimo.delete(0,END)
        e_data_retorno.delete(0,END)
        

    app_ = Label(frameDireita, text="Realizar uma devolução", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)


    #id do usuario
    l_id_emprestimo = Label(frameDireita, text="ID do emprestimo*", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_emprestimo = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_id_emprestimo.grid(row=2, column=1, padx=5, pady=5, sticky=NSEW)

    #id do livro
    l_data_retorno = Label(frameDireita, text="Nova data de devolução (formato: AAAA-MM-DD)*:", anchor=NW, font=("Ivy 10 "), bg=co1, fg=co4)
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_data_retorno.grid(row=3, column=1, padx=5, pady=5, sticky=NSEW)

    #botao de salvar
    img_salvar = Image.open('img/save.png')
    img_salvar = img_salvar.resize((18,18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, anchor=NW, width=100, text=" Salvar ", bg=co1, fg=co4, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_salvar.grid(row=7, column=1, pady=10, sticky=NSEW)


#funcao para controlar o menu
def control(i):

    #novo usario
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao para criar um novo usuario
        novo_usuario()

    #ver usarios
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao para ver os usuarios
        ver_usuarios()

    #novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao para ver os usuarios
        novo_livro()

    #ver livros
    if i == 'ver_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao para ver os usuarios
        ver_livros()

    #Realizar emprestimo
    if i == 'emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao emprestimo
        realizar_emprestimo()

    #Ver livros emprestados
    if i == 'ver_livros_emprestado':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao emprestimo
        ver_livros_emprestados()

    #retorno do emprestimo
    if i == 'retorno':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        #chamando a funcao de devolucao
        devolucao_emprestimo()


# tela do menu principal
def janela_principal():
    janela = Tk()
    janela.title("")
    janela.geometry('800x600')
    janela.configure(background=co1)
    janela.resizable(width=False, height=False)

    style = Style(janela)
    style.theme_use("clam")

    #frames
    global frameCima
    frameCima = Frame(janela, width=770, height=50, bg=co6, relief="flat")
    frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

    global frameEsquerda
    frameEsquerda = Frame(janela, width=150, height=265, bg=co4, relief="solid")
    frameEsquerda.grid(row=1, column=0, sticky=NSEW)

    global frameDireita
    frameDireita = Frame(janela, width=600, height=265, bg=co1, relief="raised")
    frameDireita.grid(row=1, column=1, sticky=NSEW)


    #logo
    #abrindo a imagem
    app_img = Image.open('img/book.png')
    app_img = app_img.resize((40,40))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, fg=co1, bg=co6)
    app_logo.place(x=5, y=0)

    app_ = Label(frameCima, text="Sistema de Gerenciamento de Livros", compound=LEFT, padx=5, anchor = NW, fg=co1, bg=co6, font=("Verdana 15 bold"))
    app_.place(x=50, y=7)

    app_linha = Label(frameCima, width=770, height=1, padx=5, anchor=NW, font=("Verdana"), fg=co1, bg=co3)
    app_linha.place(x=0, y=47)

    #Menu
    #novo usuario
    img_usuario = Image.open('img/add.png')
    img_usuario = img_usuario.resize((18,18))
    img_usuario = ImageTk.PhotoImage(img_usuario)
    b_usuario = Button(frameEsquerda, command=lambda:control('novo_usuario'),  image=img_usuario, compound=LEFT, anchor=NW, text=" Novo usuário", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

    #novo livro
    img_novo_livro = Image.open('img/add.png')
    img_novo_livro = img_novo_livro.resize((18,18))
    img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
    b_novo_livro = Button(frameEsquerda, command=lambda:control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text=" Novo Livro", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver livros
    img_ver_livro = Image.open('img/book.png')
    img_ver_livro = img_ver_livro.resize((18,18))
    img_ver_livro = ImageTk.PhotoImage(img_ver_livro)
    b_ver_livro = Button(frameEsquerda, command=lambda:control('ver_livro'), image=img_ver_livro, compound=LEFT, anchor=NW, text=" Exibir todos os Livro", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_ver_livro.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver usuarios
    img_ver_usuarios = Image.open('img/user.png')
    img_ver_usuarios = img_ver_usuarios.resize((18,18))
    img_ver_usuarios = ImageTk.PhotoImage(img_ver_usuarios)
    b_ver_usuarios = Button(frameEsquerda, image=img_ver_usuarios, command=lambda:control('ver_usuarios'), compound=LEFT, anchor=NW, text=" Exibir todos os usuarios", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_ver_usuarios.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

    #Realizar emprestimo
    img_emprestimo = Image.open('img/purchase.png')
    img_emprestimo = img_emprestimo.resize((18,18))
    img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
    b_emprestimo = Button(frameEsquerda, command=lambda:control('emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=" Realizar um emprestimo", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

    #Realizar devolucao
    img_devolucao = Image.open('img/update.png')
    img_devolucao = img_devolucao.resize((18,18))
    img_devolucao = ImageTk.PhotoImage(img_devolucao)
    b_devolucao = Button(frameEsquerda, command=lambda:control('retorno'), image=img_devolucao, compound=LEFT, anchor=NW, text=" Devolucao de um emprestimo", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

    #Ver livros emprestados
    img_livros_emprestados = Image.open('img/purchase.png')
    img_livros_emprestados = img_livros_emprestados.resize((18,18))
    img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
    b_livros_emprestados = Button(frameEsquerda, command=lambda:control('ver_livros_emprestado'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text=" Livros emprestados no momento", bg=co4, fg=co1, font=("Ivy 11"), overrelief=RIDGE, relief=GROOVE)
    b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)

    janela.mainloop()


# Função que executa a tela de login
def tela_login():
    def fazer_login():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        
        if validar_login(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            login_screen.destroy()  # Fecha a tela de login
            janela_principal()  # Abre a tela principal do sistema
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    # Criando a janela de login
    login_screen = Tk()
    login_screen.title("Login")

    # Widgets de login
    Label(login_screen, text="Usuário:").pack(pady=5)
    entry_usuario = Entry(login_screen)
    entry_usuario.pack(pady=5)

    Label(login_screen, text="Senha:").pack(pady=5)
    entry_senha = Entry(login_screen, show='*')  # Campo de senha oculto
    entry_senha.pack(pady=5)

    Button(login_screen, text="Entrar", command=fazer_login).pack(pady=20)

    login_screen.geometry("300x200")
    login_screen.mainloop()


# Executa a tela de login ao iniciar o sistema
if __name__ == "__main__":
    tela_login()