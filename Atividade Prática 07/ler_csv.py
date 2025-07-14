import csv

def ler_csv_pessoas(nome_arquivo):
    """
    Lê um arquivo CSV com informações de pessoas e exibe os dados na tela.

    Args:
        nome_arquivo (str): O nome do arquivo CSV a ser lido (ex: 'pessoas.csv').
    """
    try:
        # Abre o arquivo CSV no modo de leitura ('r')
        # 'encoding='utf-8'': É importante usar a mesma codificação com a qual o arquivo foi salvo.
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            # Cria um objeto leitor CSV que lida com dicionários.
            # O DictReader lê a primeira linha como cabeçalho e mapeia
            # as linhas subsequentes para dicionários usando esses cabeçalhos como chaves.
            leitor_csv = csv.DictReader(arquivo_csv)

            print(f"Conteúdo do arquivo '{nome_arquivo}':\n")

            # Itera sobre cada linha (que é um dicionário) no arquivo CSV
            for linha in leitor_csv:
                # Exibe cada campo do dicionário
                print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")

    except FileNotFoundError:
        # Lida com o erro caso o arquivo CSV não seja encontrado
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        # Captura outros erros que possam ocorrer durante a leitura
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

# --- Como usar o script ---
if __name__ == "__main__":
    # Use o nome do arquivo CSV que você criou anteriormente.
    # Se você usou 'pessoas_estaticas.csv' no último exemplo, use-o aqui.
    # Se você gerou com input, provavelmente é 'pessoas.csv'.
    nome_do_arquivo_para_ler = 'pessoas_estaticas.csv'
    # nome_do_arquivo_para_ler = 'pessoas.csv' # Descomente e use este se for o caso

    ler_csv_pessoas(nome_do_arquivo_para_ler)