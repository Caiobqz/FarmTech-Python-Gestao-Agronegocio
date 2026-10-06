"""Testes manuais do módulo src/arquivos.py.

Rodar na raiz do projeto:  python teste_arquivos.py
"""

import json
import os
import tempfile

from src import arquivos

REGISTROS = [
    {"id": 1, "nome_area": "Talhão A", "cultura": "Soja", "area_hectares": 15.5,
     "ph": 6.2, "nitrogenio": 30, "fosforo": 20, "potassio": 40,
     "observacoes": "Solo bem drenado"},
    {"id": 2, "nome_area": "Talhão B", "cultura": "Milho", "area_hectares": 8.0,
     "ph": 5.8, "nitrogenio": 25, "fosforo": 18, "potassio": 35,
     "observacoes": ""},
    {"id": 3, "nome_area": "Açude Norte", "cultura": "Cana-de-açúcar",
     "area_hectares": 22.75, "ph": 6.0, "nitrogenio": 28, "fosforo": 22,
     "potassio": 41},
]


def main():
    with tempfile.TemporaryDirectory() as pasta:
        json_path = os.path.join(pasta, "sub", "registros.json")
        txt_path = os.path.join(pasta, "sub", "relatorio.txt")

        print("\n--- 1. Arquivo JSON inexistente ---")
        assert arquivos.carregar_json(json_path) == []

        print("\n--- 2. Salvar e carregar vários registros ---")
        assert arquivos.salvar_json(REGISTROS, json_path)
        assert arquivos.carregar_json(json_path) == REGISTROS

        print("\n--- 3. Acentos preservados no arquivo ---")
        with open(json_path, encoding="utf-8") as f:
            assert "Talhão A" in f.read()

        print("\n--- 4. Lista vazia (JSON e TXT) ---")
        assert arquivos.salvar_json([], json_path)
        assert arquivos.carregar_json(json_path) == []
        assert arquivos.exportar_relatorio_txt([], txt_path)
        with open(txt_path, encoding="utf-8") as f:
            assert "Nenhuma área cadastrada." in f.read()

        print("\n--- 5. JSON corrompido ---")
        with open(json_path, "w", encoding="utf-8") as f:
            f.write("{isso nao e json")
        assert arquivos.carregar_json(json_path) == []

        print("\n--- 6. JSON vazio ---")
        open(json_path, "w").close()
        assert arquivos.carregar_json(json_path) == []

        print("\n--- 7. JSON com formato inesperado ---")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump({"nao": "e lista"}, f)
        assert arquivos.carregar_json(json_path) == []

        print("\n--- 8. Entrada que não é lista ---")
        assert arquivos.salvar_json("texto", json_path) is False
        assert arquivos.exportar_relatorio_txt(None, txt_path) is False

        print("\n--- 9. Caminho impossível de gravar ---")
        arquivo_comum = os.path.join(pasta, "arquivo_comum.txt")
        with open(arquivo_comum, "w", encoding="utf-8") as f:
            f.write("sou um arquivo, não uma pasta")
        caminho_invalido = os.path.join(arquivo_comum, "x.json")
        assert arquivos.salvar_json(REGISTROS, caminho_invalido) is False

        print("\n--- 10. Relatório TXT com vários registros ---")
        assert arquivos.exportar_relatorio_txt(REGISTROS, txt_path)
        with open(txt_path, encoding="utf-8") as f:
            texto = f.read()
        assert "Total de áreas: 3" in texto and "Açude Norte" in texto
        print("\n" + texto)

    print("Todos os testes passaram.")


if __name__ == "__main__":
    main()
