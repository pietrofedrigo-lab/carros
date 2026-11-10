# ==============================================================================
# SCRIPT: alterar_desconto_carros.py
# DESCRIÇÃO: Carrega os carros do arquivo 'carros.txt', permite escolher 
#             um carro e aplicar um desconto personalizado.
# ==============================================================================

def carregar_carros():
    """Lê o arquivo carros.txt e retorna um dicionário {modelo: velocidade}"""
    carros = {}
    try:
        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha or "," not in linha or linha.startswith("#"):
                    continue
                partes = linha.split(",")
                if len(partes) == 2:
                    modelo = partes[0].strip()
                    try:
                        velocidade = float(partes[1].strip())
                        carros[modelo] = velocidade
                    except ValueError:
                        continue
    except FileNotFoundError:
        print("[ERRO] Arquivo 'carros.txt' não encontrado.")
    return carros


def menu_interativo():
    carros = carregar_carros()
    
    if not carros:
        print("Nenhum carro encontrado para exibição.")
        return

    # Lista de modelos para acesso por número
    lista_modelos = list(carros.keys())

    while True:
        print("\n=== SELEÇÃO DE CARROS ===")
        for i, modelo in enumerate(lista_modelos, 1):
            print(f"{i}. {modelo.capitalize()} (Velocidade/Preço base: {carros[modelo]})")
        print("0. Sair")
        print("=========================")

        opcao = input("Escolha o número do carro que deseja alterar/aplicar desconto: ").strip()

        if opcao == "0":
            print("Saindo do programa...")
            break

        if not opcao.isdigit() or int(opcao) < 1 or int(opcao) > len(lista_modelos):
            print("[ERRO] Opção inválida! Escolha um número da lista.")
            continue

        # Carro selecionado
        modelo_escolhido = lista_modelos[int(opcao) - 1]
        valor_base = carros[modelo_escolhido]

        print(f"\nCarro Selecionado: {modelo_escolhido.upper()}")
        print(f"Valor/Velocidade Base: {valor_base}")

        try:
            desconto = float(input("Digite a porcentagem de desconto (%): "))
            
            if desconto < 0 or desconto > 100:
                print("[ERRO] O desconto deve estar entre 0% e 100%.")
                continue

            valor_desconto = valor_base * (desconto / 100)
            valor_final = valor_base - valor_desconto

            print("\n--- RESUMO DO DESCONTO ---")
            print(f"Carro: {modelo_escolhido.capitalize()}")
            print(f"Valor Original: R$ {valor_base:.2f}")
            print(f"Desconto Aplicado ({desconto}%): -R$ {valor_desconto:.2f}")
            print(f"Valor Final: R$ {valor_final:.2f}")
            print("--------------------------")

        except ValueError:
            print("[ERRO] Digite um valor numérico válido para o desconto.")

        # Opção para continuar ou encerrar
        continuar = input("\nDeseja escolher outro carro? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break


if __name__ == "__main__":
    menu_interativo()