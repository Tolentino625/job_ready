from app.models.pergunta import Pergunta


class CriarPerguntaService:
    """Caso de uso: cadastrar uma nova pergunta no banco de perguntas."""

    def __init__(self, dados):
        self.dados = dados or {}

    def execute(self):
        if not self.dados.get("texto"):
            raise ValueError("O campo 'texto' é obrigatório.")
        return Pergunta.criar(
            texto=self.dados["texto"],
            categoria=self.dados.get("categoria", "comportamental"),
            dificuldade=self.dados.get("dificuldade", "media"),
            sugestao_resposta=self.dados.get("sugestao_resposta"),
        )
