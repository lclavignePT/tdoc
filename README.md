
# Documentador de Estrutura e Conteúdo de Arquivos

Este script em Python gera um documento `.txt` contendo a estrutura de diretórios de um caminho especificado e o conteúdo de arquivos selecionados, conforme definido em um arquivo de configuração (`config.ini`). Ele permite incluir/excluir diretórios específicos, focar em extensões desejadas, e até mesmo arquivos específicos sem extensão, como `.gitignore` ou `Dockerfile`.

## Pré-requisitos

- Python 3.x instalado no sistema.

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

## Como Usar

1. Clone este repositório ou faça download dos arquivos necessários.
2. Configure o `config.ini` conforme desejado.
3. No terminal, navegue até o diretório onde o script está localizado.
4. Execute o script passando o diretório que deseja documentar como argumento ou, caso não seja especificado, ele usará o diretório atual.

### Comandos de Execução

Para executar o script no diretório atual:

```bash
python3 script.py
```

Para especificar um diretório:

```bash
python3 script.py /caminho/para/diretorio
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

- O arquivo de saída incluirá o nome do diretório e um timestamp (em formato Unix) para rastrear o momento da geração do documento.
- Arquivos ocultos (começando com `.`) serão incluídos na estrutura do diretório.
- Se o arquivo `config.ini` estiver ausente ou sem configuração de extensões e arquivos específicos, o script executará apenas a estrutura de diretórios (`tree`).

## Erros e Logs

Caso o script não encontre o `config.ini` ou detecte que ele está vazio, exibirá avisos informando que somente a estrutura do diretório será documentada.
