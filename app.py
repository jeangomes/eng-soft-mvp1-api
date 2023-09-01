from flask import Flask, make_response, request, jsonify

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


@app.route('/add_purchase', methods=['POST'])
def add_purchase():
    # lendo atributos recebidos via formulário
    produto = {}
    # print(request.form['code'])
    produto["code"] = request.form.get("code")
    produto["quantity"] = int(request.form.get("quantity"))
    produto["price"] = float(request.form.get("price"))
    produto["purchase_date"] = request.form.get("purchase_date")
    produto["purchase_amount"] = produto["quantity"] * produto["price"]
    # imprimindo no console
    print("Salvar produto:\n", produto)

    # criando JSON
    resposta_json = jsonify(produto)
    # criando resposta
    response = make_response(resposta_json, 200,)
    response.headers["Content-Type"] = "application/json"

    # retornando resposta
    return response


if __name__ == '__main__':
    app.run()
