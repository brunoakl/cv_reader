#Este script cria um subprocesso para instalar as dependências Python
#listadas no arquivo constraints.txt.
import subprocess

def install_dependencies_from_txt(file_path):
    with open(file_path, 'r') as file:
        dependencies = file.readlines()
        dependencies = [dependency.strip() for dependency in dependencies]

    for dependency in dependencies:
                        #Preparando o comando
        subprocess.call(['pip', 'install', dependency])

if __name__ == "__main__":
    file_path = input("Digite o caminho para o arquivo .txt com as dependências: ")
    install_dependencies_from_txt(file_path)
    #Se o txt estiver na mesma pasta que este script, insira o nome 
    #completo do arquivo como resposta no terminal(Ex.: contraints.txt)
    
