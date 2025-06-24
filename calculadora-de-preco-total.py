'''
Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
'''

produto = input('Digite o nome do produto desejado: ')
preco = float(input('Digite o preço unitário do produto desejado: '))
quantidade = int(input('Digite a quantidade desejada do produto: '))

total = preco * quantidade

print(f'O produto desejado é {produto}, o preço de {produto} é R$ {preco:.2f} e a quantidade desejada que o cliente quer levar é {quantidade}. O total da compra irá custar R$ {total:.2f}')