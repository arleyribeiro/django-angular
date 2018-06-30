# django-angular

#### Django
O Django é um framework do Python, sendo assim baixado pelo próprio gerenciador de pacotes da linguagem, o Pip. Portanto, será necessário inicialmente instalar (ou atualizar, pois muitos sistema Unix possuem nativamente o Python) a linguagem Python. Para isso, execute:
```
$ sudo apt-get install python3
```
A versão do Python é opcional, porém foi escolhida a versão 3 pois é a mais recente. Após a instalação do Python, é necessário instalar o gerenciador de pacotes:
```
$ sudo apt-get install python3-pip
```
Após a instalação do gerenciador, para que não haja conflito entre pacotes de python utilizados pelo Sistema Operacional e os pacotes utilizados, é necessário criar um ambiente virtual python. Esse ambiente funciona como um diretório a parte onde se pode instalar pacotes relacionados à linguagem sem que se altere os pacotes pré-existentes. A instalação do programa que cria ambiente é feita da seguinte forma:
```
$ sudo pip install virtualenv
```
Para criar um novo ambiente virtual, basta executar o comando:
```
$ cd ~
$ virtualenv -p python3 envPython3
```
Onde `envPython3` é o nome do ambiente virtual a ser criado, e o parâmetro `-p` específica a versão do Python a ser utilizada.

#### Ativando o ambiente virtual
Para ativar o ambiente (deve ser feito sempre que se deseja executar a aplicação), deve-se executar o arquivo `activate` da seguinte forma, dentro da pasta do ambiente virtual.
```
$ source bin/activate
```

#### Desativando o ambiente virtual
```
$ desactivate
```

### Dependências

### Instalando dependências
Dentro da pasta do projeto que contém o arquivo com as dependências, execute:
```
$ pip install -r requirements.txt
```

### Criando um arquivo de dependências
Para facilitar a instalação, criamos um arquivo com as dependências do projeto, para atualiza-lo, basta executar o comando;
```
$ pip freeze > requirements.txt
```

## Execução
Após ativar o ambiente virtual execute o arquivo `manage.py` com o seguinte comando: Esse comando cria o banco de dados
```
$ python manage.py migrate
```
Execute o servidor do aplicação django
```
$ python manage.py runserver
```
Para executar o servidor do angular, entre na pasta frontend e execute o seguinte comando:
```
$ ng serve 
```
Após isso, é possível acessar o aplicativo no endereço `localhost:4200`.

###Referências
[Separando o Frontend do Backend com Angular e Django](https://humberto.io/blog/separando-o-frontend-do-backend-com-angular-e-django/)
