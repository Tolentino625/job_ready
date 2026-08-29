from flask import Blueprint, jsonify, request
from flask.views import MethodView

from app.services.resposta.criar_resposta_service import CriarRespostaService
from app.services.resposta.listar_respostas_service import ListarRespostasService
from app.services.resposta.buscar_resposta_service import BuscarRespostaService
from app.services.resposta.atualizar_resposta_service import AtualizarRespostaService
from app.services.resposta.deletar_resposta_service import DeletarRespostaService

resposta_bp = Blueprint("resposta_bp", __name__)


class RespostaListController(MethodView):
    """Controller (classe) responsável pela coleção /api/respostas."""

    def get(self):
        respostas = ListarRespostasService().execute()
        return jsonify([r.to_dict() for r in respostas])

    def post(self):
        try:
            resposta = CriarRespostaService(request.get_json(force=True)).execute()
            return jsonify(resposta.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400


class RespostaDetailController(MethodView):
    """Controller (classe) responsável pelo item /api/respostas/<id>."""

    def get(self, resposta_id):
        try:
            resposta = BuscarRespostaService(resposta_id).execute()
            return jsonify(resposta.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404

    def put(self, resposta_id):
        try:
            resposta = AtualizarRespostaService(resposta_id, request.get_json(force=True)).execute()
            return jsonify(resposta.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    def delete(self, resposta_id):
        try:
            DeletarRespostaService(resposta_id).execute()
            return jsonify({"mensagem": "Resposta excluída com sucesso."})
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404


resposta_bp.add_url_rule(
    "/api/respostas", view_func=RespostaListController.as_view("resposta_list")
)
resposta_bp.add_url_rule(
    "/api/respostas/<int:resposta_id>", view_func=RespostaDetailController.as_view("resposta_detail")
)
