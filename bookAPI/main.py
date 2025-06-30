from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from flask import request, jsonify



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


# Model
class Funcionario(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    idade: Mapped[str]
    cargo: Mapped[str]

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[int]
    title: Mapped[str]

# Criação da tabela no banco
with app.app_context():
    db.create_all()

# POST
@app.route("/books", methods=["POST"])
def add_book():
    data = request.get_json()
    new_book = Book(
        author=data["author"],
        genre=data["genre"],
        year=data["year"],
        title=data["title"]
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({"message": "Livro adicionado com sucesso!"}), 201

# GET (todos)
@app.route("/books", methods=["GET"])
def get_books():
    books = Book.query.all()
    result = [
        {
            "id": book.id,
            "author": book.author,
            "genre": book.genre,
            "year": book.year,
            "title": book.title
        }
        for book in books
    ]
    return jsonify(result), 200

# GET (individual)
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    result = {
        "id": book.id,
        "author": book.author,
        "genre": book.genre,
        "year": book.year,
        "title": book.title
    }
    return jsonify(result), 200

# PUT (corrigido)
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()

    book.author = data.get("author", book.author)
    book.genre = data.get("genre", book.genre)
    book.year = data.get("year", book.year)
    book.title = data.get("title", book.title)

    db.session.commit()
    return jsonify({"message": "Livro atualizado com sucesso!"}), 200

# DELETE
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Livro deletado com sucesso!"}), 200

"""--------------------------------------------------------------------------"""

@app.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    data = request.get_json()
    funcionario = Funcionario(**data)
    db.session.add(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário criado com sucesso!", "id": funcionario.id}), 201


@app.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    return jsonify([f.to_dict() for f in funcionarios])

@app.route('/funcionarios/<int:funcionario_id>', methods=['GET'])
def obter_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    return jsonify(funcionario.to_dict())

@app.route('/funcionarios/<int:funcionario_id>', methods=['PUT'])
def atualizar_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    data = request.get_json()
    funcionario.nome = data.get('nome', funcionario.nome)
    funcionario.idade = data.get('idade', funcionario.idade)
    funcionario.cargo = data.get('cargo', funcionario.cargo)
    db.session.commit()
    return jsonify({"message": "Funcionário atualizado com sucesso!"})

@app.route('/funcionarios/<int:funcionario_id>', methods=['DELETE'])
def deletar_funcionario(funcionario_id):
    funcionario = Funcionario.query.get_or_404(funcionario_id)
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({"message": "Funcionário deletado com sucesso!"})


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/teste")
def rota_teste():
    return "<p>Rota, teste!</p>"


