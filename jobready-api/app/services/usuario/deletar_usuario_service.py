from app.services.usuario.buscar_usuario_service import BuscarUsuarioService


class DeletarUsuarioService:
    """Caso de uso: excluir um usuário existente."""

    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def execute(self):
        usuario = BuscarUsuarioService(self.usuario_id).execute()
        usuario.deletar()
