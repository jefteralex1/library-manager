# Sistema de Gerenciamento de Livros

Este projeto é um sistema de gerenciamento de livros desenvolvido com a biblioteca `Tkinter` para a interface gráfica. O sistema permite a inserção de novos usuários e livros, visualização de registros, e a realização de empréstimos.

## Funcionalidades

- **Adicionar Usuário:** Insere novos usuários com informações como nome, endereço, email e telefone.
- **Visualizar Usuários:** Exibe uma lista de todos os usuários cadastrados.
- **Adicionar Livro:** Adiciona novos livros com informações como título, autor, editora, ano, ISBN e valor.
- **Visualizar Livros:** Mostra uma lista de todos os livros disponíveis com o valor total do inventário.
- **Realizar Empréstimo:** Registra o empréstimo de um livro a um usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver o sistema.
- **Tkinter**: Biblioteca para a criação da interface gráfica.
- **Pillow (PIL)**: Biblioteca para manipulação de imagens.
- **Tkinter Treeview**: Widget para exibição de listas e tabelas.

## Estrutura do Código

- **Imports:** Importa bibliotecas essenciais para a interface gráfica, manipulação de imagens, mensagens de erro, e operações com datas.
- **Configuração da Janela Principal:** Define a janela principal do sistema com suas dimensões, estilo e tema.
- **Frames:** Organiza a interface em diferentes seções para o cabeçalho, menu lateral e área principal de exibição.
- **Logotipo:** Carrega e exibe o logotipo do sistema na parte superior da janela.

### Principais Funções

1. **`novo_usuario()`**: Formulário para adicionar um novo usuário ao sistema.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe mensagens de erro ou sucesso conforme o preenchimento dos campos.

2. **`ver_usuarios()`**: Exibe todos os usuários cadastrados em um formato de tabela utilizando o widget `Treeview`.
   - Adiciona barras de rolagem para navegação.

3. **`novo_livro()`**: Formulário para adicionar um novo livro ao sistema.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe mensagens de erro ou sucesso conforme o preenchimento dos campos.

4. **`ver_livros()`**: Exibe todos os livros cadastrados em um formato de tabela, incluindo o valor total do inventário.
   - Adiciona barras de rolagem para navegação.

5. **`realizar_emprestimo()`**: Formulário para realizar o empréstimo de um livro para um usuário.
   - Valida os campos e insere os dados no banco de dados.
   - Exibe mensagens de erro ou sucesso conforme o preenchimento dos campos.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Instale as dependências utilizando o seguinte comando:

   ```bash
   pip install Pillow
   pip install Tkinter
   pip install sqlite
3. Execute o seguinte comando:
   python main.py


## Contato
Para mais informações ou suporte, entre em contato com o desenvolvedor através de [jefteralexandre73@gmail.com].
