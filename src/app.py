from flask import render_template


import config
from models import Person


app = config.connex_app
# tell app instance to read the swagger.yaml file from the
# specification directory and configure the system to provide the
# connexion functionality
app.add_api(config.basedir / "data/swagger.yaml")


@app.route("/")
def home():
    people = Person.query.all()
    # templates are located in templates directory
    return render_template("home.html", people=people)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
