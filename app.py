from flask import Flask, make_response, request, jsonify

from model import Session, Operation

app = Flask(__name__)


@app.route('/')
def home():
    html = """<!DOCTYPE html>
    <html>
        <body>
        <h1>Home temp</h1>
        <p> Documentação em produção!! </p>
        </body>
    </html>"""
    return make_response(html), 200


@app.route('/add_operation', methods=['POST'])
def add_operation():
    """Adiciona uma nova Operação Financeira à base de dados

    Retorna uma representação dos produtos e comentários associados.
    """
    # lendo atributos recebidos da requisição
    operation = Operation(
        operation_type=request.form.get("operation_type"),
        code=request.form.get("code"),
        quantity=int(request.form.get("quantity")),
        price=float(request.form.get("price")),
        operation_date=request.form.get("operation_date"),
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
