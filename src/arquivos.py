"""Módulo de manipulação de arquivos (JSON e TXT) do FarmTech.

Responsabilidades:
- salvar e carregar a lista de áreas agrícolas em JSON;
- tratar erros simples de arquivo sem encerrar o programa;
- gerar um relatório TXT legível.

Cada área é um dicionário, no formato:
    {"id": 1, "nome_area": "Talhão A", "cultura": "Soja",
     "area_hectares": 15.5, "ph": 6.2, "nitrogenio": 30,
     "fosforo": 20, "potassio": 40, "observacoes": "..."}
"""

import json
import os
from datetime import datetime

# Tuplas: valores fixos que não devem mudar durante a execução.
CAMINHO_JSON_PADRAO = os.path.join("dados", "registros.json")
CAMINHO_TXT_PADRAO = os.path.join("dados", "relatorio.txt")
CAMPOS_RELATORIO = (
    ("nome_area", "Área"),
    ("cultura", "Cultura"),
    ("area_hectares", "Tamanho (ha)"),
    ("ph", "pH"),
    ("nitrogenio", "Nitrogênio (N)"),
    ("fosforo", "Fósforo (P)"),
    ("potassio", "Potássio (K)"),
    ("observacoes", "Observações"),
)

LARGURA_RELATORIO = 60


def _garantir_pasta(caminho):
    """Cria a pasta do arquivo, se ela ainda não existir."""
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)


def salvar_json(registros, caminho=CAMINHO_JSON_PADRAO):
    """Salva a lista de áreas em um arquivo JSON.

    Retorna True se salvou com sucesso e False se houve erro.
    """
    if not isinstance(registros, list):
        print("Erro: os registros precisam estar em uma lista.")
        return False

    try:
        _garantir_pasta(caminho)
        with open(caminho, "w", encoding="utf-8") as arquivo:
            json.dump(registros, arquivo, ensure_ascii=False, indent=4)
    except (OSError, TypeError) as erro:
        print(f"Erro ao salvar o JSON em '{caminho}': {erro}")
        return False

    print(f"{len(registros)} registro(s) salvo(s) em '{caminho}'.")
    return True


def carregar_json(caminho=CAMINHO_JSON_PADRAO):
    """Carrega a lista de áreas de um arquivo JSON.

    Se o arquivo não existir, estiver vazio, corrompido ou com formato
    inesperado, avisa o usuário e retorna uma lista vazia.
    """
    if not os.path.exists(caminho):
        print(f"Arquivo '{caminho}' não encontrado. Iniciando com lista vazia.")
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except json.JSONDecodeError:
        print(f"O arquivo '{caminho}' está vazio ou corrompido. Iniciando com lista vazia.")
        return []
    except OSError as erro:
        print(f"Erro ao ler '{caminho}': {erro}")
        return []

    if not isinstance(dados, list) or not all(isinstance(item, dict) for item in dados):
        print(f"Formato inválido em '{caminho}'. Era esperada uma lista de áreas.")
        return []

    print(f"{len(dados)} registro(s) carregado(s) de '{caminho}'.")
    return dados


def gerar_texto_relatorio(registros):
    """Monta o texto do relatório a partir da lista de áreas."""
    linha_dupla = "=" * LARGURA_RELATORIO
    linha_simples = "-" * LARGURA_RELATORIO
    agora = datetime.now().strftime("%d/%m/%Y %H:%M")

    linhas = [
        linha_dupla,
        "FARMTECH SOLUTIONS - RELATÓRIO DE ÁREAS AGRÍCOLAS".center(LARGURA_RELATORIO),
        linha_dupla,
        f"Gerado em: {agora}",
        f"Total de áreas: {len(registros)}",
        "",
    ]

    if not registros:
        linhas.append("Nenhuma área cadastrada.")
        linhas.append(linha_dupla)
        return "\n".join(linhas) + "\n"

    for registro in registros:
        linhas.append(f"Área nº {registro.get('id', '?')}")
        linhas.append(linha_simples)
        for chave, rotulo in CAMPOS_RELATORIO:
            valor = registro.get(chave, "")
            if valor == "" or valor is None:
                valor = "-"
            linhas.append(f"{rotulo:<16}: {valor}")
        linhas.append("")

    linhas.append(linha_dupla)
    return "\n".join(linhas) + "\n"


def exportar_relatorio_txt(registros, caminho=CAMINHO_TXT_PADRAO):
    """Gera o relatório TXT com as áreas cadastradas.

    Retorna True se exportou com sucesso e False se houve erro.
    """
    if not isinstance(registros, list):
        print("Erro: os registros precisam estar em uma lista.")
        return False

    try:
        _garantir_pasta(caminho)
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(gerar_texto_relatorio(registros))
    except OSError as erro:
        print(f"Erro ao gerar o relatório em '{caminho}': {erro}")
        return False

    print(f"Relatório exportado para '{caminho}'.")
    return True
