from app.models.curriculo import Curriculo
from app.models.usuario import Usuario
from app.services.curriculo.arquivo_service import salvar_arquivo


class CriarCurriculoService:
    """Caso de uso: registrar currículo e, opcionalmente, seu anexo."""

    def __init__(self, dados, arquivo=None):
        self.dados = dados or {}
        self.arquivo = arquivo

    def execute(self):
        usuario_id = self.dados.get("usuario_id")
        nome_arquivo = (self.dados.get("nome_arquivo") or "").strip()
        if not usuario_id:
            raise ValueError("O campo 'usuario_id' é obrigatório.")
        if not Usuario.buscar_por_id(usuario_id):
            raise ValueError("O usuário informado não existe.")

        arquivo_info = salvar_arquivo(self.arquivo) if self.arquivo else None
        if arquivo_info:
            nome_arquivo = arquivo_info["nome_arquivo"]
        if not nome_arquivo:
            raise ValueError("Informe um nome de arquivo ou selecione um anexo.")

        try:
            return Curriculo.criar(
                usuario_id=usuario_id,
                nome_arquivo=nome_arquivo,
                arquivo_path=arquivo_info["arquivo_path"] if arquivo_info else None,
                arquivo_mimetype=arquivo_info["arquivo_mimetype"] if arquivo_info else None,
                conteudo_texto=self.dados.get("conteudo_texto"),
                pontos_fortes=self.dados.get("pontos_fortes"),
                pontos_a_melhorar=self.dados.get("pontos_a_melhorar"),
            )
        except Exception:
            if arquivo_info:
                from app.services.curriculo.arquivo_service import apagar_arquivo
                apagar_arquivo(arquivo_info["arquivo_path"])
            raise
