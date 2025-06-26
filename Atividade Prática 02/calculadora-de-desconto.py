'''
Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
'''

produto = input('Qual o produto desejado? ')
preco_produto = int(input(f'Quanto custa o produto {produto} R$ '))
desconto = 0.20
preco_produto_desconto = preco_produto - preco_produto * desconto

print(f'O produto desejado é {produto}. Seu preço original custa R$ {preco_produto:.2f}, contudo há um desconto de 20% e portanto o preço final ficará por R$ {preco_produto_desconto:.2f}')