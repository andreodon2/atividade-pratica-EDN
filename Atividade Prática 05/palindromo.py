import re # Módulo para expressões regulares, útil para remover pontuação

def verificar_palindromo(texto):
    """
    Verifica se uma palavra ou frase é um palíndromo, ignorando espaços e pontuação.

    Args:
        texto (str): A palavra ou frase a ser verificada.

    Returns:
        str: "Sim" se for um palíndromo, "Não" caso contrário.
    """
    # 1. Remover caracteres não alfanuméricos (espaços, pontuação)
    #    e converter para minúsculas.
    #    're.sub(r'[^a-zA-Z0-9]', '', texto)' substitui tudo que NÃO for letra ou número por vazio.
    texto_limpo = re.sub(r'[^a-zA-Z0-9]', '', texto).lower()

    # 2. Comparar a string limpa com sua versão invertida
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

if __name__ == "__main__":
    print("--- Verificador de Palíndromos ---")
    print("Vamos descobrir se uma palavra ou frase é um palíndromo!")
    print("Exemplos: 'ovo', 'arara', 'A mala nada na lama'")

    while True:
        entrada_usuario = input("\nDigite uma palavra ou frase (ou 'sair' para encerrar): ")

        if entrada_usuario.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        resultado = verificar_palindromo(entrada_usuario)
        print(f"É um palíndromo? {resultado}")
        print("-----------------------------------")