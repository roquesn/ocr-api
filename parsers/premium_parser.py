import re


def parse_premium(text):

    proposta = re.search(r"Número:\s*(\S+)", text)
    nome = re.search(r"Nome completo/ Razão Social:\s*(.+)", text)
    cpf = re.search(r"CPF/CNPJ:\s*(\S+)", text)
    placa = re.search(r"Placa:\s*(\S+)", text)

    return {
        "numero_contrato": "",
        "numero_proposta": proposta.group(1) if proposta else "",
        "cliente": {
            "nome": nome.group(1).strip() if nome else "",
            "cpf_cnpj": cpf.group(1) if cpf else "",
            "telefone": "",
            "email": ""
        },
        "veiculos": [
            {
                "placa": placa.group(1) if placa else "",
                "marca": "",
                "modelo": "",
                "ano_fabricacao": "",
                "ano_modelo": "",
                "renavam": "",
                "chassi": ""
            }
        ]
    }