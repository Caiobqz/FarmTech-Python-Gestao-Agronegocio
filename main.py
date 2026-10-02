"""Ponto de entrada do projeto FarmTech.

A estrutura inicial foi criada para orientar a divisão do grupo.
As opções devem ser conectadas aos módulos conforme cada etapa for concluída.
"""


def mostrar_menu():
    print("\n" + "=" * 36)
    print("       FARMTECH SOLUTIONS")
    print("=" * 36)
    print("1 - Cadastrar área agrícola")
    print("2 - Listar áreas")
    print("3 - Consultar área")
    print("4 - Atualizar área")
    print("5 - Excluir área")
    print("6 - Registrar dados agrícolas")
    print("7 - Exportar relatório TXT")
    print("8 - Salvar/carregar dados JSON")
    print("9 - Sincronizar/consultar Oracle")
    print("0 - Sair")


def main():
    """Executa o menu principal.

    TODO: integrar as funções dos módulos em src/.
    """
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Programa encerrado.")
            break

        print("Opção ainda em desenvolvimento.")


if __name__ == "__main__":
    main()
