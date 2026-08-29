from app.services.curriculo.arquivo_service import apagar_arquivo, salvar_arquivo
from app.services.curriculo.buscar_curriculo_service import BuscarCurriculoService


class AtualizarCurriculoService:
    """Caso de uso: atualizar currículo e substituir o anexo quando enviado."""

    def __init__(self, curriculo_id, dados, arquivo=None):
        self.curriculo_id = curriculo_id
        self.dados = dados or {}
        self.arquivo = arquivo

    def execute(self):
        curriculo = BuscarCurriculoService(self.curriculo_id).execute()
        arquivo_info = salvar_arquivo(self.arquivo) if self.arquivo else None
        antigo = curriculo.arquivo_path
        try:
            atualizado = curriculo.atualizar(
                nome_arquivo=arquivo_info["nome_arquivo"] if arquivo_info else self.dados.get("nome_arquivo"),
                conteudo_texto=self.dados.get("conteudo_texto"),
                pontos_fortes=self.dados.get("pontos_fortes"),
                pontos_a_melhorar=self.dados.get("pontos_a_melhorar"),
                arquivo_path=arquivo_info["arquivo_path"] if arquivo_info else None,
                arquivo_mimetype=arquivo_info["arquivo_mimetype"] if arquivo_info else None,
            )
            if arquivo_info and antigo:
                apagar_arquivo(antigo)
            return atualizado
        except Exception:
            if arquivo_info:
                apagar_arquivo(arquivo_info["arquivo_path"])
            raise
