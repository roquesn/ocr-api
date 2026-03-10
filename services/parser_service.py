from parsers.autobem_parser import parse_autobem
from parsers.premium_parser import parse_premium


def parse_document(text, company):

    if company.lower() == "autobem":
        return parse_autobem(text)

    return parse_premium(text)