# 🔒 Armazenador de Senhas

## 📌 Sobre o Projeto
Este é um **Gerenciador de Senhas** simples desenvolvido em **Python**, com uma interface gráfica feita em **Tkinter** e armazenamento seguro utilizando **criptografia**. O objetivo é permitir que o usuário armazene, visualize e gerencie suas senhas de forma segura, utilizando uma **senha mestre** para acesso.

## 🚀 Funcionalidades
- 🏷 **Tela de Login**: Protegida por uma senha mestre.
- 🔑 **Cadastro de Senhas**: Armazena e criptografa credenciais.
- 📂 **Visualização de Senhas**: Exibe as senhas apenas após autenticação.
- 🗑 **Exclusão de Senhas**: Remove credenciais salvas.

## 🛠 Tecnologias Utilizadas
- 🐍 **Python 3.x**
- 🖥 **Tkinter** (Interface gráfica)
- 🔐 **Cryptography** (Para criptografar senhas)
- 📂 **SQLite ou JSON** (Para armazenar os dados)

## 📂 Estrutura do Projeto
```
📂 ArmazenadorSenhas
├── main.py               # Arquivo principal que inicia o programa
├── tela_login.py         # Tela de login e autenticação
├── tela_principal.py     # Interface para gerenciar senhas
├── gerenciador_senhas.py # Lógica de armazenamento e criptografia
└── README.md             # Documentação do projeto
```

## 📦 Instalação e Uso
1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-de-senhas.git
   cd gerenciador-de-senhas
   ```

2. **Instale as dependências**:
   ```bash
   pip install cryptography
   ```

3. **Execute o projeto**:
   ```bash
   python main.py
   ```

## 🛡 Segurança
- As senhas são armazenadas de forma **criptografada** para garantir segurança.
- A senha mestre deve ser mantida segura, pois será usada para descriptografar os dados.

## 📄 Licença
Este projeto é de código aberto sob a licença **MIT**. Sinta-se livre para usá-lo e modificá-lo! 🛠

---
👩‍💻 **Desenvolvido por Joca** 🚀

