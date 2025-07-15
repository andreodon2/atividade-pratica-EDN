import requests

def gerar_perfil_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        usuario = data['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("--- Perfil de Usuário Aleatório ---")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        print("---------------------------------")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API: {e}")
    except KeyError:
        print("Erro: Não foi possível extrair os dados do usuário. O formato da API pode ter mudado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    gerar_perfil_usuario_aleatorio()