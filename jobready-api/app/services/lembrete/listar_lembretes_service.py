from app.models.lembrete import Lembrete


class ListarLembretesService:
    def execute(self):
        return Lembrete.listar()
