from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'exemplo.db')
db = SQLAlchemy(app)

print(base_dir)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    idade = db.Column(db.Integer)  # Make sure this line is present

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'{self.nome} ({self.idade} anos)'



@app.route('/')
def index():
    db.create_all()
    contatos = Contato.query.all()
    return render_template('index.html', contatos = contatos)


@app.route('/inserir', methods=['POST'])
def insert():
    nome = request.form['nome']
    idade = request.form['idade']
    contato = Contato(nome, idade)
    db.session.add(contato)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def delete(id):
    contato = Contato.query.get(id)
    db.session.delete(contato)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/atualizar/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method == 'POST':
        nova_idade = request.form['nova_idade']
        contato  = Contato.query.get(id)
        contato.idade = nova_idade
        db.session.commit()
        return redirect(url_for('index'))
    else:
        contato = Contato.query.get(id)
        return render_template('atualiza.html', contato = contato)

@app.route('/listar', methods=['POST'])
def list():
    nome = request.form['nome']
    contatos = Contato.query.filter(Contato.nome.like(f'%{nome}%')).all()
    return render_template("lista.html", contato = contatos)

if __name__ == '__main__':
    app.run(debug = True)