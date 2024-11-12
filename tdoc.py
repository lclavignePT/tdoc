#!/usr/bin/env python3

import subprocess
import os
import sys
import time
import configparser

def carregar_configuracoes():
    """
    Carrega as configurações do arquivo INI localizado em ~/.config/tdoc/config.ini.
    Retorna listas de pastas excluídas, extensões desejadas e arquivos específicos.
    """
    config_path = os.path.expanduser("~/.config/tdoc/config.ini")
    config = configparser.ConfigParser()

    # Verifica se o arquivo de configuração existe
    if not os.path.exists(config_path):
        print(f"Aviso: Arquivo '{config_path}' não encontrado. Executando apenas o comando tree.")
        return [], [], []

    # Lê o arquivo de configuração
    config.read(config_path)
    
    if 'settings' not in config:
        print(f"Aviso: Seção 'settings' não encontrada no arquivo '{config_path}'. Executando apenas o comando tree.")
        return [], [], []
    
    pastas_excluidas = config['settings'].get('excluded_directories', '').split(',')
    extensoes_desejadas = config['settings'].get('desired_extensions', '').split(',')
    arquivos_especificos = config['settings'].get('specific_files', '').split(',')

    # Limpa espaços em branco de cada item
    pastas_excluidas = [pasta.strip() for pasta in pastas_excluidas if pasta.strip()]
    extensoes_desejadas = [ext.strip() for ext in extensoes_desejadas if ext.strip()]
    arquivos_especificos = [arquivo.strip() for arquivo in arquivos_especificos if arquivo.strip()]
    
    if not extensoes_desejadas and not arquivos_especificos:
        print("Aviso: Nenhuma extensão ou arquivo específico configurado no arquivo config.ini. Executando apenas o comando tree.")
    
    return pastas_excluidas, extensoes_desejadas, arquivos_especificos

def executar_comando_tree(caminho_diretorio, pastas_excluidas):
    # Adiciona a opção -a para incluir arquivos e pastas que começam com "."
    pastas_excluidas_str = "|".join(pastas_excluidas) if pastas_excluidas else ""
    comando = f"tree -n --dirsfirst {caminho_diretorio} -I '{pastas_excluidas_str}'" if pastas_excluidas_str else f"tree -n --dirsfirst {caminho_diretorio}"
    resultado = subprocess.run(comando, shell=True, text=True, capture_output=True)
    return resultado.stdout

def encontrar_arquivos(caminho_diretorio, extensoes, arquivos_especificos, pastas_excluidas):
    """
    Percorre o diretório especificado e retorna uma lista de arquivos que correspondem
    às extensões desejadas ou aos arquivos específicos, excluindo pastas especificadas.
    """
    arquivos_encontrados = []
    pastas_excluidas_set = set(pastas_excluidas)
    
    for root, dirs, files in os.walk(caminho_diretorio):
        # Remove pastas que devem ser excluídas da lista de diretórios a serem percorridos
        dirs[:] = [d for d in dirs if d not in pastas_excluidas_set]
        
        for file in files:
            # Verifica se o arquivo é um dos arquivos específicos ou tem uma extensão desejada
            if file in arquivos_especificos or any(file.endswith(ext) for ext in extensoes):
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
    nome_diretorio = os.path.basename(os.path.normpath(caminho_diretorio))
    timestamp = int(time.time())
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

# Carrega as configurações do arquivo config.ini
pastas_excluidas, extensoes_desejadas, arquivos_especificos = carregar_configuracoes()

# Usa o diretório atual se nenhum caminho for passado como argumento
caminho_diretorio = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

# Executa o comando tree no caminho especificado
saida_tree = executar_comando_tree(caminho_diretorio, pastas_excluidas)

# Se extensoes_desejadas e arquivos_especificos estiverem vazios, o script gera o documento apenas com a estrutura de diretórios
somente_tree = not (extensoes_desejadas or arquivos_especificos)

# Encontra arquivos e lê o conteúdo (somente se houver extensões desejadas ou arquivos específicos)
arquivos_documentados = {}
if not somente_tree:
    arquivos_encontrados = encontrar_arquivos(caminho_diretorio, extensoes_desejadas, arquivos_especificos, pastas_excluidas)
    arquivos_documentados = {arquivo: ler_conteudo_arquivo(arquivo) for arquivo in arquivos_encontrados}

# Gera o arquivo de documentação com ou sem conteúdo de arquivos, conforme configurado
gerar_documentacao(saida_tree, arquivos_documentados, caminho_diretorio, somente_tree=somente_tree)
