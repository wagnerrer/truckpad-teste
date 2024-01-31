# truckpad-teste
## pre requisitos
**Instalção python versão 3.11** <br>
sudo apt-get install python3.11<br><br>
**Instalação pip**<br>
sudo apt-get install python3-pip<br><br>
**Instalação virtualenv**<br>
pip install virtualenv<br><br>
**Criando virtualenv**<br>
python3 -m venv venv<br><br>

## Instalação Projeto
source venv/bin/activate <br>
pip install -r requirements.txt


## Executando Projeto
**Execcute os comandos abaixo para criar a base de dados e criar <br>
um usuário de teste**<br>
python manage.py makemigrations<br>
python manage.py migrate<br>
python manage.py createsuperuser<br><br>

**Para rodar a aplicação execute o comando abaixo**<br>
python manage.py runserver<br>

**Endpoints de Teste**<br>
para executar os testes coloquei na raiz do projeto um arquivo<br>
truckpad.postman_collection.json para importar no postan<br><br>
Os passos no arquivo de endiponts são os seguintes:<br>
 http://127.0.0.1:8000/api/token/ para autenticar e gerar um token<br>
copie o token gerado e coloque nas apis<br>
http://127.0.0.1:8000/api/crate-author/ <br>
http://127.0.0.1:8000/api/crate-ebook/ <br>
http://127.0.0.1:8000/api/update-ebook/1 1 é o codigo do ebook criado <br>
http://127.0.0.1:8000/api/delete-ebook/1 1 é o codigo do ebook criado <br>
as apis abaixo são de listagem e não necessitam do token<br>
http://127.0.0.1:8000/api/list-author/<br>
http://127.0.0.1:8000/api/list-ebook/






