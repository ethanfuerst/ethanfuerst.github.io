from flask_frozen import Freezer

from app import app

app.config["FREEZER_DESTINATION"] = "../docs"
app.config["FREEZER_REMOVE_EXTRA_FILES"] = False
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()
