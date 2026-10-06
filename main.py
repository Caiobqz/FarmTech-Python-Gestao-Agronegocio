"""Ponto de entrada do projeto FarmTech."""

from src.arquivos import (
    carregar_json,
    exportar_relatorio_txt,
    salvar_json,
)
from src.banco_oracle import (
    conectar,
    consultar_areas,
    fechar_conexao,
    inserir_area,
)
from src.cadastro import cadastrar_area
from src.consultas import (
    atualizar_area,
    consultar_por_id,
    excluir_area,
    listar_areas,
)
from src.validacoes import ler_inteiro_positivo


def mostrar_menu():
    """Exibe as opções disponíveis no sistema."""
    print("\n" + "=" * 42)
    print("          FARMTECH SOLUTIONS")
    print("=" * 42)
    print("1  - Cadastrar área agrícola")
    print("2  - Listar áreas")
    print("3  - Consultar área por ID")
    print("4  - Atualizar área")
    print("5  - Excluir área")
    print("6  - Salvar dados em JSON")
    print("7  - Carregar dados do JSON")
    print("8  - Exportar relatório TXT")
    print("9  - Enviar registros ao Oracle")
    print("10 - Consultar registros do Oracle")
    print("0  - Sair")


def enviar_registros_oracle(registros):
    """Envia os registros em memória para o Oracle."""
    if not registros:
        print("Nenhuma área cadastrada para enviar ao Oracle.")
        return

    conexao = conectar()

    if conexao is None:
        return

    try:
        enviados = 0

        for registro in registros:
            if inserir_area(conexao, registro):
                enviados += 1

        print(
            f"Sincronização concluída: {enviados} de "
            f"{len(registros)} registro(s) inserido(s)."
        )
    finally:
        fechar_conexao(conexao)


def consultar_oracle():
    """Consulta os registros existentes no Oracle e os exibe."""
    conexao = conectar()

    if conexao is None:
        return

    try:
        registros_oracle = consultar_areas(conexao)

        if registros_oracle:
            listar_areas(registros_oracle)
    finally:
        fechar_conexao(conexao)


def main():
    """Executa o menu principal e mantém os registros em memória."""
    registros = []

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_area(registros)

        elif opcao == "2":
            listar_areas(registros)

        elif opcao == "3":
            id_area = ler_inteiro_positivo("Digite o ID da área: ")
            consultar_por_id(registros, id_area)

        elif opcao == "4":
            id_area = ler_inteiro_positivo("Digite o ID da área: ")
            atualizar_area(registros, id_area)

        elif opcao == "5":
            id_area = ler_inteiro_positivo("Digite o ID da área: ")
            excluir_area(registros, id_area)

        elif opcao == "6":
            salvar_json(registros)

        elif opcao == "7":
            registros = carregar_json()

        elif opcao == "8":
            exportar_relatorio_txt(registros)

        elif opcao == "9":
            enviar_registros_oracle(registros)

        elif opcao == "10":
            consultar_oracle()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    main()
