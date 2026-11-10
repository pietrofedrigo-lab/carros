# ==============================================================================
# SCRIPT: calcular_desconto.py
# DESCRIÇÃO: Recebe o valor de um carro (ou produto) e o percentual de
#             desconto, exibindo o valor do desconto e o preço final.
# ==============================================================================

def calcular_valor_com_desconto():
    print("--- Calculadora de Desconto ---")

    try:
        # Solicita ao usuário o valor original e a porcentagem de desconto
        valor_original = float(input("Digite o valor do carro/produto (R$): "))
        percentual_desconto = float(input("Digite a porcentagem de desconto (%): "))

        # Validações simples
        if valor_original < 0 or percentual_desconto < 0:
            print("[ERRO] Os valores informados não podem ser negativos.")
            return

        # Cálculo do valor economizado e do preço final
        valor_desconto = valor_original * (percentual_desconto / 100)
        valor_final = valor_original - valor_desconto

        # Exibição dos resultados
        print("---------------------------------")
        print(f"Valor Original: R$ {valor_original:.2f}")
        print(f"Desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
        print(f"Valor Final com Desconto: R$ {valor_final:.2f}")

    except ValueError:
        print("[ERRO] Por favor, digite apenas números válidos (use ponto para decimais).")

    print("---------------------------------")


if __name__ == "__main__":
    calcular_valor_com_desconto()