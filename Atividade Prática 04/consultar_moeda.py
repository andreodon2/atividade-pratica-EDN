import requests
from datetime import datetime

def consultar_cotacao_moeda():
    print("Bem-vindo ao Consultor de Cotação de Moedas!")
    print("Moedas disponíveis (exemplos): USD (Dólar Americano), EUR (Euro), GBP (Libra Esterlina), JPY (Iene Japonês)")

    while True:
        codigo_moeda = input("\nDigite o código da moeda desejada (ex: USD, EUR, GBP) ou 'sair' para encerrar: ").upper()

        if codigo_moeda == 'SAIR':
            print("Programa encerrado.")
            break

        if not codigo_moeda.isalpha() or len(codigo_moeda) != 3:
            print("Código de moeda inválido. Por favor, digite um código de 3 letras (ex: USD).")
            continue

        url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

        try:
            response = requests.get(url)
            response.raise_for_status()

            data = response.json()

            chave_cotacao = f"{codigo_moeda}BRL"

            if chave_cotacao in data:
                cotacao = data[chave_cotacao]

                nome_moeda = cotacao.get('name', 'N/A').replace('/BRL', '')
                valor_atual = float(cotacao.get('bid', 0))
                valor_maximo = float(cotacao.get('high', 0))
                valor_minimo = float(cotacao.get('low', 0))
                
                timestamp_atualizacao = int(cotacao.get('timestamp', 0))
                data_hora_atualizacao = datetime.fromtimestamp(timestamp_atualizacao).strftime('%d/%m/%Y %H:%M:%S')

                print(f"\n--- Cotação de {nome_moeda} (em relação ao BRL) ---")
                print(f"Moeda: {nome_moeda} ({codigo_moeda})")
                print(f"Valor Atual (Compra): R$ {valor_atual:.4f}")
                print(f"Valor Máximo (24h): R$ {valor_maximo:.4f}")
                print(f"Valor Mínimo (24h): R$ {valor_minimo:.4f}")
                print(f"Última Atualização: {data_hora_atualizacao}")
                print("--------------------------------------------------")
            else:
                print(f"Não foi possível encontrar a cotação para {codigo_moeda}. Verifique o código da moeda.")
                print("Lembre-se que a AwesomeAPI pode não ter dados para todas as combinações de moedas.")

        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: Não foi possível conectar à API. Verifique sua conexão ou tente mais tarde. Detalhes: {e}")
        except ValueError:
            print(f"Erro: Resposta inválida da API. Não foi possível processar os dados.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    consultar_cotacao_moeda()