from datetime import datetime
from app.extensions import db


class Lembrete(db.Model):
    """Lembrete de estudo e preparação."""

    __tablename__ = "lembretes"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    data = db.Column(db.Date, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def criar(cls, titulo, descricao, data):
        lembrete = cls(titulo=titulo, descricao=descricao, data=data)
        db.session.add(lembrete)
        db.session.commit()
        return lembrete

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.data.asc(), cls.id.asc()).all()

    @classmethod
    def buscar_por_id(cls, lembrete_id):
        return cls.query.get(lembrete_id)

    def atualizar(self, titulo=None, descricao=None, data=None):
        if titulo is not None:
            self.titulo = titulo
        if descricao is not None:
            self.descricao = descricao
        if data is not None:
            self.data = data
        db.session.commit()
        return self

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "data": self.data.isoformat() if self.data else None,
            "criado_em": self.criado_em.isoformat() if self.criado_em else None,
        }
