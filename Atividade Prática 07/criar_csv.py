import csv

def criar_csv_pessoas(nome_arquivo):
    nomes_colunas = ['Nome', 'Idade', 'Cidade']

    dados_pessoas = [
        {'Nome': 'Ana Silva', 'Idade': 28, 'Cidade': 'Belém'},
        {'Nome': 'Carlos Oliveira', 'Idade': 42, 'Cidade': 'Manaus'},
        {'Nome': 'Fernanda Costa', 'Idade': 35, 'Cidade': 'São Paulo'}
    ]

    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=nomes_colunas)

        escritor_csv.writeheader()

        escritor_csv.writerows(dados_pessoas)

    print(f"Arquivo '{nome_arquivo}' criado e preenchido com sucesso!")

if __name__ == "__main__":
    nome_do_arquivo_csv = 'pessoas_estaticas.csv'
    criar_csv_pessoas(nome_do_arquivo_csv)

    print(f"\nConteúdo do arquivo '{nome_do_arquivo_csv}':")
    try:
        with open(nome_do_arquivo_csv, 'r', encoding='utf-8') as arquivo:
            print(arquivo.read())
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado após a criação.")