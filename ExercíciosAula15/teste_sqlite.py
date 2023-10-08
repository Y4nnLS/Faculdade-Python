import sqlite3

conn = sqlite3.connect("exemplo.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')

# try:
#     cursor.execute('INSERT INTO usuarios (nome,idade) VALUES (?,?)', ('Arlos Alberto',24))
# except Exception as e:
#     conn.rollback()
#     print('Erro: ', e)
# finally:
#     conn.close()
cursor.execute('INSERT INTO usuarios (nome,idade) VALUES (?,?)', ('Arlos Alberto',24))
cursor.execute('INSERT INTO usuarios (nome,idade) VALUES (?,?)', ('Henrique',69))
cursor.execute('INSERT INTO usuarios (nome,idade) VALUES (?,?)', ('Juliano',96))
cursor.execute('UPDATE usuarios SET idade=? WHERE nome=?',(19,'Juliano'))
cursor.execute('DELETE FROM usuarios WHERE nome=?', ('Henrique',))
# cursor.execute('''DROP TABLE usuarios''')
conn.commit()
conn.close()