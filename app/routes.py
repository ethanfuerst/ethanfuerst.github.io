from app import app
from flask import render_template


@app.route("/")
def index():
    return render_template("index.html", show_url=False)


@app.route("/dashboards/venmo_splitter/")
def venmo_splitter():
    return render_template(
        "dashboards/venmo_splitter.html", title="Venmo Splitter", show_url=True
    )


@app.route("/dashboards/nba/")
def nba():
    return render_template("dashboards/nba.html", title="NBA Dashboard", show_url=True)


@app.route("/dashboards/imdb_ratings/")
def imdb_ratings():
    return render_template(
        "dashboards/imdb_ratings.html", title="IMDb Dashboard", show_url=True
    )


@app.route("/dashboards/bitcoin/")
def bitcoin():
    return render_template(
        "dashboards/bitcoin.html", title="Bitcoin Dashboard", show_url=True
    )


@app.route("/dashboards/mpg/")
def mpg():
    return render_template("dashboards/mpg.html", title="MPG Dashboard", show_url=True)
