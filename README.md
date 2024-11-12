
# tdoc

[![License](https://img.shields.io/github/license/lclavignePT/tdoc)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GitHub Issues](https://img.shields.io/github/issues/lclavignePT/tdoc)

Este script em Python gera um documento `.txt` contendo a estrutura de diretórios de um caminho especificado e o conteúdo de arquivos selecionados, conforme definido em um arquivo de configuração (`config.ini`). Ele permite incluir/excluir diretórios específicos, focar em extensões desejadas, e até mesmo arquivos específicos sem extensão, como `.gitignore` ou `Dockerfile`.

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação do Git](#instalação-do-git)
- [Clonando o Projeto](#clonando-o-projeto)
- [Arquivo de Configuração (config.ini)](#arquivo-de-configuração-configini)
- [Instalação com install.sh](#instalação-com-installsh)
- [Como Usar o Script Instalado](#como-usar-o-script-instalado)
- [Exemplo de Saída](#exemplo-de-saída)
- [Notas](#notas)
- [Erros e Logs](#erros-e-logs)

## Pré-requisitos

- Python 3.x instalado no sistema.

## Instalação do Git

Para clonar este projeto, você precisa ter o Git instalado em seu sistema. Siga as instruções abaixo para instalar o Git.

### No Debian/Ubuntu (derivados)

```bash
sudo apt update
sudo apt install git
```

### No Fedora

```bash
sudo dnf install git
```

### No macOS

No macOS, você pode instalar o Git usando o Homebrew:

```bash
brew install git
```

## Clonando o Projeto

Após instalar o Git, você pode clonar o repositório do projeto. No terminal, navegue até o diretório onde deseja salvar o projeto e execute o comando abaixo:

```bash
git clone https://github.com/usuario/repositorio.git
```

Substitua `https://github.com/usuario/repositorio.git` pelo URL do repositório do GitHub onde este projeto está hospedado.

## Arquivo de Configuração (`config.ini`)

Para configurar quais pastas serão excluídas, quais extensões e arquivos específicos serão documentados, utilize o arquivo `config.ini`. Aqui está um exemplo de configuração:

```ini
[settings]
excluded_directories = .venv, venv, node_modules
desired_extensions = .py, .js, .css, .html, .sh, .c, .cpp, .yml
specific_files = Dockerfile, .gitignore
```

### Descrição dos Parâmetros

- **excluded_directories**: Lista de pastas que serão ignoradas durante a documentação (separadas por vírgula).
- **desired_extensions**: Lista de extensões de arquivos que devem ser incluídas no documento gerado (separadas por vírgula).
- **specific_files**: Lista de arquivos específicos (sem extensão) a serem incluídos, como `Dockerfile` ou `.gitignore` (separados por vírgula).

> **Nota:** Certifique-se de separar cada item por vírgula e, se necessário, remover espaços extras.

## Instalação com `install.sh`

Para facilitar o uso do script, você pode instalá-lo como um comando global no sistema usando o script `install.sh`. Isso moverá o script para `~/.local/bin` e o arquivo de configuração para `~/.config/tdoc`.

### Passos para Instalação

1. No terminal, navegue até o diretório onde os arquivos `install.sh`, `tdoc.py`, e `exemplo_config.ini` estão localizados.
2. Dê permissão de execução ao `install.sh` com o comando:

   ```bash
   chmod +x install.sh
   ```

3. Execute o script de instalação:

   ```bash
   ./install.sh
   ```

O script `install.sh` renomeará `exemplo_config.ini` para `config.ini` e o copiará para `~/.config/tdoc`. Ele também tornará o comando `tdoc` acessível de qualquer lugar do sistema.

## Como Usar o Script Instalado

Após a instalação, você pode executar o comando `tdoc` em qualquer diretório:

- Para gerar a documentação no diretório atual:

  ```bash
  tdoc
  ```

- Para especificar um diretório:

  ```bash
  tdoc /caminho/para/diretorio
  ```

O script gerará um arquivo `.txt` com o nome da pasta e um timestamp, que conterá a estrutura do diretório e o conteúdo dos arquivos configurados no `config.ini`.

## Exemplo de Saída

Após a execução, o arquivo gerado terá uma estrutura como esta:

```plaintext
Estrutura de Diretórios:
<saída do comando tree>

Arquivo: /caminho/para/diretorio/exemplo.py
# conteúdo do arquivo exemplo.py

==================================================
Arquivo: /caminho/para/diretorio/Dockerfile
# conteúdo do arquivo Dockerfile

==================================================
...
```

Cada arquivo encontrado e seu conteúdo serão listados com uma linha de separação (`=====`) entre eles.

## Notas

- Atualmente só funciona utilizando o `install.sh`
- O arquivo de saída incluirá o nome do diretório e um timestamp (em formato Unix) para rastrear o momento da geração do documento.
- Arquivos ocultos (começando com `.`) serão incluídos na estrutura do diretório.
- Se o arquivo `config.ini` estiver ausente ou sem configuração de extensões e arquivos específicos, o script salvará apenas a estrutura de diretórios.

## Erros e Logs

Caso o script não encontre o `config.ini` ou detecte que ele está vazio, exibirá avisos informando que somente a estrutura do diretório será documentada.

### Licença
Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).

### Contato
Para quaisquer dúvidas, sugestões ou feedback, sinta-se à vontade para abrir uma **Issue** ou entrar em contato diretamente através do meu perfil no GitHub.
