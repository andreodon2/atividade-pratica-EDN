import requests

def consultar_cep(cep):
    cep = ''.join(filter(str.isdigit, cep))

    if len(cep) != 8:
        print("Erro: O CEP deve conter 8 dígitos numéricos.")
        return None

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if 'erro' in data and data['erro']:
            print(f"Erro: CEP '{cep}' não encontrado.")
            return None
        else:
            return data

    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: Não foi possível se conectar à API ViaCEP. Verifique sua conexão com a internet ou tente novamente mais tarde. Detalhes: {e}")
    except ValueError:
        print(f"Erro: A resposta da API não é um JSON válido. Detalhes: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    return None

if __name__ == "__main__":
    while True:
        cep_digitado = input("Digite o CEP para consulta (apenas números, ou 'sair' para encerrar): ")

        if cep_digitado.lower() == 'sair':
            print("Programa encerrado.")
            break

        endereco_info = consultar_cep(cep_digitado)

        if endereco_info:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {endereco_info.get('cep', 'N/A')}")
            print(f"Logradouro: {endereco_info.get('logradouro', 'N/A')}")
            print(f"Complemento: {endereco_info.get('complemento', 'N/A')}")
            print(f"Bairro: {endereco_info.get('bairro', 'N/A')}")
            print(f"Cidade: {endereco_info.get('localidade', 'N/A')}")
            print(f"Estado (UF): {endereco_info.get('uf', 'N/A')}")
            print(f"DDD: {endereco_info.get('ddd', 'N/A')}")
            print("-------------------------------\n")
        else:
            print("Não foi possível obter informações para o CEP fornecido.\n")