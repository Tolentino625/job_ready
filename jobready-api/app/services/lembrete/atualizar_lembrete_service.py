from datetime import date
from app.services.lembrete.buscar_lembrete_service import BuscarLembreteService


class AtualizarLembreteService:
    def __init__(self, lembrete_id, dados):
        self.lembrete_id = lembrete_id
        self.dados = dados or {}

    def execute(self):
        lembrete = BuscarLembreteService(self.lembrete_id).execute()

        titulo = self.dados.get("titulo")
        if titulo is not None:
            titulo = str(titulo).strip()
            if not titulo:
                raise ValueError("O título não pode ficar vazio.")

        data_raw = self.dados.get("data")
        data = None
        if data_raw is not None:
            try:
                data = date.fromisoformat(str(data_raw))
            except (TypeError, ValueError):
                raise ValueError("A data informada é inválida.")

        return lembrete.atualizar(
            titulo=titulo,
            descricao=self.dados.get("descricao"),
            data=data,
        )
