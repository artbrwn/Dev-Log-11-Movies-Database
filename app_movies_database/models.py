import requests

def search_by_title(search):
    """
    Recibe un str de búsqueda, consulta la api de 
    """
    url = f"http://www.omdbapi.com/?apikey={key}&s={search}"
    response = requests.get(url)

    return response.json()

def search_by_year(search):
    pass