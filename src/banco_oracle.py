"""Integração com banco de dados Oracle.

Responsável principal: Cleidimar.

As credenciais devem ser carregadas de variáveis de ambiente.
Nunca inserir usuário, senha ou DSN reais diretamente neste arquivo.
"""

import os

import oracledb
from dotenv import load_dotenv


CAMPOS_AREA = (
    "id",
    "nome_area",
    "cultura",
    "area_hectares",
    "ph",
    "nitrogenio",
    "fosforo",
    "potassio",
    "observacoes",
)


def conectar():
    """Abre uma conexão Oracle usando ORACLE_USER, ORACLE_PASSWORD e ORACLE_DSN."""
    load_dotenv()

    usuario = os.getenv("ORACLE_USER")
    senha = os.getenv("ORACLE_PASSWORD")
    dsn = os.getenv("ORACLE_DSN")

    faltantes = [
        nome
        for nome, valor in (
            ("ORACLE_USER", usuario),
            ("ORACLE_PASSWORD", senha),
            ("ORACLE_DSN", dsn),
        )
        if not valor
    ]

    if faltantes:
        print(
            "Não foi possível conectar ao Oracle. "
            "Variáveis ausentes: " + ", ".join(faltantes)
        )
        return None

    try:
        conexao = oracledb.connect(
            user=usuario,
            password=senha,
            dsn=dsn,
        )
    except oracledb.Error as erro:
        print(f"Erro ao conectar ao Oracle: {erro}")
        return None

    print("Conexão com Oracle realizada com sucesso.")
    return conexao


def inserir_area(conexao, registro):
    """Insere uma área agrícola no Oracle.

    Retorna True em caso de sucesso e False se ocorrer erro.
    """
    if conexao is None:
        print("Conexão Oracle indisponível.")
        return False

    if not isinstance(registro, dict):
        print("Registro inválido: era esperado um dicionário.")
        return False

    campos_faltantes = [campo for campo in CAMPOS_AREA if campo not in registro]

    if campos_faltantes:
        print(
            "Registro incompleto. Campos ausentes: "
            + ", ".join(campos_faltantes)
        )
        return False

    sql = """
        INSERT INTO areas_agricolas (
            id,
            nome_area,
            cultura,
            area_hectares,
            ph,
            nitrogenio,
            fosforo,
            potassio,
            observacoes
        )
        VALUES (
            :id,
            :nome_area,
            :cultura,
            :area_hectares,
            :ph,
            :nitrogenio,
            :fosforo,
            :potassio,
            :observacoes
        )
    """

    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                {
                    "id": registro["id"],
                    "nome_area": registro["nome_area"],
                    "cultura": registro["cultura"],
                    "area_hectares": registro["area_hectares"],
                    "ph": registro["ph"],
                    "nitrogenio": registro["nitrogenio"],
                    "fosforo": registro["fosforo"],
                    "potassio": registro["potassio"],
                    "observacoes": registro["observacoes"],
                },
            )
        conexao.commit()
    except oracledb.IntegrityError:
        print(
            f"Já existe um registro com o ID {registro['id']} no Oracle."
        )
        return False
    except oracledb.Error as erro:
        print(f"Erro ao inserir área no Oracle: {erro}")
        return False

    print(
        f"Área '{registro['nome_area']}' inserida no Oracle "
        f"com ID {registro['id']}."
    )
    return True


def consultar_areas(conexao):
    """Consulta todas as áreas do Oracle e retorna uma lista de dicionários."""
    if conexao is None:
        print("Conexão Oracle indisponível.")
        return []

    sql = """
        SELECT
            id,
            nome_area,
            cultura,
            area_hectares,
            ph,
            nitrogenio,
            fosforo,
            potassio,
            observacoes
        FROM areas_agricolas
        ORDER BY id
    """

    try:
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            linhas = cursor.fetchall()
    except oracledb.Error as erro:
        print(f"Erro ao consultar áreas no Oracle: {erro}")
        return []

    registros = []

    for linha in linhas:
        registros.append(dict(zip(CAMPOS_AREA, linha)))

    print(f"{len(registros)} registro(s) encontrado(s) no Oracle.")
    return registros


def testar_conexao(conexao):
    """Executa uma consulta simples para confirmar que a conexão está ativa."""
    if conexao is None:
        return False

    try:
        with conexao.cursor() as cursor:
            cursor.execute("SELECT 1 FROM dual")
            resultado = cursor.fetchone()
    except oracledb.Error as erro:
        print(f"Falha no teste da conexão Oracle: {erro}")
        return False

    return resultado is not None and resultado[0] == 1


def fechar_conexao(conexao):
    """Fecha a conexão Oracle, se ela estiver aberta."""
    if conexao is None:
        return

    try:
        conexao.close()
    except oracledb.Error as erro:
        print(f"Erro ao fechar a conexão Oracle: {erro}")
