from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__, template_folder="templates", static_folder="static")
bootstrap = Bootstrap(app)


from app import routes
