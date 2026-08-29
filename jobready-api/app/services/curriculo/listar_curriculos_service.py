from app.models.curriculo import Curriculo


class ListarCurriculosService:
    """Caso de uso: listar todos os currículos cadastrados."""

    def execute(self):
        return Curriculo.listar()
