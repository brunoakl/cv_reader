import textract
from pyresparser import ResumeParser

# Solicitar ao usuário o nome do arquivo
nome_arquivo_pdf = input("Qual o nome completo do arquivo a ser lido? ")

# Extrair texto do arquivo PDF
texto = textract.process(nome_arquivo_pdf, method='pdfminer').decode('utf-8')

# Ler o currículo e extrair as informações
dados_curriculo = ResumeParser(texto).get_extracted_data()

# Exibir as informações extraídas
print(dados_curriculo)
