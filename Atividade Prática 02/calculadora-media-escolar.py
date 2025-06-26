'''
Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
'''

nome_aluno = input('Digite o nome do aluno: ')
nota1 = float(input(f'Digite a Nota 1 do aluno(a) {nome_aluno}: '))
nota2 = float(input(f'Digite a Nota 2 do aluno(a) {nome_aluno}: '))
nota3 = float(input(f'Digite a Nota 3 do aluno(a) {nome_aluno}: '))
media = (nota1 + nota2 + nota3) / 3

print(f'O aluno {nome_aluno} possui as seguintes notas: \n- Nota 1: {nota1} \n- Nota 2: {nota2} \n- Nota 3: {nota3} \ne sua média anual foi de {media:.2f}')