import requests
from config import API_KEY
from app_movies_database.connection import Connection
from datetime import datetime

def search(text_search, year_search):
    """
    Recibe un str de búsqueda (y opcionalmente un año),
    consulta la API de OMDb y devuelve el resultado.
    """

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={text_search}"
    
    if year_search:
        url += f"&y={year_search}"
    
    response = requests.get(url)
    return response.json()


def get_movie(id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={id}"
    response = requests.get(url)

    return response.json()

def select_comments_by_movie_id(movie_id):
    """
    Recibe un imdb_id y devuelve todos los resultados 
    ordenados por fecha de más recientes a más antiguos
    como una lista de diccionarios.
    """
    connect = Connection(f'SELECT * FROM comentario WHERE id_pelicula ="{movie_id}" ORDER BY fecha DESC;')
    result = connect.response.fetchall()
    connect.response.close()
    dictionaries_result = []
    for row in result:
        comment_data = {}
        comment_data["id"] = row[0]
        comment_data["id_pelicula"] = row[1]
        comment_data["persona"] = row[2]
        comment_data["comentario"] = row[3]
        
        try:
            fecha_original = datetime.fromisoformat(row[4])
            comment_data["fecha"] = fecha_original.strftime("%d/%m/%y %H:%M")

        except Exception:
            comment_data["fecha"] = row[4]
            
        dictionaries_result.append(comment_data)

    return dictionaries_result

def insert_comment(register_form):
    connect = Connection("INSERT INTO comentario (id_pelicula, persona, comentario, fecha) VALUES (?, ?, ?, ?)", register_form)
    connect.connection.commit()
    connect.connection.close()