from app.models.lembrete import Lembrete


class BuscarLembreteService:
    def __init__(self, lembrete_id):
        self.lembrete_id = lembrete_id

    def execute(self):
        lembrete = Lembrete.buscar_por_id(self.lembrete_id)
        if not lembrete:
            raise LookupError("Lembrete não encontrado.")
        return lembrete
