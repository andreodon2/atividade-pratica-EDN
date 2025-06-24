#Calculadora de Volume
# Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:
'''* Comprimento: 12 cm
* Largura: 14 cm
* Altura: 20 cm
O programa deve calcular o volume e exibir o resultado em cm³.'''

comprimento = int(input('Digite o comprimento em cm³ da caixa: '))
largura = int(input('Digite a largura em cm³ da caixa: '))
altura = int(input('Digite a altura em cm³ da caixa: '))

volume = comprimento * largura * altura

print(f'O volume da caixa é {volume} cm³')