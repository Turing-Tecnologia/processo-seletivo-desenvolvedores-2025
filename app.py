from flask import Flask, jsonify, request
import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='senha',  
    database='bd_boladao',
)

cursor = conexao.cursor()

app = Flask(__name__)

# =========== PRODUTO ==============

# Mostrar todos os Produtos
@app.route('/produtos', methods=['GET'])
def listar_pro():
    cursor.execute("SELECT * FROM produtos")  
    produtos = cursor.fetchall()  
    
    # Cria a lista de produtos com base nO bd
    produtos_list = []
    for produto in produtos:
        produto_dict = {
            'id': produto[0], 
            'nome': produto[1],  
            'marca': produto[2], 
            'preco': produto[3],  
            'descricao': produto[4],  
        }
        produtos_list.append(produto_dict)
    
    return jsonify(produtos_list)

# Mostrar Produto por ID
@app.route('/produtos/<int:id>', methods=['GET'])
def buscar_pro_por_id(id):
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (id,)) 
    produto = cursor.fetchone()  # Pega o produto encontrado
    
    if produto:
        produto_dict = {
            'id': produto[0],
            'nome': produto[1],
            'marca': produto[2],
            'preco': produto[3],
            'descricao': produto[4],
        }
        return jsonify(produto_dict)
    else:
        return jsonify({'message': 'Produto não encontrado'})

# Criar novo produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    nome = dados.get('nome')
    marca = dados.get('marca')
    preco = dados.get('preco')
    descricao = dados.get('descricao')

    cursor.execute(
        "INSERT INTO produtos (nome, marca, preco, descricao) VALUES (%s, %s, %s, %s)",
        (nome, marca, preco, descricao)
    )
    conexao.commit()

    return jsonify({'message': 'Produto criado com sucesso'}) 

#Editar o produto
@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto_id(id):
    dados = request.get_json()
    nome = dados.get('nome')
    marca = dados.get('marca')
    preco = dados.get('preco')
    descricao = dados.get('descricao')

    cursor.execute(
        "UPDATE produtos SET nome = %s, marca = %s, preco = %s, descricao = %s WHERE id = %s",
        (nome, marca, preco, descricao, id)
    )
    conexao.commit()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Produto não encontrado'}), 
    return jsonify({'message': 'Produto atualizado com sucesso'})

#Deletar produto 
@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto_id(id):
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conexao.commit()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Produto não encontrado'}) 
    return jsonify({'message': 'Produto deletado com sucesso'})

#===================================

#============ CARRINHO =============

@app.route('/carrinho/addProduto', methods=['POST'])
def adicionar_produto_no_carrinho():
    dados = request.get_json()  # Pega os dados enviados no corpo da requisição
    produto_id = dados.get('produto_id')
    quantidade = dados.get('quantidade')

    if not produto_id or not quantidade or quantidade <= 0:
        return jsonify({'message': 'Dados inválidos. Certifique-se de enviar produto_id e quantidade.'}) 

    # Verifica se o produto existe no banco
    cursor.execute("SELECT * FROM produtos WHERE id = %s", (produto_id,))
    produto = cursor.fetchone()

    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 

    # Adiciona o produto no carrinho
    cursor.execute("""
        INSERT INTO produtos_carrinho (produto_id, quantidade)
        VALUES (%s, %s)
        ON DUPLICATE KEY UPDATE quantidade = quantidade + %s
    """, (produto_id, quantidade, quantidade)) # Se o produto for duplicado soma a que ja tem 
    conexao.commit()

    return jsonify({'message': f'Produto {produto[1]} adicionado ao carrinho com {quantidade} unidades'}) 

# Mostrar o Carrinho
@app.route('/carrinho/mostrar', methods=['GET'])
def mostrar_carrinho():
    cursor.execute("""
        SELECT 
            p.id,
            p.nome,
            p.marca,
            p.preco,
            pc.quantidade,
            (p.preco * pc.quantidade) AS subtotal
        FROM produtos_carrinho pc
        JOIN produtos p ON pc.produto_id = p.id
    """)
    
    itens = cursor.fetchall()

    carrinho = []
    total_geral = 0

    for item in itens:
        produto = {
            'id': item[0],
            'nome': item[1],
            'marca': item[2],
            'preco_unitario': item[3],
            'quantidade': item[4],
            'subtotal': item[5]
        }
        total_geral += item[5]
        carrinho.append(produto)

    return jsonify({
        'itens': carrinho,
        'total': total_geral
    })

# Limpar Carrinho 
@app.route('/carrinho/limpar', methods=['DELETE'])
def limpar_carrinho():
    cursor.execute("DELETE FROM produtos_carrinho")
    conexao.commit()
    return jsonify({'message': 'Carrinho esvaziado com sucesso'})

@app.route('/carrinho/removerProduto/<int:produto_id>', methods=['DELETE'])
def remover_produto(produto_id):
    cursor.execute("DELETE FROM produtos_carrinho WHERE produto_id = %s", (produto_id,))
    conexao.commit()

    if cursor.rowcount == 0:
        return jsonify({'message': 'Produto não encontrado no carrinho'}), 
    return jsonify({'message': f'Produto {produto_id} removido do carrinho'})

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
