from app.models.entrevista import Entrevista


class CriarEntrevistaService:
    """Caso de uso: iniciar uma nova simulação de entrevista."""

    def __init__(self, dados):
        self.dados = dados or {}

    def execute(self):
        if not self.dados.get("usuario_id"):
            raise ValueError("O campo 'usuario_id' é obrigatório.")
        return Entrevista.criar(
            usuario_id=self.dados["usuario_id"],
            tipo=self.dados.get("tipo", "texto"),
            status=self.dados.get("status", "em_andamento"),
            pontuacao_geral=self.dados.get("pontuacao_geral"),
        )
