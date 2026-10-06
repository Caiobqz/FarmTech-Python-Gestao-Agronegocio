"""Cadastro e estruturas de dados.

Responsável principal: Paulo Vitor.
"""

from src.validacoes import (
    ler_float_positivo,
    ler_inteiro_positivo,
    ler_texto_obrigatorio,
)


CULTURAS_PERMITIDAS = ("Soja", "Café", "Cana-de-açúcar")


def gerar_proximo_id(registros):
    """Retorna um novo ID sem repetir IDs já existentes."""
    if not registros:
        return 1

    return max(registro["id"] for registro in registros) + 1


def ler_cultura():
    """Exibe as culturas disponíveis e retorna a opção escolhida."""
    while True:
        print("\nCulturas disponíveis:")

        for indice, cultura in enumerate(CULTURAS_PERMITIDAS, start=1):
            print(f"{indice} - {cultura}")

        opcao = ler_inteiro_positivo("Digite o número da cultura: ")

        if opcao <= len(CULTURAS_PERMITIDAS):
            return CULTURAS_PERMITIDAS[opcao - 1]

        print("Opção inválida. Escolha uma cultura da lista.")


def ler_ph():
    """Lê um pH válido dentro da escala de 0 a 14."""
    while True:
        ph = ler_float_positivo("Digite o pH do solo: ")

        if ph <= 14:
            return ph

        print("O pH deve estar entre 0 e 14.")


def cadastrar_area(registros):
    """Cadastra uma área agrícola e adiciona o registro à lista recebida."""
    print("\n=== CADASTRO DE ÁREA AGRÍCOLA ===")

    nome_area = ler_texto_obrigatorio("Nome da área: ")
    cultura = ler_cultura()
    area_hectares = ler_float_positivo("Área em hectares: ")
    ph = ler_ph()
    nitrogenio = ler_float_positivo("Nitrogênio (N): ")
    fosforo = ler_float_positivo("Fósforo (P): ")
    potassio = ler_float_positivo("Potássio (K): ")
    observacoes = input("Observações (opcional): ").strip()

    registro = {
        "id": gerar_proximo_id(registros),
        "nome_area": nome_area,
        "cultura": cultura,
        "area_hectares": area_hectares,
        "ph": ph,
        "nitrogenio": nitrogenio,
        "fosforo": fosforo,
        "potassio": potassio,
        "observacoes": observacoes,
    }

    registros.append(registro)

    print(
        f"Área '{registro['nome_area']}' cadastrada com sucesso "
        f"(ID {registro['id']})."
    )

    return registro
