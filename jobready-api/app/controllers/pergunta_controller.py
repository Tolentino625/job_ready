from flask import Blueprint, jsonify, request
from flask.views import MethodView

from app.services.pergunta.criar_pergunta_service import CriarPerguntaService
from app.services.pergunta.listar_perguntas_service import ListarPerguntasService
from app.services.pergunta.buscar_pergunta_service import BuscarPerguntaService
from app.services.pergunta.atualizar_pergunta_service import AtualizarPerguntaService
from app.services.pergunta.deletar_pergunta_service import DeletarPerguntaService
from app.services.pergunta.gerar_perguntas_service import GerarPerguntasService

pergunta_bp = Blueprint("pergunta_bp", __name__)


class PerguntaListController(MethodView):
    """Controller (classe) responsável pela coleção /api/perguntas."""

    def get(self):
        perguntas = ListarPerguntasService().execute()
        return jsonify([p.to_dict() for p in perguntas])

    def post(self):
        try:
            pergunta = CriarPerguntaService(request.get_json(force=True)).execute()
            return jsonify(pergunta.to_dict()), 201
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400


@pergunta_bp.post("/api/perguntas/gerar")
def gerar_perguntas():
    try:
        perguntas = GerarPerguntasService(request.get_json(force=True) or {}).execute()
        return jsonify({"perguntas": [p.to_dict() for p in perguntas]}), 201
    except (ValueError, TypeError) as e:
        return jsonify({"erro": str(e)}), 400
    except RuntimeError as e:
        return jsonify({"erro": str(e)}), 500


class PerguntaDetailController(MethodView):
    """Controller (classe) responsável pelo item /api/perguntas/<id>."""

    def get(self, pergunta_id):
        try:
            pergunta = BuscarPerguntaService(pergunta_id).execute()
            return jsonify(pergunta.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404

    def put(self, pergunta_id):
        try:
            pergunta = AtualizarPerguntaService(pergunta_id, request.get_json(force=True)).execute()
            return jsonify(pergunta.to_dict())
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404
        except ValueError as e:
            return jsonify({"erro": str(e)}), 400

    def delete(self, pergunta_id):
        try:
            DeletarPerguntaService(pergunta_id).execute()
            return jsonify({"mensagem": "Pergunta excluída com sucesso."})
        except LookupError as e:
            return jsonify({"erro": str(e)}), 404


pergunta_bp.add_url_rule(
    "/api/perguntas", view_func=PerguntaListController.as_view("pergunta_list")
)
pergunta_bp.add_url_rule(
    "/api/perguntas/<int:pergunta_id>", view_func=PerguntaDetailController.as_view("pergunta_detail")
)
