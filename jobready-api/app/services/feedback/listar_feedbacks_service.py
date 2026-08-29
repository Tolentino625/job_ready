from app.models.feedback import Feedback


class ListarFeedbacksService:
    """Caso de uso: listar todos os feedbacks registrados."""

    def execute(self):
        return Feedback.listar()
