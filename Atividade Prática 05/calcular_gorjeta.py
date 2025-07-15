def calcular_gorjeta(valor_total_conta, porcentagem_gorjeta):
    try:
        if not isinstance(valor_total_conta, (int, float)) or valor_total_conta < 0:
            print("Erro: O valor total da conta deve ser um número positivo.")
            return None, None
        
        if not isinstance(porcentagem_gorjeta, (int, float)) or porcentagem_gorjeta < 0:
            print("Erro: A porcentagem da gorjeta deve ser um número positivo.")
            return None, None

        valor_gorjeta = valor_total_conta * (porcentagem_gorjeta / 100)
        
        total_a_pagar = valor_total_conta + valor_gorjeta
        
        return valor_gorjeta, total_a_pagar
    
    except Exception as e:
        print(f"Ocorreu um erro ao calcular a gorjeta: {e}")
        return None, None

if __name__ == "__main__":
    print("--- Calculadora de Gorjeta ---")
    
    while True:
        try:
            total_conta_str = input("Digite o valor total da conta (ex: 75.50) ou 'sair' para encerrar: R$ ").replace(',', '.')
            if total_conta_str.lower() == 'sair':
                print("Programa encerrado.")
                break

            valor_conta = float(total_conta_str)

            porcentagem_str = input("Digite a porcentagem de gorjeta desejada (ex: 10 para 10%): ")
            porcentagem = float(porcentagem_str)

            gorjeta, total = calcular_gorjeta(valor_conta, porcentagem)

            if gorjeta is not None and total is not None:
                print(f"\nValor da conta: R$ {valor_conta:.2f}")
                print(f"Porcentagem da gorjeta: {porcentagem:.0f}%")
                print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
                print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")
                print("--------------------------------")
            else:
                print("Por favor, insira valores válidos.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números para o valor da conta e a porcentagem.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")