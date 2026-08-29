from app.models.usuario import Usuario


class ListarUsuariosService:
    """Caso de uso: listar todos os usuários cadastrados."""

    def execute(self):
        return Usuario.listar()
