from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir="./")
# tell app instance to read the swagger.yaml file from the 
# specification directory and configure the system to provide the
# connexion functionality
app.add_api("swagger.yaml")

# app = Flask(__name__)


@app.route("/")
def home():
    # templates are located in templates directory
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)