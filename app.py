from flask import Flask, make_response, request, jsonify, redirect
from flask_openapi3 import OpenAPI, Info, Tag

from model import Session, Operation
from schemas import OperationViewSchema, OperationSchema, ErrorSchema

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# app = Flask(__name__)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/operation', tags=[produto_tag],
          responses={"200": OperationViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_operation(form: OperationSchema):
    """Adiciona uma nova Operação Financeira à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    # lendo atributos recebidos da requisição
    operation = Operation(
        operation_type=form.operation_type,
        code=form.code,
        quantity=int(form.quantity),
        price=float(form.price),
        operation_date=form.operation_date,
    )
    operation.operation_amount = operation.quantity * operation.price
    try:
        # criando conexão com a base
        session = Session()
        # adicionando operation
        session.add(operation)
        # efetivando o comando de adição de novo registro na tabela
        session.commit()

        # criando JSON
        operation_dict = {
            "operation_type": operation.operation_type,
            "code": operation.code,
            "quantity": operation.quantity
        }
        resposta_json = jsonify(operation_dict)
        # criando resposta
        response = make_response(resposta_json, 200)

        # imprimindo no console
        print("Operation saved:\n", operation_dict)

    except Exception as e:
        print(e)
        # caso um erro fora do previsto
        error = {"msg": "Não foi possível salvar a operação :/"}
        # criando JSON
        resposta_json = jsonify(error)
        # criando resposta
        response = make_response(resposta_json, 400)

    # retornando resposta
    response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    app.run()
