'''
Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400
'''

def eh_ano_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    print("--- Verificador de Ano Bissexto ---")

    while True:
        try:
            ano_digitado = int(input("Digite um ano para verificar (ou 0 para sair): "))

            if ano_digitado == 0:
                print("Saindo do programa. Até mais!")
                break

            if eh_ano_bissexto(ano_digitado):
                print(f"O ano {ano_digitado} é um **ano bissexto**!")
            else:
                print(f"O ano {ano_digitado} **não é um ano bissexto**.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o ano.")
        
        print("-" * 30) # Linha divisória para clareza

if __name__ == "__main__":
    main()