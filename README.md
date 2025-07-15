# Contador de Números em PDF

Uma aplicação de desktop com interface gráfica para analisar arquivos PDF. Este programa extrai todos os números de 2 e 3 dígitos de um documento, conta a frequência de cada um e exibe os resultados de forma organizada.

Construído em Python com uma interface moderna usando a biblioteca **CustomTkinter**.


## Funcionalidades

-   **Interface Gráfica Amigável**: Fácil de usar, com um design limpo e moderno (inclui temas claro e escuro).
-   **Seleção de Arquivo Intuitiva**: Permite navegar e selecionar arquivos PDF facilmente.
-   **Extração de Texto de PDF**: Utiliza a biblioteca `PyPDF2` para ler o conteúdo de cada página do documento.
-   **Filtragem Inteligente**: Isola apenas números com 2 ou 3 dígitos, ignorando valores irrelevantes.
-   **Relatório Organizado**: Apresenta a contagem de números predefinidos e outros números encontrados em uma área de texto clara.

## Como Usar

Existem duas maneiras de usar este programa:

### Opção 1: Usando o Executável (Recomendado para Usuários)

A maneira mais fácil de usar, sem precisar instalar Python ou qualquer dependência.

1.  Vá para a seção de [**Releases**](https://github.com/felipemaiafe/Contador_CH/releases) deste repositório.
2.  Baixe o arquivo `Contador-CH.exe` da versão mais recente.
3.  Execute o arquivo. Nenhuma instalação é necessária.

### Opção 2: Executando a Partir do Código-Fonte (para Desenvolvedores)

Se você preferir rodar o script diretamente ou modificá-lo, siga os passos abaixo.

#### 1. Requisitos

-   Python 3.11 ou 3.12 (versões estáveis recomendadas).
-   Bibliotecas: `customtkinter`, `PyPDF2`.

#### 2. Instalação

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/felipemaiafe/Contador_CH.git
    cd Contador_CH
    ```

2.  Crie e ative um ambiente virtual (altamente recomendado):
    ```bash
    # Crie o ambiente
    python -m venv venv

    # Ative-o (Windows)
    .\venv\Scripts\activate
    ```

3.  Instale as dependências necessárias:
    ```bash
    pip install customtkinter PyPDF2
    ```

#### 3. Execução

Com o ambiente virtual ativado, execute o script da interface gráfica:

```bash
python Contador_CH.py
```

---

## Como Criar o Executável (.exe)

Se você modificou o código e deseja gerar seu próprio arquivo executável, você pode usar o **PyInstaller**.

1.  Instale o PyInstaller no seu ambiente virtual:
    ```bash
    pip install pyinstaller
    ```

2.  Execute o comando a seguir no terminal, a partir da pasta do projeto:
    ```bash
    pyinstaller --onefile --windowed --name ContadorCH seu_script_gui.py
    ```
    -   `--onefile`: Agrupa tudo em um único arquivo `.exe`.
    -   `--windowed`: Impede que um console de fundo seja aberto com a sua aplicação.

    O executável será criado na pasta `dist`.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE] para mais detalhes.