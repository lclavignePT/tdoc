#!/usr/bin/env python3

import subprocess
import os
import sys
import yaml
from datetime import datetime

def carregar_configuracoes(config_path="config.yml"):
    """
    Carrega as configurações de um arquivo YAML especificado.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config.get('excluded_directories', []), config.get('desired_extensions', [])

def executar_comando_tree(caminho_diretorio, pastas_excluidas):
    # Converte a lista de pastas excluídas em uma string para o comando tree
    pastas_excluidas_str = "|".join(pastas_excluidas)
    comando = f"tree -n --dirsfirst {caminho_diretorio} -I '{pastas_excluidas_str}'"
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    return resultado.stdout

def encontrar_arquivos(caminho_diretorio, extensoes, pastas_excluidas):
    arquivos_encontrados = []
    pastas_excluidas_set = set(pastas_excluidas)
    
    for root, dirs, files in os.walk(caminho_diretorio):
        dirs[:] = [d for d in dirs if d not in pastas_excluidas_set]
        for file in files:
            if file == "Dockerfile" or file.startswith("Dockerfile.") or any(file.endswith(ext) for ext in extensoes):
                arquivos_encontrados.append(os.path.join(root, file))
    return arquivos_encontrados

def ler_conteudo_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Erro ao ler {caminho_arquivo}: {e}"

def gerar_documentacao(saida_tree, arquivos_documentados, caminho_diretorio):
    nome_diretorio = os.path.basename(os.path.normpath(caminho_diretorio))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_txt = f"{nome_diretorio}_{timestamp}.txt"

    with open(nome_txt, "w", encoding="utf-8") as file:
        file.write("Estrutura de Diretórios:\n")
        file.write(saida_tree + "\n\n")

        for arquivo, conteudo in arquivos_documentados.items():
            file.write(f"Arquivo: {arquivo}\n")
            file.write(conteudo + "\n")
            file.write("="*50 + "\n")
    
    print(f"Documento gerado: {nome_txt}")

# Carrega as configurações do arquivo config.yml
pastas_excluidas, extensoes_desejadas = carregar_configuracoes()

# Usa o diretório atual se nenhum caminho for passado como argumento
caminho_diretorio = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

# Executa o comando tree no caminho especificado
saida_tree = executar_comando_tree(caminho_diretorio, pastas_excluidas)

# Encontra arquivos e lê o conteúdo
arquivos_encontrados = encontrar_arquivos(caminho_diretorio, extensoes_desejadas, pastas_excluidas)
arquivos_documentados = {arquivo: ler_conteudo_arquivo(arquivo) for arquivo in arquivos_encontrados}

# Gera o arquivo de documentação
gerar_documentacao(saida_tree, arquivos_documentados, caminho_diretorio)
