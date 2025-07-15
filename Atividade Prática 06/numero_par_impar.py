def verificar_par_impar():
    print("--- Verificador de Números Pares e Ímpares ---")
    print("Digite números inteiros. Para finalizar, digite 'fim'.")

    contagem_pares = 0
    contagem_impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para sair): ").lower()

        if entrada == 'fim':
            print("\nFinalizando o programa...")
            break

        try:
            numero = int(entrada)

            if numero % 2 == 0:
                print(f"O número {numero} é PAR.")
                contagem_pares += 1
            else:
                print(f"O número {numero} é ÍMPAR.")
                contagem_impares += 1

        except ValueError:
            print(f"Erro: '{entrada}' não é um número inteiro válido. Por favor, digite um número inteiro ou 'fim'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")
        
        print("-----------------------------------")

    print("\n--- Resumo ---")
    print(f"Total de números pares inseridos: {contagem_pares}")
    print(f"Total de números ímpares inseridos: {contagem_impares}")
    print("----------------")

if __name__ == "__main__":
    verificar_par_impar()