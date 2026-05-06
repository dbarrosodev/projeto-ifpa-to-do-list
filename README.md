# ✅ TO-DO List — Gerenciador de Tarefas

> Aplicação desktop de gerenciamento de tarefas desenvolvida com **Python** e **Flet**, como atividade acadêmica do **IFPA** (Instituto Federal do Pará).

---

## 📋 Sobre o Projeto

Este projeto é um sistema de **lista de tarefas (To-Do List)** com autenticação de usuários, desenvolvido como atividade prática para a disciplina do IFPA. A aplicação permite que o usuário se cadastre, faça login e gerencie suas tarefas de forma simples e intuitiva.

### Funcionalidades

- 🔐 **Cadastro de usuário** — registro com nome, e-mail e senha
- 🔑 **Login** — autenticação por e-mail e senha
- ➕ **Adicionar tarefas** — criação de tarefas com título e descrição
- 📄 **Listar tarefas** — visualização de todas as tarefas cadastradas
- 🗂️ **Navegação por abas** — interface organizada com abas (Adicionar, Tarefas, Perfil)

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|---|---|
| [Python](https://www.python.org/) | Linguagem de programação principal |
| [Flet](https://flet.dev/) | Framework para construção da interface gráfica |
| [SQLAlchemy](https://www.sqlalchemy.org/) | ORM para manipulação do banco de dados |
| [SQLite](https://www.sqlite.org/) | Banco de dados relacional local |

---

## 📁 Estrutura do Projeto

```
TO-DO-List-no-Flet-main/
├── src/
│   ├── main.py                  # Ponto de entrada da aplicação
│   ├── database.db              # Banco de dados SQLite
│   ├── database/
│   │   ├── connection.py        # Configuração da conexão com o banco
│   │   └── init_db.py           # Inicialização e criação das tabelas
│   ├── models/
│   │   ├── base.py              # Base declarativa do SQLAlchemy
│   │   ├── user_model.py        # Modelo do usuário
│   │   └── task_model.py        # Modelo da tarefa
│   └── views/
│       ├── login_view.py        # Tela de login
│       ├── register_view.py     # Tela de cadastro
│       └── home_view.py         # Tela principal com abas
└── README.md
```

---

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.8+** instalado — [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/dbarrosodev/projeto-ifpa-to-do-list.git
   cd projeto-ifpa-to-do-list
   ```

2. **Instale as dependências:**

   ```bash
   pip install flet sqlalchemy
   ```

3. **Execute a aplicação:**

   ```bash
   cd src
   python main.py
   ```

A aplicação será aberta em uma janela desktop com dimensões de **480×854** pixels.

---

## 🖥️ Telas da Aplicação

| Tela | Descrição |
|---|---|
| **Login** | Tela inicial com campos de e-mail e senha para autenticação |
| **Cadastro** | Formulário de registro com nome, e-mail, senha e confirmação |
| **Home** | Tela principal com navegação por abas: Adicionar, Tarefas e Perfil |

---

## 🏗️ Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)** simplificado:

- **Models** → Definem a estrutura das tabelas do banco de dados (Usuário e Tarefa)
- **Views** → Responsáveis pela interface gráfica e interação com o usuário
- **Database** → Gerencia a conexão e inicialização do banco SQLite via SQLAlchemy

---

## 👤 Autor

Desenvolvido por **Daniel Barroso** — [@dbarrosodev](https://github.com/dbarrosodev)

📚 Atividade acadêmica — **IFPA** (Instituto Federal do Pará)

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.