'''
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
'''

nome = input('Digite seu nome: ')
distancia = float(input('Digite a distância percorrida: '))
gasto_combustivel = (float(input('Digite a quantidade de combustível gasto: ')))
consumo = distancia / gasto_combustivel

print(f'Olá tudo bem {nome}? A distância percorrida foi de {distancia:.2f} km e o consumo médio do combustível foi de {consumo:.2f} km/l')