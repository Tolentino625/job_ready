import json
import re

from flask import current_app
from google import genai
from google.genai import types

from app.models.pergunta import Pergunta


class GerarPerguntasService:
    def __init__(self, dados):
        self.dados = dados or {}

    def execute(self):
        api_key = current_app.config.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY não configurada no ambiente do servidor.")

        quantidade = max(1, min(int(self.dados.get("quantidade", 5)), 10))
        categoria = self.dados.get("categoria", "comportamental")
        dificuldade = self.dados.get("dificuldade", "media")

        client = genai.Client(api_key=api_key)
        prompt = f"""Você é um especialista em recrutamento e entrevistas de emprego.
Gere exatamente {quantidade} perguntas de entrevista para o JobReady.
Categoria: {categoria}.
Dificuldade: {dificuldade}.

As perguntas devem ser realistas, diferentes entre si e adequadas para candidatos a vagas de emprego.
Para cada pergunta, gere também uma sugestão curta de resposta que ajude o candidato a estudar.

Responda SOMENTE com um JSON válido, sem markdown, sem comentários e sem texto adicional, neste formato:
[{{"texto": "...", "sugestao_resposta": "..."}}]"""

        response = client.models.generate_content(
            model=current_app.config.get("GEMINI_MODEL", "gemini-3.7-flash"),
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.8,
                max_output_tokens=3000,
            ),
        )

        texto = (response.text or "").strip()
        texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto, flags=re.IGNORECASE)
        try:
            perguntas = json.loads(texto)
        except json.JSONDecodeError as exc:
            raise RuntimeError("O Gemini retornou uma resposta inválida. Tente novamente.") from exc

        if not isinstance(perguntas, list):
            raise RuntimeError("O Gemini não retornou uma lista de perguntas válida.")

        criadas = []
        for item in perguntas[:quantidade]:
            if not isinstance(item, dict) or not item.get("texto"):
                continue
            criadas.append(
                Pergunta.criar(
                    texto=str(item["texto"]).strip(),
                    categoria=categoria,
                    dificuldade=dificuldade,
                    sugestao_resposta=str(item.get("sugestao_resposta") or "").strip(),
                )
            )

        if not criadas:
            raise RuntimeError("Não foi possível criar perguntas com o retorno do Gemini.")

        return criadas
