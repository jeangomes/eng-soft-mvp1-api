# eng-soft-mvp1-api
API em Python usando Flask para projeto do curso de pós graduação.

Contém funcionalidades para cadastrar compras de ativos do mercado financeiro, 
como ações e fundos imobiliários, um gerenciamento básico da carteira de um investidor iniciante.


## Como executar o código


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> O projeto usa o ambiente virtual [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

O comando acima é necessário para instalar as dependências/bibliotecas, listadas no arquivo `requirements.txt`.

Para rodar o projeto execute no terminal:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.
