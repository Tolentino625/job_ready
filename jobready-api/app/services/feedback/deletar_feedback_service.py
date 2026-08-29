from app.services.feedback.buscar_feedback_service import BuscarFeedbackService


class DeletarFeedbackService:
    """Caso de uso: excluir um feedback existente."""

    def __init__(self, feedback_id):
        self.feedback_id = feedback_id

    def execute(self):
        feedback = BuscarFeedbackService(self.feedback_id).execute()
        feedback.deletar()
