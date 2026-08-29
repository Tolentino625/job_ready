from app.models.entrevista import Entrevista


class BuscarEntrevistaService:
    """Caso de uso: buscar uma entrevista pelo id."""

    def __init__(self, entrevista_id):
        self.entrevista_id = entrevista_id

    def execute(self):
        entrevista = Entrevista.buscar_por_id(self.entrevista_id)
        if not entrevista:
            raise LookupError("Entrevista não encontrada.")
        return entrevista
