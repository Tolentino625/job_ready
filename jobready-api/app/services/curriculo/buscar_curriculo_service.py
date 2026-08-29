from app.models.curriculo import Curriculo


class BuscarCurriculoService:
    """Caso de uso: buscar um currículo pelo id."""

    def __init__(self, curriculo_id):
        self.curriculo_id = curriculo_id

    def execute(self):
        curriculo = Curriculo.buscar_por_id(self.curriculo_id)
        if not curriculo:
            raise LookupError("Currículo não encontrado.")
        return curriculo
