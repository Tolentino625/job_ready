from app.models.feedback import Feedback


class BuscarFeedbackService:
    """Caso de uso: buscar um feedback pelo id."""

    def __init__(self, feedback_id):
        self.feedback_id = feedback_id

    def execute(self):
        feedback = Feedback.buscar_por_id(self.feedback_id)
        if not feedback:
            raise LookupError("Feedback não encontrado.")
        return feedback
