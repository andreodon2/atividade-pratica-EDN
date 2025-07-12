import csv

def coleta_dados():
    nome = input('Digite o seu nome: ')
    while True:
        try:
            idade = int(input('Digite a sua idade: '))
            break
        except ValueError:
            print('Idade inválidada. Por favor, digite um número inteiro!')
    cidade = input('Digite o nome da sua cidade: ')
    return {'Nome': nome, 'Idade': idade, 'Cidade': cidade}

    def escrever_pessoas_csv(nome_arquivo, dados_pessoas):
        nomes_colunas = ['Nome', 'Idade', 'Cidade']
        with open(nome_arquivo, 'a+', new_line='', encoding = 'utf-8') as arquivo_csv:
            arquivo_csv.seek(0)
            primeira_linha = arquivo_csv.readline()

            escritor_csv = csv.DictWriter(arquivo_csv, fieldnames = nomes_colunas)

            if not primeira_linha or primeira_linha.strip() != ','.join(nomes_colunas):
                escritor_csv = csv.writeheader()

                for pessoa in dados_pessoas:
                    escritor_csv.writerow(pessoa)
    print(f"Dados gravados com sucesso em  '{nome_arquivo}'")
    if __name__ == "__main__":
        lista_pessoas = []
    
    while True:
        nova_pessoa = coletar_dados_pessoa()
        lista_pessoas.append(nova_pessoa)
        
        continuar = input("Deseja adicionar outra pessoa? (s/n): ").lower()
        if continuar != 's':
            break
            
    escrever_pessoas_csv('pessoas.csv', lista_pessoas)

    print("\nConteúdo atualizado do arquivo 'pessoas.csv':")
    try:
        with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo 'pessoas.csv' não foi encontrado.")