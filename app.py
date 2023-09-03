from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag

from model import Session, Operation
from schemas import OperationViewSchema, OperationSchema, ErrorSchema
from schemas.operation import show_operation

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)

# app = Flask(__name__)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
operation_tag = Tag(name="Operação", description="Adição, visualização e remoção de operações financeiras à base")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


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


if __name__ == '__main__':
    app.run()
