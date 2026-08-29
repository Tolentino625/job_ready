from app.models.usuario import Usuario


class BuscarUsuarioService:
    """Caso de uso: buscar um usuário pelo id."""

    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def execute(self):
        usuario = Usuario.buscar_por_id(self.usuario_id)
        if not usuario:
            raise LookupError("Usuário não encontrado.")
        return usuario
