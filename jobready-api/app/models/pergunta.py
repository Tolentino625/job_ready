from app.extensions import db


class Pergunta(db.Model):
    """Model da entidade Pergunta (banco de perguntas frequentes de entrevista)."""

    __tablename__ = "perguntas"

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(80), nullable=False, default="comportamental")
    dificuldade = db.Column(db.String(20), nullable=False, default="media")
    sugestao_resposta = db.Column(db.Text, nullable=True)

    # ---------- CRUD ----------
    @classmethod
    def criar(cls, texto, categoria="comportamental", dificuldade="media", sugestao_resposta=None):
        pergunta = cls(
            texto=texto,
            categoria=categoria,
            dificuldade=dificuldade,
            sugestao_resposta=sugestao_resposta,
        )
        db.session.add(pergunta)
        db.session.commit()
        return pergunta

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.id).all()

    @classmethod
    def buscar_por_id(cls, pergunta_id):
        return cls.query.get(pergunta_id)

    def atualizar(self, texto=None, categoria=None, dificuldade=None, sugestao_resposta=None):
        if texto is not None:
            self.texto = texto
        if categoria is not None:
            self.categoria = categoria
        if dificuldade is not None:
            self.dificuldade = dificuldade
        if sugestao_resposta is not None:
            self.sugestao_resposta = sugestao_resposta
        db.session.commit()
        return self

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "texto": self.texto,
            "categoria": self.categoria,
            "dificuldade": self.dificuldade,
            "sugestao_resposta": self.sugestao_resposta,
        }
