import random
import string

def gerar_senha(quantidade_caracteres):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    senha = ''.join(random.choice(caracteres) for i in range(quantidade_caracteres))
    return senha

if __name__ == "__main__":
    while True:
        try:
            quantidade = int(input("Digite a quantidade de caracteres para a senha (mínimo 6): "))
            
            if quantidade < 6:
                print("A quantidade de caracteres deve ser no mínimo 6. Por favor, tente novamente.")
            else:
                senha_gerada = gerar_senha(quantidade)
                print(f"Sua senha aleatória gerada é: {senha_gerada}")
                break 
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")