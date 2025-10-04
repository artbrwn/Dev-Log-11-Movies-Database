import requests
from config import API_KEY

def search(search):
    """
    Recibe un str de búsqueda, consulta la api de omdbapi y devuelve el resultado
    """
    if search.isnumeric():
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={search}"
    else:
        url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={search}"
    
    response = requests.get(url)

    return response.json()
