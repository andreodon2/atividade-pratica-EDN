import json
import os

def escrever_json_pessoa(nome_arquivo, dados_pessoa):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados_pessoa, arquivo_json, indent=4, ensure_ascii=False)
        print(f"Dados gravados com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo JSON: {e}")

def ler_json_pessoa(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_lidos = json.load(arquivo_json)
        
        print(f"\nConteúdo lido do arquivo '{nome_arquivo}':")
        print(f"Nome: {dados_lidos.get('Nome', 'N/A')}")
        print(f"Idade: {dados_lidos.get('Idade', 'N/A')}")
        print(f"Cidade: {dados_lidos.get('Cidade', 'N/A')}")
        
    except json.JSONDecodeError:
        print(f"Erro: O arquivo '{nome_arquivo}' não é um JSON válido ou está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo JSON: {e}")

if __name__ == "__main__":
    nome_do_arquivo_json = 'pessoa.json'

    dados_da_pessoa = {
        'Nome': 'Mariana Santos',
        'Idade': 29,
        'Cidade': 'Porto Alegre'
    }

    escrever_json_pessoa(nome_do_arquivo_json, dados_da_pessoa)

    ler_json_pessoa(nome_do_arquivo_json)

    print("\n--- Modificando e Reescrevendo ---")
    dados_da_pessoa['Idade'] = 30 
    dados_da_pessoa['Profissão'] = 'Engenheira' 
    escrever_json_pessoa(nome_do_arquivo_json, dados_da_pessoa)
    ler_json_pessoa(nome_do_arquivo_json)