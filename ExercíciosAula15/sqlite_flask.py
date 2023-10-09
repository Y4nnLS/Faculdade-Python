from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect('exemplo.db')

@app.route('/')
def index():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)

@app.route('/inserir', methods=['POST'])
def insert():
    nome = request.form['nome']
    idade = request.form['idade']
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome,idade) VALUES(?,?)', (nome, idade))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def delet(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id=?', (id,))
    usuario = cursor.fetchone()
    conn.close()
    return render_template('editar.html', usuario=usuario)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    idade = request.form['idade']
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET idade=? WHERE id=?', (idade, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
