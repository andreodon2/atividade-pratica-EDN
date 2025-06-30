'''
Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
'''

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade >= 0 and idade < 13:
    print('Tu és uma criança')
elif idade >= 13 and idade < 14:
    print('Tu és um adolescente')
elif idade >= 18 and idade < 60:
    print('Tu és tu adulto')
else:
    print('Tu és um idoso')