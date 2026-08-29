from app.services.entrevista.buscar_entrevista_service import BuscarEntrevistaService


class AtualizarEntrevistaService:
    """Caso de uso: atualizar os dados de uma entrevista existente."""

    def __init__(self, entrevista_id, dados):
        self.entrevista_id = entrevista_id
        self.dados = dados or {}

    def execute(self):
        entrevista = BuscarEntrevistaService(self.entrevista_id).execute()
        return entrevista.atualizar(
            tipo=self.dados.get("tipo"),
            status=self.dados.get("status"),
            pontuacao_geral=self.dados.get("pontuacao_geral"),
        )
