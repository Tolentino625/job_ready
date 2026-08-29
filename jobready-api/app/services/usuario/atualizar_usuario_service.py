from app.models.usuario import Usuario
from app.services.usuario.buscar_usuario_service import BuscarUsuarioService


class AtualizarUsuarioService:
    """Caso de uso: atualizar os dados de um usuário existente."""

    def __init__(self, usuario_id, dados):
        self.usuario_id = usuario_id
        self.dados = dados or {}

    def execute(self):
        usuario = BuscarUsuarioService(self.usuario_id).execute()
        email = self.dados.get("email")
        if email and email.strip().lower() != usuario.email:
            outro = Usuario.buscar_por_email(email)
            if outro and outro.id != usuario.id:
                raise ValueError("Já existe um usuário com este e-mail.")
        senha = self.dados.get("senha")
        if senha is not None and senha != "" and len(senha) < 6:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        return usuario.atualizar(
            nome=self.dados.get("nome"),
            email=email,
            senha=senha,
        )
