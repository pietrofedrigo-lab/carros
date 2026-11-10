# ==============================================================================
# SCRIPT: carros.py (ou cadrasto.py)
# DESCRIÇÃO: Lê o arquivo 'carros.txt' (modelo , velocidade) e exibe o carro mais rápido.
# ==============================================================================

def buscar_carro_mais_rapido():
    maior_velocidade = -1.0
    carro_mais_rapido = ""

    print("--- Iniciando Análise de Frota ---")

    try:
        with open("carros.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                
                if not linha or "," not in linha:
                    continue
                
                partes = linha.split(",")
                if len(partes) == 2:
                    modelo = partes[0].strip()
                    try:
                        velocidade = float(partes[1].strip())
                        if velocidade > maior_velocidade:
                            maior_velocidade = velocidade
                            carro_mais_rapido = modelo
                    except ValueError:
                        continue

        print("---------------------------------")
        if carro_mais_rapido:
            print(f"RESULTADO: O carro mais rápido é o '{carro_mais_rapido}'")
            print(f"VELOCIDADE: {maior_velocidade} km/h")
        else:
            print("RESULTADO: Nenhum carro válido foi encontrado no arquivo.")

    except FileNotFoundError:
        print("[ERRO] O arquivo 'carros.txt' não foi encontrado.")

    print("--- Fim da Análise ---")

if __name__ == "__main__":
    buscar_carro_mais_rapido()