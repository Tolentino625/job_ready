from app.models.pergunta import Pergunta


class ListarPerguntasService:
    """Caso de uso: listar todas as perguntas cadastradas."""

    def execute(self):
        return Pergunta.listar()
