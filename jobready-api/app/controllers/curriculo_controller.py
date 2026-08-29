from pathlib import Path

from flask import Blueprint, jsonify, request, send_file
from flask.views import MethodView

from app.services.curriculo.criar_curriculo_service import CriarCurriculoService
from app.services.curriculo.listar_curriculos_service import ListarCurriculosService
from app.services.curriculo.buscar_curriculo_service import BuscarCurriculoService
from app.services.curriculo.atualizar_curriculo_service import AtualizarCurriculoService
from app.services.curriculo.deletar_curriculo_service import DeletarCurriculoService

curriculo_bp = Blueprint("curriculo_bp", __name__)


class CurriculoListController(MethodView):
    def get(self):
        curriculos = ListarCurriculosService().execute()
        return jsonify([c.to_dict() for c in curriculos])

    def post(self):
        try:
            if request.files:
                dados = request.form.to_dict()
                arquivo = request.files.get("arquivo")
            else:
                dados = request.get_json(force=True) or {}
                arquivo = None
            curriculo = CriarCurriculoService(dados, arquivo).execute()
            return jsonify(curriculo.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400


class CurriculoDetailController(MethodView):
    def get(self, curriculo_id):
        try:
            curriculo = BuscarCurriculoService(curriculo_id).execute()
            return jsonify(curriculo.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404

    def put(self, curriculo_id):
        try:
            if request.files:
                dados = request.form.to_dict()
                arquivo = request.files.get("arquivo")
            else:
                dados = request.get_json(force=True) or {}
                arquivo = None
            curriculo = AtualizarCurriculoService(curriculo_id, dados, arquivo).execute()
            return jsonify(curriculo.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    def delete(self, curriculo_id):
        try:
            DeletarCurriculoService(curriculo_id).execute()
            return jsonify({"mensagem": "Currículo excluído com sucesso."})
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404


@curriculo_bp.get("/api/curriculos/<int:curriculo_id>/arquivo")
def baixar_arquivo(curriculo_id):
    try:
        curriculo = BuscarCurriculoService(curriculo_id).execute()
    except LookupError as e:
        return jsonify({"erro": str(e)}), 404

    if not curriculo.arquivo_path:
        return jsonify({"erro": "Este currículo não possui anexo."}), 404

    base = Path(__file__).resolve().parents[2]
    caminho = (base / curriculo.arquivo_path).resolve()
    try:
        caminho.relative_to(base.resolve())
    except ValueError:
        return jsonify({"erro": "Arquivo inválido."}), 400

    if not caminho.is_file():
        return jsonify({"erro": "O arquivo não foi encontrado no servidor."}), 404

    return send_file(
        caminho,
        mimetype=curriculo.arquivo_mimetype or "application/octet-stream",
        download_name=curriculo.nome_arquivo,
        as_attachment=False,
    )


curriculo_bp.add_url_rule(
    "/api/curriculos", view_func=CurriculoListController.as_view("curriculo_list")
)
curriculo_bp.add_url_rule(
    "/api/curriculos/<int:curriculo_id>", view_func=CurriculoDetailController.as_view("curriculo_detail")
)
