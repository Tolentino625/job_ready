from app.models.entrevista import Entrevista


class ListarEntrevistasService:
    """Caso de uso: listar todas as entrevistas realizadas."""

    def execute(self):
        return Entrevista.listar()
