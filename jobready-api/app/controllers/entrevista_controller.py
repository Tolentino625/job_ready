from flask import Blueprint, jsonify, request
from flask.views import MethodView

from app.services.entrevista.criar_entrevista_service import CriarEntrevistaService
from app.services.entrevista.listar_entrevistas_service import ListarEntrevistasService
from app.services.entrevista.buscar_entrevista_service import BuscarEntrevistaService
from app.services.entrevista.atualizar_entrevista_service import AtualizarEntrevistaService
from app.services.entrevista.deletar_entrevista_service import DeletarEntrevistaService

entrevista_bp = Blueprint("entrevista_bp", __name__)


class EntrevistaListController(MethodView):
    """Controller (classe) responsável pela coleção /api/entrevistas."""

    def get(self):
        entrevistas = ListarEntrevistasService().execute()
        return jsonify([e.to_dict() for e in entrevistas])

    def post(self):
        try:
            entrevista = CriarEntrevistaService(request.get_json(force=True)).execute()
            return jsonify(entrevista.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400


class EntrevistaDetailController(MethodView):
    """Controller (classe) responsável pelo item /api/entrevistas/<id>."""

    def get(self, entrevista_id):
        try:
            entrevista = BuscarEntrevistaService(entrevista_id).execute()
            return jsonify(entrevista.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404

    def put(self, entrevista_id):
        try:
            entrevista = AtualizarEntrevistaService(entrevista_id, request.get_json(force=True)).execute()
            return jsonify(entrevista.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    def delete(self, entrevista_id):
        try:
            DeletarEntrevistaService(entrevista_id).execute()
            return jsonify({"mensagem": "Entrevista excluída com sucesso."})
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404


entrevista_bp.add_url_rule(
    "/api/entrevistas", view_func=EntrevistaListController.as_view("entrevista_list")
)
entrevista_bp.add_url_rule(
    "/api/entrevistas/<int:entrevista_id>", view_func=EntrevistaDetailController.as_view("entrevista_detail")
)
