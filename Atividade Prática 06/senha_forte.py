import string # Para acessar conjuntos de caracteres como letras e pontuação

def verificar_senha_forte_corrigida():
    """
    Verifica se uma senha atende aos critérios de "forte":
    - Pelo menos 8 caracteres.
    - Conter pelo menos um número.
    - Conter pelo menos uma letra (maiúscula ou minúscula).
    - (Opcional, mas boa prática) Conter pelo menos um caractere especial.
      Para este exemplo, vamos exigir número E letra.
    O programa continua pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
    """
    print("--- Verificador de Senha Forte ---")
    print("Para ser forte, sua senha precisa ter:")
    print("  - Pelo menos 8 caracteres.")
    print("  - Pelo menos um número (0-9).")
    print("  - Pelo menos uma letra (maiúscula ou minúscula).")
    print("Digite 'sair' a qualquer momento para encerrar o programa.")

    while True:
        senha = input("\nPor favor, digite sua senha: ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        # 1. Verifica o comprimento da senha
        if len(senha) < 8:
            print("Senha fraca: A senha deve ter pelo menos 8 caracteres.")
            continue # Pede uma nova senha

        # 2. Verifica se contém pelo menos um número
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break
        if not tem_numero:
            print("Senha fraca: A senha deve conter pelo menos um número.")
            continue

        # 3. Verifica se contém pelo menos uma letra (maiúscula ou minúscula)
        tem_letra = False
        for caractere in senha:
            if caractere.isalpha(): # Verifica se o caractere é uma letra
                tem_letra = True
                break
        if not tem_letra:
            print("Senha fraca: A senha deve conter pelo menos uma letra (maiúscula ou minúscula).")
            continue
        
        # Se chegou até aqui, a senha é forte (atende a todos os critérios)
        print("Senha forte! Sua senha atende aos requisitos de segurança.")
        print("---------------------------------")
        break # Sai do loop, pois uma senha válida foi inserida

if __name__ == "__main__":
    verificar_senha_forte_corrigida()