import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configurações gerais da aplicação Flask."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "jobready-dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'jobready.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    GEMINI_MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.7-flash")
