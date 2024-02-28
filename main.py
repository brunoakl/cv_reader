import spacy
import PyPDF2

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

def ler_pdf(nome_arquivo):
    texto = ""
    with open(nome_arquivo, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
        num_paginas = leitor_pdf.numPages
        for pagina_num in range(num_paginas):
            pagina = leitor_pdf.getPage(pagina_num)
            texto += pagina.extractText()
    return texto

# Exemplo de uso
nome_arquivo_pdf = input("Qual o nome do arquivo a ser lido? \n")
texto_curriculo = ler_pdf(nome_arquivo_pdf)
informacoes = extrair_informacoes(texto_curriculo)
print(informacoes)
