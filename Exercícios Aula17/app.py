from flask import Flask, jsonify, request

contatos = []
contatos.append({'nome' : 'Joao', 'idade' : 22})
contatos.append({'nome' : 'Maria', 'idade' : 19})
contatos.append({'nome' : 'Cu', 'idade' : 69})



app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello!'

@app.route('/contatos', methods=['GET'])
def get_contatos():
    return jsonify( {'contatos' : contatos} )

@app.route('/contatos/<int:id>', methods=['GET'])
def get_contato(id):
    if 0 <= id < len(contatos):
        return jsonify( {'contato': contatos[id]} )
    else:
        return jsonify( {'error' : 'Contato não encontrado'}, 404 )

@app.route('/contatos', methods=['POST'])
def add_contatos():
    new_contato = request.json
    contatos.append(new_contato)
    return jsonify( {'message' : 'Contato adicionado!'} )

@app.route('/contatos/<int:id>', methods=['DELETE'])
def delete__contatos(id):
    contatos.pop(id)
    if 0 <= id < len(contatos):
        return jsonify( {'message': 'Contato removido!'} )
    else:
        return jsonify( {'error' : 'Contato não encontrado'}, 404 )

@app.route('/contatos/<int:id>', methods=['PUT'])
def update__contatos(id):
    if 0 <= id < len(contatos):
        update_contato = request.json
        contatos[id] = update_contato
        return jsonify( {'message': 'Contato atualizado!'} )
    else:
        return jsonify( {'error' : 'Contato não encontrado'}, 404 )

if __name__ == '__main__':
    app.run(debug=True)