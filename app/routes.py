from flask import render_template

from app import app


@app.route("/")
def index():
    return render_template("index.html", show_url=False)


@app.route("/dashboards/venmo_splitter/")
def venmo_splitter():
    return render_template(
        "dashboards/venmo_splitter.html", title="Venmo Splitter", show_url=True
    )
