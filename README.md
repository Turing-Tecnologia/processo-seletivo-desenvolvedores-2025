*Indicação de Time*
Gostaria de integrar o time Backend.

*Apresentação*
Meu nome é Isaias Cunha, sou estudante de LCI e tenho interesse na área de desenvolvimento backend. Tenho me dedicado a aprender sobre APIs, banco de dados e já criei algumas aplicações básicas. Gosto de resolver problemas com código.

*Breve resumo sobre o projeto*
No projeto desenvolvido, implementei uma API utilizando Python com Flask e banco de dados MySQL. A API permite o cadastro, listagem, atualização e exclusão de produtos, além de operações básicas de um carrinho de compras, como adicionar produtos, visualizar o carrinho, remover produtos e limpar o carrinho por completo.

## Configurações Necessárias

### Requisitos:

* Python 3.11.9 ou superior
* MySQL 
* Pip (gerenciador de pacotes do Python)

### Instalação das bibliotecas:

```bash
pip install flask mysql-connector-python
```

### Banco de Dados:

1. Crie o banco:

```sql
CREATE DATABASE bd_boladao;
```

2. Crie as tabelas:

```sql
CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    marca VARCHAR(100),
    preco FLOAT(10,2),
    descricao VARCHAR(100)
);

CREATE TABLE produtos_carrinho (
    produto_id INT,
    quantidade INT,
    PRIMARY KEY (produto_id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);
```

3. Configure a conexão com o banco no seu código:

```python
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='sua_senha',
    database='bd_boladao',
)
```

---

## Endpoints da API

### Produtos

#### 1. Listar todos os produtos

**GET /produtos**
Retorna todos os produtos cadastrados.

#### 2. Buscar produto por ID

**GET /produtos/<id>**
Retorna os dados de um produto específico.

#### 3. Criar novo produto

**POST /produtos**
Cria um novo produto.
**Exemplo de JSON:**

```json
{
  "nome": "Arroz",
  "marca": "Tio João",
  "preco": 5.99,
  "descricao": "Arroz branco tipo 1"
}
```

#### 4. Editar produto por ID

PUT /produtos/<id> 
Atualiza os dados de um produto.
**Exemplo de JSON:**

```json
{
  "nome": "Feijão",
  "marca": "Kicaldo",
  "preco": 6.50,
  "descricao": "Feijão preto"
}
```

#### 5. Deletar produto por ID

**DELETE /produtos/<id> **
Remove um produto do banco de dados.

### Carrinho

#### 1. Adicionar produto ao carrinho

**POST /carrinho/addProduto**
Adiciona um produto ao carrinho. Se já existir, a quantidade é somada.
**Exemplo de JSON:**

```json
{
  "produto_id": 1,
  "quantidade": 3
}
```

#### 2. Mostrar carrinho

**GET /carrinho/mostrar**
Retorna todos os produtos adicionados ao carrinho com:

* Id
* Nome
* Marca
* Preço unitário
* Quantidade
* Subtotal por item
* Total geral do carrinho

#### 3. Remover produto do carrinho

**DELETE /carrinho/removerProduto/\<produto\_id>**
Remove um único produto do carrinho.

#### 4. Limpar carrinho

**DELETE /carrinho/limpar**
Remove todos os produtos do carrinho.


