from app.models.resposta import Resposta


class CriarRespostaService:
    """Caso de uso: registrar a resposta de um usuário a uma pergunta."""

    def __init__(self, dados):
        self.dados = dados or {}

    def execute(self):
        obrigatorios = ("entrevista_id", "pergunta_id", "texto_resposta")
        if not all(self.dados.get(campo) for campo in obrigatorios):
            raise ValueError(
                "Campos 'entrevista_id', 'pergunta_id' e 'texto_resposta' são obrigatórios."
            )
        return Resposta.criar(
            entrevista_id=self.dados["entrevista_id"],
            pergunta_id=self.dados["pergunta_id"],
            texto_resposta=self.dados["texto_resposta"],
            tipo=self.dados.get("tipo", "texto"),
        )
