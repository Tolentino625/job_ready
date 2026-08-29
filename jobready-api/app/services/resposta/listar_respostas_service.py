from app.models.resposta import Resposta


class ListarRespostasService:
    """Caso de uso: listar todas as respostas registradas."""

    def execute(self):
        return Resposta.listar()
