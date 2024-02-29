import spacy
import pdfplumber
import re

# Carregar o modelo de língua portuguesa do spaCy
nlp = spacy.load("pt_core_news_sm")

# Função para extrair informações do currículo
def extrair_informacoes(curriculo_texto):
    # Inicializar variáveis para armazenar as informações extraídas
    nome = ""
    endereco = ""
    educacao = []
    experiencia = []
    habilidades = []

    # Identificar automaticamente as seções do currículo
    secoes = re.split(r"\n(?=[A-Z\s]+:)", curriculo_texto)

    # Iterar sobre as seções identificadas
    for secao in secoes:
        secao = secao.strip()
        # Processar o texto da seção com o spaCy
        doc = nlp(secao)

        # Identificar entidades relevantes na seção
        for entidade in doc.ents:
            if entidade.label_ == "PER" and not nome:
                nome = entidade.text
            elif entidade.label_ == "LOC" and not endereco:
                endereco = entidade.text
            elif entidade.label_ == "ORG":
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

# Função para ler o arquivo PDF do currículo
def ler_pdf(nome_arquivo):
    texto = ""
    with pdfplumber.open(nome_arquivo) as pdf:
        for page in pdf.pages:
            texto += page.extract_text()
    return texto

# Solicitar ao usuário o nome do arquivo
nome_arquivo_pdf = input("Qual o nome completo do arquivo a ser lido? ")

# Ler o conteúdo do currículo
texto_curriculo = ler_pdf(nome_arquivo_pdf)

# Extrair informações do currículo
informacoes = extrair_informacoes(texto_curriculo)

# Exibir as informações extraídas
print(informacoes)
