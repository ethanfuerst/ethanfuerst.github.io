import os

import frontmatter
import markdown2
from flask import abort, render_template

from app import app

POSTS_DIR = os.path.join(os.path.dirname(__file__), "posts")


@app.route("/")
def index():
    return render_template("index.html", show_url=False)


@app.route("/dashboards/venmo_splitter/")
def venmo_splitter():
    return render_template(
        "dashboards/venmo_splitter.html", title="Venmo Splitter", show_url=True
    )


@app.route("/dashboards/imdb_ratings/")
def imdb_ratings():
    return render_template(
        "dashboards/imdb_ratings.html", title="IMDb Ratings", show_url=True
    )


@app.route("/blog/<post_name>.html")
def blog_post(post_name):
    post_path = os.path.join(POSTS_DIR, f"{post_name}.md")

    if not os.path.exists(post_path):
        return abort(404)

    with open(post_path, "r") as f:
        post = frontmatter.load(f)

    content = markdown2.markdown(post.content, extras=["tables"])

    return render_template(
        "blog_post.html",
        content=content,
        show_url=True,
        **post.metadata,
    )


@app.route("/blog/")
def blog():
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            with open(os.path.join(POSTS_DIR, filename), "r") as f:
                post = frontmatter.load(f)
            posts.append(
                {
                    "slug": filename[:-3],
                    "title": post.metadata.get("title", "Untitled"),
                    "date": post.metadata.get("date"),
                    "description": post.metadata.get("description", ""),
                }
            )

    posts.sort(key=lambda x: x["date"], reverse=True)

    return render_template(
        "blog.html",
        title="Blog",
        posts=posts,
        show_url=True,
    )
