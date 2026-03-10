from anthropic import Anthropic
from config import CLAUDE_API_KEY

client = Anthropic(api_key=CLAUDE_API_KEY)


def improve_extraction(text):

    prompt = f"""
Extract structured data from this automotive protection contract.

{text}

Return JSON with:

numero_contrato
numero_proposta
cliente
veiculos
"""

    response = client.messages.create(
        model="claude-3-7-sonnet",
        max_tokens=2000,
        messages=[{"role":"user","content":prompt}]
    )

    return response.content