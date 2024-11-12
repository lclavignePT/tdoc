# tdoc

[![License](https://img.shields.io/github/license/lclavignePT/tdoc)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GitHub Issues](https://img.shields.io/github/issues/lclavignePT/tdoc)

## Visão Geral

O **tdoc** é um script em Python que automatiza a criação de um documento `.txt` detalhando a estrutura de diretórios de um caminho especificado e o conteúdo de arquivos selecionados. Utilizando um arquivo de configuração (`config.ini`), o script permite:

- Incluir ou excluir diretórios específicos.
- Focar em extensões de arquivo desejadas.
- Incluir arquivos específicos sem extensão, como `.gitignore` ou `Dockerfile`.

Este utilitário é ideal para desenvolvedores que desejam documentar a estrutura de seus projetos de forma rápida e personalizada.

## Índice

- [Visão Geral](#visão-geral)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
  - [Instalação do Git](#instalação-do-git)
  - [Clonando o Projeto](#clonando-o-projeto)
  - [Instalação com `install.sh`](#instalação-com-installsh)
- [Configuração](#configuração)
  - [Arquivo de Configuração (`config.ini`)](#arquivo-de-configuração-configini)
  - [Descrição dos Parâmetros](#descrição-dos-parâmetros)
- [Uso](#uso)
  - [Usando o Script Instalado](#usando-o-script-instalado)
  - [Exemplo de Saída](#exemplo-de-saída)
- [Notas](#notas)
- [Erros e Logs](#erros-e-logs)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Dependências**: Nenhuma dependência externa além da biblioteca padrão do Python.

## Pré-requisitos

- **Python 3.x** instalado no sistema.
- **Git** instalado para clonar o repositório.

## Instalação

### Instalação do Git

Para clonar este projeto, você precisa ter o Git instalado em seu sistema. Siga as instruções abaixo para instalar o Git conforme seu sistema operacional.

#### No Debian/Ubuntu (derivados)

```bash
sudo apt update
sudo apt install git
```

#### No Fedora

```bash
sudo dnf install git
```
#### No macOS
No macOS, você pode instalar o Git usando o Homebrew:

```bash
brew install git
```
### Clonando o Projeto
Após instalar o Git, clone o repositório do projeto. No terminal, navegue até o diretório onde deseja salvar o projeto e execute o comando abaixo:

```bash
git clone https://github.com/lclavignePT/tdoc.git
```
### Instalação com `install.sh`
Para facilitar o uso do script, você pode instalá-lo como um comando global no sistema usando o script `install.sh`. Isso moverá o script para `~/.local/bin` e o arquivo de configuração para `~/.config/tdoc`.

#### Passos para Instalação
1. No terminal, navegue até o diretório onde os arquivos `install.sh`, `tdoc.py`, e `exemplo_config.ini` estão localizados.

2. Dê permissão de execução ao install.sh com o comando:

```bash
chmod +x install.sh
```
3. Execute o script de instalação:

```bash
./install.sh
```
O script `install.sh` realizará as seguintes ações:

- Renomeará `exemplo_config.ini` para `config.ini`.
- Copiará `config.ini` para `~/.config/tdoc`.
- Tornará o comando `tdoc` acessível de qualquer lugar do sistema.
### Configuração
#### Arquivo de Configuração (`config.ini`)
Para configurar quais pastas serão excluídas, quais extensões e arquivos específicos serão documentados, utilize o arquivo `config.ini`. Abaixo está um exemplo de configuração:

```bash
[settings]
excluded_directories = .venv, venv, node_modules
desired_extensions = .py, .js, .css, .html, .sh, .c, .cpp, .yml
specific_files = Dockerfile, .gitignore
```
### Descrição dos Parâmetros
- excluded_directories: Lista de pastas que serão ignoradas durante a documentação (separadas por vírgula).
- desired_extensions: Lista de extensões de arquivos que devem ser incluídas no documento gerado (separadas por vírgula).
- specific_files: Lista de arquivos específicos (sem extensão) a serem incluídos, como Dockerfile ou .gitignore (separados por vírgula).
>**Nota**: Certifique-se de separar cada item por vírgula e, se necessário, remover espaços extras.

### Uso
#### Usando o Script Instalado
Após a instalação, você pode executar o comando tdoc em qualquer diretório:

- **Gerar a documentação no diretório atual:**

```bash
tdoc
```
- **Especificar um diretório:**

```bash
tdoc /caminho/para/diretorio
```
O script gerará um arquivo `.txt` com o nome da pasta e um timestamp, que conterá a estrutura do diretório e o conteúdo dos arquivos configurados no `config.ini`.

### Exemplo de Saída
Após a execução, o arquivo gerado terá uma estrutura semelhante a esta:

```bash
Estrutura de Diretórios:
.
├── src
│   ├── main.py
│   └── utils.py
├── tests
│   └── test_main.py
├── Dockerfile
├── .gitignore
...

Arquivo: /caminho/para/diretorio/src/main.py
# conteúdo do arquivo main.py

==================================================
Arquivo: /caminho/para/diretorio/Dockerfile
# conteúdo do arquivo Dockerfile

==================================================
...
```
Cada arquivo encontrado e seu conteúdo serão listados com uma linha de separação (`==================================================`) entre eles.

### Notas
- Compatibilidade: Atualmente, o script funciona utilizando o `install.sh`.
- Arquivo de Saída: O arquivo de saída incluirá o nome do diretório e um timestamp (em formato Unix) para rastrear o momento da geração do documento.
- Configuração Padrão: Se o arquivo `config.ini` estiver ausente ou sem configuração de extensões e arquivos específicos, o script salvará apenas a estrutura de diretórios.
### Erros e Logs
Caso o script não encontre o `config.ini` ou detecte que ele está vazio, serão exibidos avisos informando que somente a estrutura do diretório será documentada. Para resolver:

1. **Verifique a Presença do`config.ini`:**

Certifique-se de que o arquivo `config.ini` está presente no diretório `~/.config/tdoc` após a instalação.

2. **Verifique o Conteúdo do `config.ini`:**

Assegure-se de que os parâmetros estão corretamente configurados e que não há erros de sintaxe.

3. **Logs de Erro:**

O script pode gerar logs adicionais no terminal para auxiliar na identificação de problemas. Revise as mensagens exibidas para obter mais detalhes.

### Contribuição
Contribuições são bem-vindas! Siga os passos abaixo para contribuir com o projeto:

1. **Fork o Repositório:**

Clique no botão "Fork" no canto superior direito do repositório para criar uma cópia pessoal.

2. **Clone o Repositório Forkado:**

```bash
git clone https://github.com/seu-usuario/tdoc.git
```
3. **Crie uma Branch para Sua Feature:**

```bash
git checkout -b minha-nova-feature
```
4. **Faça as Alterações Necessárias e Commit:**

```bash
git add .
git commit -m "Descrição clara da feature ou correção"
```
5. **Envie a Branch para o GitHub:**

```bash
git push origin minha-nova-feature
```
6. **Abra um Pull Request:**

Vá até o repositório original e abra um Pull Request comparando sua branch com a branch principal.

>**Nota**: Por favor, assegure-se de que suas contribuições sigam o padrão de codificação do projeto e que qualquer nova funcionalidade seja bem documentada.

### Licença
Este projeto está licenciado sob a [GNU General Public License v3.0](LICENSE).

### Contato
Para quaisquer dúvidas, sugestões ou feedback, sinta-se à vontade para abrir uma **Issue** ou entrar em contato diretamente através do meu perfil no GitHub.