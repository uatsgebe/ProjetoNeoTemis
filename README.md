# NeoTêmis

Sistema web jurídico desenvolvido com Flask, com autenticação de usuários, cadastro, login, recuperação de senha, controle de sessão, permissões por tipo de usuário e estrutura modular.

## Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- python-dotenv
- SQLite
- HTML
- CSS
- JavaScript

## Como rodar o projeto em outro computador

Clonar o repositório

```bash
git clone https://github.com/uatsgebe/ProjetoNeoTemis.git

Após baixar ou clonar o projeto pelo GitHub, siga os passos abaixo para configurar corretamente o ambiente e executar o sistema.

1. Abrir a pasta do projeto no VS Code

Abra a pasta do projeto normalmente pelo VS Code.

2. Criar o ambiente virtual

No terminal do VS Code, execute:

```bash
python -m venv venv

3. Ativar o ambiente virtual

venv\Scripts\activate

Se funcionar corretamente, no início da linha do terminal aparecerá algo parecido com:

(venv)

4. Instalar as dependências necessárias
Execute os comandos abaixo no terminal:

pip install flask
pip install flask_sqlalchemy
pip install flask_login
pip install flask_migrate
pip install python-dotenv

5. Executar o sistema
Depois de instalar tudo, execute:

python app.py

6. Abrir o sistema no navegador
Após rodar o comando acima, o terminal mostrará um endereço parecido com:

http://127.0.0.1:5000

Abra esse endereço no navegador para acessar o sistema.

################

Observações importantes
O projeto utiliza Flask, então NÃO deve ser aberto com Live Server.
O sistema sempre deve ser executado pelo app.py.
O banco SQLite é criado automaticamente dentro da pasta instance/.
Caso o banco apresente erro por falta de colunas após atualizações do projeto, apague o arquivo:

instance/banco.db

e para recriar o banco atualizado, execute novamente:

python app.py