from app.services.pergunta.buscar_pergunta_service import BuscarPerguntaService


class AtualizarPerguntaService:
    """Caso de uso: atualizar os dados de uma pergunta existente."""

    def __init__(self, pergunta_id, dados):
        self.pergunta_id = pergunta_id
        self.dados = dados or {}

    def execute(self):
        pergunta = BuscarPerguntaService(self.pergunta_id).execute()
        return pergunta.atualizar(
            texto=self.dados.get("texto"),
            categoria=self.dados.get("categoria"),
            dificuldade=self.dados.get("dificuldade"),
            sugestao_resposta=self.dados.get("sugestao_resposta"),
        )
