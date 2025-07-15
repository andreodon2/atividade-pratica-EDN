def calcular_media_turma():
    print("--- Calculadora de Média da Turma ---")
    print("Digite as notas dos alunos (entre 0 e 10).")
    print("Para finalizar e calcular a média, digite 'fim'.")

    total_notas = 0.0
    quantidade_notas = 0

    while True:
        entrada = input("Digite a nota (ou 'fim' para finalizar): ").lower()

        if entrada == 'fim':
            print("\nFinalizando o registro de notas...")
            break

        try:
            nota = float(entrada.replace(',', '.'))

            if 0 <= nota <= 10:
                total_notas += nota
                quantidade_notas += 1
                print(f"Nota {nota:.2f} registrada com sucesso!")
            else:
                print(f"Aviso: A nota {nota:.2f} é inválida. Por favor, digite uma nota entre 0 e 10.")
        
        except ValueError:
            print(f"Erro: '{entrada}' não é um número válido. Por favor, digite um número entre 0 e 10 ou 'fim'.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")
        
        print("-----------------------------------")

    print("\n--- Resultado Final ---")
    if quantidade_notas > 0:
        media = total_notas / quantidade_notas
        print(f"Total de notas válidas registradas: {quantidade_notas}")
        print(f"Soma das notas: {total_notas:.2f}")
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi inserida para calcular a média.")
    print("-----------------------")

if __name__ == "__main__":
    calcular_media_turma()