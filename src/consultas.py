"""Consulta, atualização e exclusão.

Responsável principal: Kauê Araujo.
"""

from src.cadastro import CULTURAS_PERMITIDAS


def _buscar_por_id(registros, id_area):
    """Retorna o registro com o ID informado ou None quando não encontrado."""
    for registro in registros:
        if registro.get("id") == id_area:
            return registro

    return None


def _exibir_area(registro):
    """Exibe um registro agrícola de forma legível."""
    print("-" * 40)
    print(f"ID: {registro.get('id')}")
    print(f"Nome da área: {registro.get('nome_area')}")
    print(f"Cultura: {registro.get('cultura')}")
    print(f"Área: {registro.get('area_hectares')} ha")
    print(f"pH: {registro.get('ph')}")
    print(f"Nitrogênio (N): {registro.get('nitrogenio')}")
    print(f"Fósforo (P): {registro.get('fosforo')}")
    print(f"Potássio (K): {registro.get('potassio')}")
    print(f"Observações: {registro.get('observacoes') or 'Sem observações'}")


def _ler_texto_opcional(mensagem, valor_atual):
    """Lê texto para atualização; Enter mantém o valor atual."""
    texto = input(mensagem).strip()

    if not texto:
        return valor_atual

    return texto


def _ler_float_opcional(mensagem, valor_atual, valor_maximo=None):
    """Lê número positivo para atualização; Enter mantém o valor atual."""
    while True:
        entrada = input(mensagem).strip()

        if not entrada:
            return valor_atual

        try:
            valor = float(entrada)
        except ValueError:
            print("Ops, isso não é um valor numérico.")
            continue

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue

        if valor_maximo is not None and valor > valor_maximo:
            print(f"O valor deve ser menor ou igual a {valor_maximo}.")
            continue

        return valor


def _ler_cultura_opcional(cultura_atual):
    """Permite trocar a cultura ou manter a atual pressionando Enter."""
    while True:
        print("\nCulturas disponíveis:")

        for indice, cultura in enumerate(CULTURAS_PERMITIDAS, start=1):
            print(f"{indice} - {cultura}")

        entrada = input(
            f"Nova cultura [atual: {cultura_atual}] "
            "(Enter para manter): "
        ).strip()

        if not entrada:
            return cultura_atual

        try:
            opcao = int(entrada)
        except ValueError:
            print("Digite o número correspondente à cultura.")
            continue

        if 1 <= opcao <= len(CULTURAS_PERMITIDAS):
            return CULTURAS_PERMITIDAS[opcao - 1]

        print("Opção inválida. Escolha uma cultura da lista.")


def listar_areas(registros):
    """Exibe todos os registros de forma organizada."""
    if not registros:
        print("Nenhuma área agrícola cadastrada.")
        return False

    print("\n=== ÁREAS AGRÍCOLAS CADASTRADAS ===")

    for registro in registros:
        _exibir_area(registro)

    print("-" * 40)
    return True


def consultar_por_id(registros, id_area):
    """Localiza e exibe um registro pelo ID."""
    registro = _buscar_por_id(registros, id_area)

    if registro is None:
        print(f"Nenhuma área encontrada com o ID {id_area}.")
        return None

    print("\n=== ÁREA ENCONTRADA ===")
    _exibir_area(registro)
    print("-" * 40)

    return registro


def atualizar_area(registros, id_area):
    """Atualiza um registro existente sem alterar o seu ID."""
    registro = _buscar_por_id(registros, id_area)

    if registro is None:
        print(f"Nenhuma área encontrada com o ID {id_area}.")
        return None

    print("\n=== ATUALIZAÇÃO DE ÁREA ===")
    print("Pressione Enter para manter o valor atual.")

    registro["nome_area"] = _ler_texto_opcional(
        f"Nome da área [atual: {registro['nome_area']}]: ",
        registro["nome_area"],
    )

    registro["cultura"] = _ler_cultura_opcional(registro["cultura"])

    registro["area_hectares"] = _ler_float_opcional(
        f"Área em hectares [atual: {registro['area_hectares']}]: ",
        registro["area_hectares"],
    )

    registro["ph"] = _ler_float_opcional(
        f"pH [atual: {registro['ph']}]: ",
        registro["ph"],
        valor_maximo=14,
    )

    registro["nitrogenio"] = _ler_float_opcional(
        f"Nitrogênio (N) [atual: {registro['nitrogenio']}]: ",
        registro["nitrogenio"],
    )

    registro["fosforo"] = _ler_float_opcional(
        f"Fósforo (P) [atual: {registro['fosforo']}]: ",
        registro["fosforo"],
    )

    registro["potassio"] = _ler_float_opcional(
        f"Potássio (K) [atual: {registro['potassio']}]: ",
        registro["potassio"],
    )

    registro["observacoes"] = _ler_texto_opcional(
        f"Observações [atual: {registro.get('observacoes') or 'vazio'}]: ",
        registro.get("observacoes", ""),
    )

    print(f"Área de ID {id_area} atualizada com sucesso.")
    return registro


def excluir_area(registros, id_area):
    """Exclui um registro existente da lista."""
    registro = _buscar_por_id(registros, id_area)

    if registro is None:
        print(f"Nenhuma área encontrada com o ID {id_area}.")
        return False

    registros.remove(registro)
    print(f"Área de ID {id_area} excluída com sucesso.")
    return True
