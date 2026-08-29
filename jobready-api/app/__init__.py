from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import inspect, text

from app.extensions import db

__all__ = ["create_app", "db"]


def _migrar_schema():
    """Adiciona colunas novas sem apagar dados existentes do SQLite."""
    inspector = inspect(db.engine)
    if "curriculos" in inspector.get_table_names():
        colunas = {c["name"] for c in inspector.get_columns("curriculos")}
        with db.engine.begin() as conn:
            if "arquivo_path" not in colunas:
                conn.execute(text("ALTER TABLE curriculos ADD COLUMN arquivo_path VARCHAR(500)"))
            if "arquivo_mimetype" not in colunas:
                conn.execute(text("ALTER TABLE curriculos ADD COLUMN arquivo_mimetype VARCHAR(120)"))


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024

    db.init_app(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    from app.models import usuario, curriculo, pergunta, entrevista, resposta, feedback, lembrete  # noqa

    with app.app_context():
        db.create_all()
        _migrar_schema()

    from app.controllers.usuario_controller import usuario_bp
    from app.controllers.curriculo_controller import curriculo_bp
    from app.controllers.pergunta_controller import pergunta_bp
    from app.controllers.entrevista_controller import entrevista_bp
    from app.controllers.resposta_controller import resposta_bp
    from app.controllers.feedback_controller import feedback_bp
    from app.controllers.lembrete_controller import lembrete_bp
    from app.controllers.auth_controller import auth_bp

    app.register_blueprint(usuario_bp)
    app.register_blueprint(curriculo_bp)
    app.register_blueprint(pergunta_bp)
    app.register_blueprint(entrevista_bp)
    app.register_blueprint(resposta_bp)
    app.register_blueprint(feedback_bp)
    app.register_blueprint(lembrete_bp)
    app.register_blueprint(auth_bp)

    @app.before_request
    def proteger_api():
        if request.method == "OPTIONS":
            return None
        if not request.path.startswith("/api/"):
            return None
        if request.path.startswith("/api/auth/"):
            return None

        from app.services.auth.auth_service import usuario_autenticado
        if not usuario_autenticado():
            return jsonify({"erro": "Autenticação necessária."}), 401
        return None

    @app.errorhandler(413)
    def arquivo_grande(_error):
        return jsonify({"erro": "O arquivo deve ter no máximo 10 MB."}), 413

    @app.route("/")
    def index():
        return jsonify({
            "servico": "JobReady API",
            "descricao": "API REST do JobReady.",
            "recursos": [
                "/api/auth/login",
                "/api/auth/registro",
                "/api/usuarios",
                "/api/curriculos",
                "/api/perguntas",
                "/api/entrevistas",
                "/api/respostas",
                "/api/feedbacks",
                "/api/lembretes",
            ],
        })

    return app
