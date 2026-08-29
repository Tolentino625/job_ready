from app.services.entrevista.buscar_entrevista_service import BuscarEntrevistaService


class DeletarEntrevistaService:
    """Caso de uso: excluir uma entrevista existente."""

    def __init__(self, entrevista_id):
        self.entrevista_id = entrevista_id

    def execute(self):
        entrevista = BuscarEntrevistaService(self.entrevista_id).execute()
        entrevista.deletar()
