'''
Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''

def converter_temperatura(valor, unidade_origem, unidade_destino):
    """
    Converte uma temperatura de uma unidade para outra.

    Args:
        valor (float): O valor da temperatura.
        unidade_origem (str): A unidade da temperatura de entrada ('C', 'F' ou 'K').
        unidade_destino (str): A unidade desejada para a temperatura de saída ('C', 'F' ou 'K').

    Returns:
        float: A temperatura convertida.
        str: Uma mensagem de erro se as unidades forem inválidas.
    """
    
    # Normaliza as unidades para maiúsculas para facilitar a comparação
    unidade_origem = unidade_origem.upper()
    unidade_destino = unidade_destino.upper()

    if unidade_origem not in ['C', 'F', 'K'] or unidade_destino not in ['C', 'F', 'K']:
        return "Unidade de temperatura inválida. Por favor, use 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin."

    # Primeiro, converte a temperatura de entrada para Celsius
    if unidade_origem == 'F':
        celsius = (valor - 32) * 5/9
    elif unidade_origem == 'K':
        celsius = valor - 273.15
    else:  # unidade_origem == 'C'
        celsius = valor

    # Em seguida, converte de Celsius para a unidade de saída desejada
    if unidade_destino == 'F':
        valor_convertido = (celsius * 9/5) + 32
    elif unidade_destino == 'K':
        valor_convertido = celsius + 273.15
    else:  # unidade_destino == 'C'
        valor_convertido = celsius

    return valor_convertido

def main():
    print("Bem-vindo ao **Conversor de Temperatura**!")

    while True:
        try:
            temp_valor = float(input("Digite a temperatura: "))
            unidade_origem = input("Qual a **unidade de origem**? (C, F, K): ").strip().upper()
            unidade_destino = input("Para qual **unidade deseja converter**? (C, F, K): ").strip().upper()

            resultado = converter_temperatura(temp_valor, unidade_origem, unidade_destino)

            if isinstance(resultado, str):
                print(f"Erro: {resultado}")
            else:
                print(f"A temperatura convertida é: **{resultado:.2f} {unidade_destino}**")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número para a temperatura.")
        
        outra_conversao = input("Deseja fazer outra conversão? (s/n): ").strip().lower()
        if outra_conversao != 's':
            break

    print("Obrigado por usar o Conversor de Temperatura!")

if __name__ == "__main__":
    main()