import spacy

# Carregar o modelo de língua inglesa do spaCy
nlp = spacy.load("en_core_web_sm")

def extrair_informacoes(curriculo_texto):
    # Processar o texto do currículo
    doc = nlp(curriculo_texto)

    # Inicializar variáveis para armazenar as informações extraídas
    nome = ""
    endereco = ""
    educacao = []
    experiencia = []
    habilidades = []

    # Iterar sobre as entidades no documento
    for entidade in doc.ents:
        if entidade.label_ == "PERSON":
            nome = entidade.text
        elif entidade.label_ == "GPE":
            endereco = entidade.text
        elif entidade.label_ == "ORG" or entidade.label_ == "WORK_OF_ART":
            experiencia.append(entidade.text)
        elif entidade.label_ == "DATE":
            educacao.append(entidade.text)
        elif entidade.label_ == "SKILL":
            habilidades.append(entidade.text)

    # Retornar as informações extraídas
    return {
        "Nome": nome,
        "Endereço": endereco,
        "Educação": educacao,
        "Experiência": experiencia,
        "Habilidades": habilidades
    }

# Exemplo de uso
curriculo = """
[Seu currículo em texto aqui]
"""
informacoes = extrair_informacoes(curriculo)
print(informacoes)
