from app.services.feedback.buscar_feedback_service import BuscarFeedbackService


class AtualizarFeedbackService:
    """Caso de uso: atualizar os dados de um feedback existente."""

    def __init__(self, feedback_id, dados):
        self.feedback_id = feedback_id
        self.dados = dados or {}

    def execute(self):
        feedback = BuscarFeedbackService(self.feedback_id).execute()
        return feedback.atualizar(
            pontuacao=self.dados.get("pontuacao"),
            comentario=self.dados.get("comentario"),
            ponto_forte=self.dados.get("ponto_forte"),
            ponto_a_melhorar=self.dados.get("ponto_a_melhorar"),
        )
