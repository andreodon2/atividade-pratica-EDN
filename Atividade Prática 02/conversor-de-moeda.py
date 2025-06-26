'''
Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
'''

nome = input('Qual o seu nome? ')
real = int(input('Digite o valor em reais para ser convertido: R$ '))

dolar = real / 5.20
euro = real / 6.15

print(f'Olá, bom dia {nome}. Atendendo sua solicitação o valor R$ {real:.2f} convertido para Euro será de €{euro:.2f} e em Dólar ficará em $ {dolar:.2f}')