# Contador de Números em PDF

Este é um script Python de linha de comando projetado para analisar arquivos PDF. Ele extrai todos os números presentes no texto do documento, filtra-os para manter apenas aqueles com 2 ou 3 dígitos, e então conta a frequência de cada número.

O resultado é exibido em duas seções: uma lista de "Números Principais" predefinidos (com suas contagens, mesmo que seja zero) e uma lista de todos os outros números encontrados no PDF.

## Funcionalidades

- **Extração de Texto de PDF**: Utiliza a biblioteca `PyPDF2` para ler o conteúdo de cada página de um arquivo PDF.
- **Filtragem Inteligente**: Isola apenas números com 2 ou 3 dígitos, ignorando números muito pequenos (um dígito) ou muito grandes (4+ dígitos).
- **Contagem de Frequência**: Conta quantas vezes cada número aparece no documento.
- **Relatório Organizado**: Apresenta os resultados em duas categorias claras: "Números Principais" e "Outros Números", para fácil visualização.

## Requisitos

- Python 3.x
- Biblioteca `PyPDF2`

## Instalação

1.  Clone este repositório para a sua máquina local:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  Instale as dependências necessárias. É recomendado criar um ambiente virtual.
    ```bash
    # Crie e ative um ambiente virtual (opcional, mas recomendado)
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

    # Instale a biblioteca
    pip install PyPDF2
    ```

## Como Usar

1.  Execute o script a partir do seu terminal:
    ```bash
    python Contador_CH.py
    ```

2.  O script solicitará que você insira o caminho para o arquivo PDF que deseja analisar:
    ```
    Enter the path to the PDF file: /caminho/para/seu/documento.pdf
    ```

3.  Após a análise, o script exibirá a contagem dos números diretamente no terminal.

### Exemplo de Saída

```
Main Numbers
Number		Count
====================
90		5
100		0
105		2
135		8
150		1
157		0
175		12
180		3
200		0
210		4
====================

Other Numbers
Number		Count
====================
20		1
45		6
110		2
350		1
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.