import re


def extract_vehicles(text):

    vehicles = []

    blocks = text.split("Item de Risco")

    for block in blocks[1:]:

        placa = re.search(r"Placa:\s*(\S+)", block)
        renavam = re.search(r"Renavam:\s*(\S+)", block)
        chassi = re.search(r"Chassi:\s*(\S+)", block)
        marca = re.search(r"Marca:\s*(.+)", block)
        modelo = re.search(r"Modelo:\s*(.+)", block)

        vehicles.append({
            "placa": placa.group(1) if placa else "",
            "marca": marca.group(1).strip() if marca else "",
            "modelo": modelo.group(1).strip() if modelo else "",
            "ano_fabricacao": "",
            "ano_modelo": "",
            "renavam": renavam.group(1) if renavam else "",
            "chassi": chassi.group(1) if chassi else ""
        })

    return vehicles


def parse_autobem(text):

    contrato = re.search(r"Nr Contrato:\s*(\S+)", text)
    proposta = re.search(r"Número da Proposta:\s*(\S+)", text)

    nome = re.search(r"Nome:\s*(.+)", text)
    cnpj = re.search(r"CNPJ:\s*([\d./-]+)", text)

    vehicles = extract_vehicles(text)

    return {
        "numero_contrato": contrato.group(1) if contrato else "",
        "numero_proposta": proposta.group(1) if proposta else "",
        "cliente": {
            "nome": nome.group(1).strip() if nome else "",
            "cpf_cnpj": cnpj.group(1) if cnpj else "",
            "telefone": "",
            "email": ""
        },
        "veiculos": vehicles
    }