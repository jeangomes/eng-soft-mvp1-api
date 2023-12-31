from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from sqlalchemy.sql import text
from sqlalchemy import func

from model import Session, Operation
from model.operation import format_date
from schemas import OperationViewSchema, OperationSchema, ErrorSchema
from schemas.operation import show_operation, ListOperationsSchema, show_operations, OperationDelSchema, \
    OperationBuscaSchema

info = Info(title="Minha API - EngSoft MVP1", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Documentação em Swagger")
operation_tag = Tag(name="Operação", description="Adição, visualização, alteração e remoção de operações financeiras")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para a documentação em Swagger.
    """
    return redirect('/openapi/swagger')


@app.post('/operation', tags=[operation_tag],
          responses={"200": OperationViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_operation(form: OperationSchema):
    """Adiciona uma nova Operação Financeira à base de dados

    Retorna uma representação da operação.
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
        return show_operation(operation)

    except Exception as e:
        print(e)
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        return {"message": error_msg}, 400


@app.get('/operations', tags=[operation_tag],
         responses={"200": ListOperationsSchema, "404": ErrorSchema})
def get_operations(query: OperationBuscaSchema):
    """Faz a busca por todas as operações cadastrados, permitindo filtrar pelo código de negociação.

    Retorna uma representação da listagem de operações.
    """
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    if query.code:
        operations = (session.query(Operation)
                      .where(func.upper(Operation.code) == query.code.upper())
                      .order_by(text("operation_date desc"))
                      .all())
    else:
        operations = session.query(Operation).order_by(text("operation_date desc")).all()

    if not operations:
        # se não há registros cadastrados
        return {"operations": []}, 200
    else:
        # retorna a representação de uma operação
        # print(operations)
        return show_operations(operations), 200


# Endpoint for deleting an operation
@app.delete('/operation', tags=[operation_tag],
            responses={"200": OperationDelSchema, "404": ErrorSchema})
def del_operation(query: OperationBuscaSchema):
    """Deleta uma operação financeira a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    operation_id = query.operation_id
    session = Session()
    # fazendo a exclusão
    count = session.query(Operation).filter(Operation.id == operation_id).delete()
    session.commit()

    if count:
        return {"message": "Operação financeira removida", "id": operation_id}
    else:
        error_msg = "Operação não encontrada na base :/"
        return {"message": error_msg}, 404


@app.get('/operation', tags=[operation_tag],
         responses={"200": OperationViewSchema, "404": ErrorSchema})
def get_operation(query: OperationBuscaSchema):
    """Faz a busca por uma operação a partir do id do registro

    Retorna uma representação da operação financeira.
    """
    operation_id = query.operation_id
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    operation = session.query(Operation).filter(Operation.id == operation_id).first()

    if not operation:
        error_msg = "Registro não encontrado na base :/"
        return {"message": error_msg}, 404
    else:
        return show_operation(operation), 200


# Endpoint for updating a finance operation
@app.put('/operation/<int:operation_id>', tags=[operation_tag])
def operation_update(path: OperationBuscaSchema, body: OperationSchema):
    """Faz o update de um registro selecionado pelo id

    Retorna uma representação da operação financeira atualizada.
    """
    session = Session()
    operation = session.query(Operation).filter(Operation.id == path.operation_id).first()
    if operation:
        operation.operation_type = body.operation_type
        operation.code = body.code
        operation.quantity = int(body.quantity)
        operation.price = float(body.price)
        operation.operation_date = format_date(body.operation_date)
        operation.operation_amount = operation.quantity * operation.price
        session.commit()
        return show_operation(operation), 200
    else:
        return {"message": "Registro não encontrado para esse id"}, 404


if __name__ == '__main__':
    app.run()
