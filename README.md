# 🎬 Catálogo de Filmes - Django

Um sistema de gerenciamento de catálogo de filmes moderno, desenvolvido com Python e Django. O projeto permite realizar o CRUD completo (Criar, Ler, Atualizar e Deletar) de filmes, com uma interface elegante e validações robustas.

## ✨ Funcionalidades

-   **Listagem de Filmes**: Visualização de todos os filmes cadastrados em formato de cards.
-   **Cadastro e Edição**: Formulário estilizado para adicionar novos filmes ou editar as informações de títulos existentes.
-   **Exclusão Segura**: Página de confirmação antes de remover qualquer item do catálogo.
-   **Validações Inteligentes**: Verificação de dados antes de salvar (ex: ano de lançamento válido, tamanho mínimo de título e descrição).
-   **Design Premium**: Interface escura com efeito de desfoque (Glassmorphism), responsiva e com foco na experiência do usuário.

## 🚀 Tecnologias Utilizadas

-   [Python](https://www.python.org/) 3.10+
-   [Django](https://www.djangoproject.com/) 5.2
-   [HTML5 / CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS) (Vanilla CSS)
-   [SQLite](https://www.sqlite.org/index.html) (Banco de dados padrão do Django)

## 🛠️ Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Lucas-Alves-Marques/Django---Catalogo-de-Filmes.git
    cd Django---Catalogo-de-Filmes
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install django
    ```

4.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

6.  **Acesse no seu navegador:**
    [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📁 Estrutura do Projeto

-   `catalogo/`: Configurações principais do projeto Django.
-   `filmes/`: Aplicativo responsável pela lógica do catálogo (models, views, forms, urls).
-   `filmes/static/`: Arquivos de estilo (CSS) e imagens.
-   `filmes/templates/`: Arquivos HTML para renderização das páginas.

## 📝 Autor

Projeto desenvolvido por **Lucas Alves Marques**.
