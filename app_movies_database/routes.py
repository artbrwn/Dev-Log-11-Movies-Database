from app_movies_database import app
from flask import render_template, request, redirect
from app_movies_database.models import search, get_movie, select_comments_by_movie_id, insert_comment
from datetime import datetime

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

@app.route("/details/<imdb_id>", methods=["GET", "POST"])
def show_details(imdb_id):
    movie_data = get_movie(imdb_id)
    if request.method == "POST":
        comment_data = request.form
        insert_comment([
            imdb_id,
            comment_data["user_name"],
            comment_data["comment"],
            datetime.now()
        ])
        return redirect(f"/details/{imdb_id}")
    else:
        movie_comments = select_comments_by_movie_id(imdb_id)
        return render_template("details.html", result=movie_data, comments=movie_comments)

@app.route("/contact")
def show_contact():
    return render_template("contact.html")