from app_movies_database import app
from flask import render_template, request
from app_movies_database.models import search_by_title, search_by_year

@app.route("/hello")
def hello():
    return "Hello, World"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results")
def load_search():
    search = request.args.get("search")
    if search.isnumeric():
        result = search_by_year(search)
    else:
        result = search_by_title(search)
    return render_template("search_results.html", search_results=result)