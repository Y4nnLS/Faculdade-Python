from flask import Flask, render_template, request

app = Flask(__name__)
lista_nomes = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar')
def listar():
    return render_template('lista.html', names = lista_nomes)

@app.route('/cadastrar')
def cadastrar():
    name = request.args.get('name')
    lista_nomes.append(name)
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)