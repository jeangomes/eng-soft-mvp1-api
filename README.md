# eng-soft-mvp1-api - Gestão de compra de ativos financeiros
API em Python usando Flask para projeto do curso de pós graduação.

Contém funcionalidades para gestão de ativos do mercado financeiro, 
como cadastro e listagem de compras de ações e fundos imobiliários, um gerenciamento básico da carteira de um investidor iniciante.

Por se tratar de um MVP, o projeto atualmente persiste os dados em um banco de dados SQLite.

## Funcionalidades/endpoints:

- [POST] `/operation`

  Adiciona uma nova operação financeira à base de dados.

  - **Entrada**: Tipo de operação, código do ativo, quantidade, cotação e data da operação.

- [GET] `/operations`

  Retorna a listagem de todas as operações registradas.

##### * É possível também deletar e alterar os registros, verifique a documentação completa das rotas.
Após rodar o projeto, acesse: [http://localhost:5000/openapi/swagger](http://localhost:5000/openapi/swagger)

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
