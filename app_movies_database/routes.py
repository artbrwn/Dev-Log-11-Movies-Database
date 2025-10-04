from app_movies_database import app
from flask import render_template, request
from app_movies_database.models import search, get_movie

@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def load_search():
    # Almacenar los parámetros de búsqueda
    search_query = request.args.get("search")

    # Almacenar los resultados de la búsqueda
    result = search(search_query)

    return render_template("search_results.html", search_results=result)

@app.route("/details/<imdb_id>")
def show_details(imdb_id):
    movie_data = get_movie(imdb_id)
    return render_template("details.html", result=movie_data)