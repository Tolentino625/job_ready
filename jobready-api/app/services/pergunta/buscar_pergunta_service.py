from app.models.pergunta import Pergunta


class BuscarPerguntaService:
    """Caso de uso: buscar uma pergunta pelo id."""

    def __init__(self, pergunta_id):
        self.pergunta_id = pergunta_id

    def execute(self):
        pergunta = Pergunta.buscar_por_id(self.pergunta_id)
        if not pergunta:
            raise LookupError("Pergunta não encontrada.")
        return pergunta
