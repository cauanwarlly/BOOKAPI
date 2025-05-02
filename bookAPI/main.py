from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

#crie o aplicativo
app = Flask(__name__)
# configurar o banco de dados SQLite, em relação à pasta da instância do aplicativo
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# inicializar o aplicativo com a extensão
db.init_app(app)

# Model -
class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str]
    genre: Mapped[str]
    year: Mapped[str]
    title: Mapped[str]


# Criasao das tabelas no banco
with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return "<p>bom dia familha</p>"

@app.route("/teste")
def rota_teste():
    return "<p>bom dia pedro</p>"

