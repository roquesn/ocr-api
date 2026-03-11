from services.claude_service import parse_contract

def parse_document(text, company):
    return parse_contract(text)