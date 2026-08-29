"""
Script opcional para popular o banco com um conjunto inicial de perguntas
frequentes de entrevista. Rode com: python seed.py
"""
from app import create_app, db
from app.models.pergunta import Pergunta

PERGUNTAS = [
    ("Fale um pouco sobre você.", "comportamental", "facil",
     "Estruture em: formação, experiência relevante e o que busca agora."),
    ("Qual seu maior ponto fraco?", "comportamental", "media",
     "Escolha um ponto real e mostre o que está fazendo para melhorar."),
    ("Por que devemos te contratar?", "comportamental", "media",
     "Conecte suas habilidades diretamente com os requisitos da vaga."),
    ("Explique o conceito de complexidade de algoritmos.", "tecnica", "dificil",
     "Fale sobre notação Big-O e dê exemplos de O(1), O(n) e O(n log n)."),
    ("Como você lida com prazos apertados?", "situacional", "media",
     "Descreva um exemplo real usando priorização e comunicação com o time."),
]

app = create_app()
with app.app_context():
    db.create_all()
    if Pergunta.query.count() == 0:
        for texto, categoria, dificuldade, sugestao in PERGUNTAS:
            Pergunta.criar(texto, categoria, dificuldade, sugestao)
        print(f"{len(PERGUNTAS)} perguntas inseridas com sucesso.")
    else:
        print("Já existem perguntas cadastradas — nenhuma ação realizada.")
