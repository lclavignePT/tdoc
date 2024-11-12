#!/usr/bin/env python3

import subprocess
import os
import sys
import yaml
from datetime import datetime
import time

def carregar_configuracoes(config_path="config.yml"):
    """
    Carrega as configurações de um arquivo YAML especificado.
    Retorna listas de pastas excluídas e extensões desejadas, ou listas vazias se o arquivo não existir.
    """
    if not os.path.exists(config_path):
        print(f"Aviso: Arquivo '{config_path}' não encontrado. Executando apenas o comando tree.")
        return [], []
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    
    pastas_excluidas = config.get('excluded_directories', [])
    extensoes_desejadas = config.get('desired_extensions', [])
    
    if not extensoes_desejadas:
        print("Aviso: Nenhuma extensão configurada no arquivo config.yml. Executando apenas o comando tree.")
    
    return pastas_excluidas, extensoes_desejadas

def executar_comando_tree(caminho_diretorio, pastas_excluidas):
    pastas_excluidas_str = "|".join(pastas_excluidas) if pastas_excluidas else ""
    comando = f"tree -n --dirsfirst {caminho_diretorio} -I '{pastas_excluidas_str}'" if pastas_excluidas_str else f"tree -n --dirsfirst {caminho_diretorio}"
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    return resultado.stdout

def encontrar_arquivos(caminho_diretorio, extensoes, pastas_excluidas):
    """
    Percorre o diretório especificado e retorna uma lista de arquivos que correspondem
    às extensões desejadas, excluindo pastas específicas.
    """
    arquivos_encontrados = []
    pastas_excluidas_set = set(pastas_excluidas)
    
    for root, dirs, files in os.walk(caminho_diretorio):
        dirs[:] = [d for d in dirs if d not in pastas_excluidas_set]
        for file in files:
            if file == "Dockerfile" or file.startswith("Dockerfile.") or any(file.endswith(ext) for ext in extensoes):
                arquivos_encontrados.append(os.path.join(root, file))
    return arquivos_encontrados

def ler_conteudo_arquivo(caminho_arquivo):
    """
    Lê o conteúdo de um arquivo especificado e retorna o conteúdo.
    Retorna uma mensagem de erro se o arquivo não puder ser lido.
    """
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Erro ao ler {caminho_arquivo}: {e}"

def gerar_documentacao(saida_tree, arquivos_documentados, caminho_diretorio, somente_tree=False):
    # Usa o nome da pasta e o timestamp de data e hora para o nome do arquivo
    nome_diretorio = os.path.basename(os.path.normpath(caminho_diretorio))
    timestamp = int(time.time())
    #timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_txt = f"{nome_diretorio}_{timestamp}.txt"

    with open(nome_txt, "w", encoding="utf-8") as file:
        file.write("Estrutura de Diretórios:\n")
        file.write(saida_tree + "\n\n")

        # Adiciona conteúdo dos arquivos documentados apenas se não estiver no modo 'somente_tree'
        if not somente_tree:
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

# Se extensoes_desejadas estiver vazio, o script gera o documento apenas com a estrutura de diretórios
somente_tree = not extensoes_desejadas

# Encontra arquivos e lê o conteúdo (somente se houver extensões desejadas)
arquivos_documentados = {}
if not somente_tree:
    arquivos_encontrados = encontrar_arquivos(caminho_diretorio, extensoes_desejadas, pastas_excluidas)
    arquivos_documentados = {arquivo: ler_conteudo_arquivo(arquivo) for arquivo in arquivos_encontrados}

# Gera o arquivo de documentação com ou sem conteúdo de arquivos, conforme configurado
gerar_documentacao(saida_tree, arquivos_documentados, caminho_diretorio, somente_tree=somente_tree)
