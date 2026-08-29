from app.models.resposta import Resposta


class BuscarRespostaService:
    """Caso de uso: buscar uma resposta pelo id."""

    def __init__(self, resposta_id):
        self.resposta_id = resposta_id

    def execute(self):
        resposta = Resposta.buscar_por_id(self.resposta_id)
        if not resposta:
            raise LookupError("Resposta não encontrada.")
        return resposta
