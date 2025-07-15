def calculadora():
    print("--- Calculadora Python ---")
    print("Operações válidas: + (adição), - (subtração), * (multiplicação), / (divisão)")

    while True:
        try:
            num1_str = input("Digite o primeiro número: ")
            num1 = float(num1_str.replace(',', '.'))

            num2_str = input("Digite o segundo número: ")
            num2 = float(num2_str.replace(',', '.'))

            operacao = input("Digite a operação (+, -, *, /): ")

            resultado = None

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero!")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Por favor, use +, -, * ou /.")

            print(f"\nResultado: {num1} {operacao} {num2} = {resultado:.2f}")
            print("Operação concluída com sucesso!")
            break

        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente com entradas válidas.")
        except ZeroDivisionError as zde:
            print(f"Erro: {zde}. Por favor, tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

if __name__ == "__main__":
    calculadora()