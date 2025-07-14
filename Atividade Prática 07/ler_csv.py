import csv

def ler_csv_pessoas(nome_arquivo):
    """
    Lê um arquivo CSV com informações de pessoas e exibe os dados na tela.

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser lido (ex: 'pessoas.csv').
    """
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.DictReader(arquivo_csv)

            print(f"Conteúdo do arquivo '{nome_arquivo}':\n")

            for linha in leitor_csv:
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    nome_do_arquivo_para_ler = 'pessoas_estaticas.csv'

    ler_csv_pessoas(nome_do_arquivo_para_ler)