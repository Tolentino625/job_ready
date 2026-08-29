from app.services.pergunta.buscar_pergunta_service import BuscarPerguntaService


class DeletarPerguntaService:
    """Caso de uso: excluir uma pergunta existente."""

    def __init__(self, pergunta_id):
        self.pergunta_id = pergunta_id

    def execute(self):
        pergunta = BuscarPerguntaService(self.pergunta_id).execute()
        pergunta.deletar()
