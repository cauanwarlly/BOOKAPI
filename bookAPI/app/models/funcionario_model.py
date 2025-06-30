from app import db
from sqlalchemy.orm import Mapped, mapped_column

class Funcionario(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    idade: Mapped[str]
    cargo: Mapped[str]

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "cargo": self.cargo
        }