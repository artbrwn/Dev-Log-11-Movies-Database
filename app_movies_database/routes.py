from app_movies_database import app
from flask import render_template, request, redirect
from app_movies_database.models import search, get_movie, select_comments_by_movie_id, insert_comment
from datetime import datetime
from app_movies_database.forms import CommentsForm
from http import HTTPStatus

@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def load_search():
    # Almacenar los parámetros de búsqueda
    text_search_query = request.args.get("text-search")
    year_search_query = request.args.get("year-search", default="")

    # Almacenar los resultados de la búsqueda
    result = search(text_search_query, year_search_query)

    return render_template("search_results.html", search_results=result)

@app.route("/details/<imdb_id>", methods=["GET", "POST"])
def show_details(imdb_id):
    movie_data = get_movie(imdb_id)

    if movie_data["Response"] == "False":
        return render_template("404.html", result=movie_data), HTTPStatus.NOT_FOUND

    form = CommentsForm()

    # Obtenemos comentarios y posible error
    movie_comments, comments_error = select_comments_by_movie_id(imdb_id)

    if request.method == "POST" and form.validate_on_submit():
        message = insert_comment([
            imdb_id,
            form.user_name.data,
            form.comment.data,
            datetime.now().isoformat()
        ])
        # Volvemos a obtener comentarios actualizados
        movie_comments, comments_error = select_comments_by_movie_id(imdb_id)
        return render_template(
            "details.html",
            result=movie_data,
            comments=movie_comments,
            form=form,
            feedback_message=message,
            comments_error=comments_error
        )

    return render_template(
        "details.html",
        result=movie_data,
        comments=movie_comments,
        form=form,
        feedback_message=None,
        comments_error=comments_error
    )

@app.route("/contact")
def show_contact():
    return render_template("contact.html")