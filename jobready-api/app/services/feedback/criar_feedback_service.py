from app.models.feedback import Feedback


class CriarFeedbackService:
    """Caso de uso: registrar o feedback de desempenho de uma entrevista."""

    def __init__(self, dados):
        self.dados = dados or {}

    def execute(self):
        if not self.dados.get("entrevista_id") or self.dados.get("pontuacao") is None:
            raise ValueError("Campos 'entrevista_id' e 'pontuacao' são obrigatórios.")
        return Feedback.criar(
            entrevista_id=self.dados["entrevista_id"],
            pontuacao=self.dados["pontuacao"],
            comentario=self.dados.get("comentario"),
            ponto_forte=self.dados.get("ponto_forte"),
            ponto_a_melhorar=self.dados.get("ponto_a_melhorar"),
        )
