"""Teste de conexão e consulta do módulo Oracle.

Pré-requisitos:
1. instalar as dependências: pip install -r requirements.txt
2. copiar .env.example para .env e preencher as credenciais;
3. executar database/criar_tabelas.sql no Oracle.

Este teste NÃO insere nem exclui dados.
"""

from src.banco_oracle import (
    conectar,
    consultar_areas,
    fechar_conexao,
    testar_conexao,
)


def main():
    conexao = conectar()

    if conexao is None:
        print("Teste interrompido: não foi possível abrir a conexão.")
        return

    try:
        assert testar_conexao(conexao), "A consulta SELECT 1 FROM dual falhou."
        print("Teste básico de conexão: OK")

        registros = consultar_areas(conexao)
        print(f"Consulta da tabela areas_agricolas: OK ({len(registros)} registro(s))")
    finally:
        fechar_conexao(conexao)


if __name__ == "__main__":
    main()
