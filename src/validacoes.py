"""Funções de validação de entrada.

Responsabilidade: concentrar regras de validação para evitar lógica repetida
nos demais módulos.
"""


def ler_float_positivo(mensagem):
    """Lê um número decimal maior que zero."""

    while True:
        try:
            valor = float(input(mensagem))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
            else:
                return valor

        except ValueError:
            print("Ops, isso não é um valor numérico.")


def ler_inteiro_positivo(mensagem):
    """Lê um número inteiro maior que zero."""

    while True:
        try:
            valor = int(input(mensagem))

            if valor <= 0:
                print("O valor deve ser maior que zero.")
            else:
                return valor

        except ValueError:
            print("Ops, isso não é um valor numérico.")

def ler_texto_obrigatorio(mensagem):
    """Lê um texto obrigatório (não vazio)."""

    while True:
        texto = input(mensagem).strip()

        if not texto:
            print("O valor não pode ser vazio.")
        else:
            return texto
