import os
import json
import anthropic

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

PROMPT = """
Extraia as seguintes informações do contrato de proteção automotiva.

Retorne apenas JSON no formato:

{
 "numero_contrato": "",
 "numero_proposta": "",
 "cliente": {
   "nome": "",
   "cpf_cnpj": "",
   "telefone": "",
   "email": ""
 },
 "veiculos": [
   {
     "placa": "",
     "marca": "",
     "modelo": "",
     "ano_fabricacao": "",
     "ano_modelo": "",
     "renavam": "",
     "chassi": ""
   }
 ]
}

Regras importantes:
- Pode existir mais de um veículo
- Não invente dados
- Se não encontrar algo, deixe vazio
- Retorne apenas JSON
"""

def parse_contract(text: str):

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": PROMPT + "\n\nTexto do contrato:\n" + text
            }
        ]
    )

    response_text = message.content[0].text

    try:
        return json.loads(response_text)
    except:
        return {"error": response_text}