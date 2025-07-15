from datetime import datetime

def calcular_idade_em_dias(ano_nascimento, mes_nascimento, dia_nascimento):
    """
    Calcula a idade de uma pessoa em dias, baseando-se na data de nascimento fornecida.

    Args:
        ano_nascimento (int): O ano de nascimento da pessoa.
        mes_nascimento (int): O mês de nascimento da pessoa.
        dia_nascimento (int): O dia de nascimento da pessoa.

    Returns:
        int or None: A idade em dias se a data for válida, ou None em caso de erro.
    """
    try:
        # Cria um objeto datetime para a data de nascimento
        data_nascimento = datetime(ano_nascimento, mes_nascimento, dia_nascimento)
        
        # Obtém a data e hora atuais
        data_atual = datetime.now()
        
        # Calcula a diferença entre as duas datas
        diferenca = data_atual - data_nascimento
        
        # Retorna o número de dias da diferença
        return diferenca.days
        
    except ValueError:
        print("Erro: Data de nascimento inválida. Por favor, verifique o ano, mês e dia.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None

if __name__ == "__main__":
    print("--- Calculadora de Idade em Dias ---")
    
    while True:
        try:
            print("\nPor favor, digite sua data de nascimento:")
            ano = int(input("Ano (AAAA): "))
            mes = int(input("Mês (MM): "))
            dia = int(input("Dia (DD): "))
            
            idade_dias = calcular_idade_em_dias(ano, mes, dia)
            
            if idade_dias is not None:
                print(f"\nVocê viveu aproximadamente {idade_dias} dias até agora!")
                print("-------------------------------------")
            
            continuar = input("Deseja calcular outra idade? (s/n): ").lower()
            if continuar != 's':
                print("Programa encerrado.")
                break
                
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros para o ano, mês e dia.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")