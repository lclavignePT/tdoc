#!/bin/bash

# Nome do script Python e arquivo de configuração de exemplo
SCRIPT_NAME="tdoc.py"  # Nome do arquivo Python original
EXEMPLO_CONFIG_NAME="exemplo_config.ini"  # Nome do arquivo de configuração de exemplo
CONFIG_NAME="config.ini"  # Nome final do arquivo de configuração

# Diretórios de destino
BIN_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/tdoc"

# Cria o diretório ~/.local/bin se ele não existir
if [ ! -d "$BIN_DIR" ]; then
    mkdir -p "$BIN_DIR"
    echo "Diretório $BIN_DIR criado."
fi

# Cria o diretório ~/.config/tdoc se ele não existir
if [ ! -d "$CONFIG_DIR" ]; then
    mkdir -p "$CONFIG_DIR"
    echo "Diretório $CONFIG_DIR criado."
fi

# Copia o script Python para ~/.local/bin, renomeando-o para "tdoc" e torna-o executável
cp "$SCRIPT_NAME" "$BIN_DIR/tdoc"
chmod +x "$BIN_DIR/tdoc"
echo "Script $SCRIPT_NAME copiado para $BIN_DIR como 'tdoc' e configurado como executável."

# Copia o arquivo de exemplo de configuração para ~/.config/tdoc como config.ini
cp "$EXEMPLO_CONFIG_NAME" "$CONFIG_DIR/$CONFIG_NAME"
echo "Arquivo de configuração $EXEMPLO_CONFIG_NAME copiado para $CONFIG_DIR como $CONFIG_NAME."

# Informa ao usuário que a instalação foi concluída
echo "Instalação concluída. Agora você pode usar o comando 'tdoc' em qualquer diretório do sistema."
echo "Para desinstalar, remova $BIN_DIR/tdoc e o diretório $CONFIG_DIR."
