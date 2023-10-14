from flask import Flask, request, jsonify
import cx_Oracle

app = Flask(__name)

connection = cx_Oracle.connect(RM550620,130400,oracle.fiap.com.br:1521/orcl)

@app.route('/recurso', methods=['POST'])
def criar_recurso():
    data = request.get_json()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO livros_checkpoint (livro_id, nome_livro, float_preco, data_lancamento) VALUES (:livro_id, :nome_livro, :float_preco, TO_DATE(:data_lancamento, 'DD-MM-YYYY'))", data)
    cursor.close()
    connection.commit()
    return jsonify({"message": "Recurso criado com sucesso"})

@app.route('/recurso/<int:id>', methods=['GET'])
def ler_recurso_por_id(id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tabela WHERE id = :id", {"id": id})
    result = cursor.fetchone()
    cursor.close()
    if result:
        recursos.append({"livro_id": result[0], "nome_livro": result[1], "float_preco": result[2],"float_preco": result[3], "data_lancamento": result[4].strftime('%d-%m-%Y')})
    else:
        return jsonify({"message": "Recurso não encontrado"}, 404)

@app.route('/recursos', methods=['GET'])
def listar_recursos():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM livros_checkpoint")
    results = cursor.fetchall()
    cursor.close()
    recursos = []
    for result in results:
        recursos.append({"livro_id": result[0], "nome_livro": result[1], "float_preco": result[2],"float_preco": result[3], "data_lancamento": result[4].strftime('%d-%m-%Y')})
    return jsonify(recursos)

if __name__ == '__main__':
    app.run(debug=True)
