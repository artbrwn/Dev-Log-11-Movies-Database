import requests
from config import API_KEY
from app_movies_database.connection import Connection
from datetime import datetime
import sqlite3

def search(text_search, year_search):
    """
    Recibe un str de búsqueda (y opcionalmente un año),
    consulta la API de OMDb y devuelve el resultado.
    """

    url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={text_search}"
    
    if year_search:
        url += f"&y={year_search}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

    except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError) as e:
        return {"Response": "False", "Error": f"Error al obtener los datos: {e}"}

    if data.get("Response") == "False" and data.get("Error") == "Too many results.":
        data["Error"] = "Demasiados resultados. Por favor, especifica mejor tu búsqueda."
    
    return data

def get_movie(id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={id}"
    try:
        response = requests.get(url, timeout=5)
        return response.json()
    
    except (requests.exceptions.RequestException, requests.exceptions.JSONDecodeError) as e:
        return {"Response": "False", "Error": f"Error al obtener los datos: {e}"}

def select_comments_by_movie_id(movie_id):
    """
    Devuelve los comentarios asociados a una película y None si no hay error.
    Si ocurre un error, devuelve una lista vacía y un mensaje de error.
    """
    try:
        connect = Connection(f'SELECT * FROM comentario WHERE id_pelicula = "{movie_id}" ORDER BY fecha DESC;')
        result = connect.response.fetchall()
        connect.response.close()
    except Exception as e:
        # Devuelve estructura controlada si falla la base de datos
        return [], f"Error al obtener los comentarios: {e}"

    dictionaries_result = []
    for row in result:
        comment_data = {
            "id": row[0],
            "id_pelicula": row[1],
            "persona": row[2],
            "comentario": row[3]
        }

        try:
            fecha_original = datetime.fromisoformat(row[4])
            comment_data["fecha"] = fecha_original.strftime("%d/%m/%y %H:%M")
        except Exception:
            comment_data["fecha"] = row[4]

        dictionaries_result.append(comment_data)

    # Si todo va bien, devolvemos lista y None (sin error)
    return dictionaries_result, None

def insert_comment(register_form):
    try:
        connect = Connection(
            "INSERT INTO comentario (id_pelicula, persona, comentario, fecha) VALUES (?, ?, ?, ?)",
            register_form
        )
        connect.connection.commit()
        connect.connection.close()
        return "Comentario guardado correctamente"
    
    except sqlite3.Error as e:
        return f"Comentario no guardado: {e}"