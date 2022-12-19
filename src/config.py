import pathlib
import connexion

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# pure path to project directory
basedir = pathlib.Path(__file__).parent.parent.resolve()
# uses the basedir variable to create the Connexion app instance
# and give it the path to the directory that contains our 
# specification file
connex_app = connexion.App(__name__, specification_dir=basedir)

# create flask instance initialized by connexion
app = connex_app.app

database_uri = f"sqlite://{basedir / 'data/people.db'}"
# print(database_uri)
# tell sqlalchemy to use sqlite as database and use people.db
# file as database file
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

# turn the SQLAlchemy event system off.
# the event system generates events that are useful in event-driven
# programs, but adds significant overhead.
# our program isn't event driven one so, off 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# initializes SQLAlchemy by passing the app configuration
# information to SQLAlchemy and assigning the result to a
# db variable
db = SQLAlchemy(app)

# initializes marshmallow and allows it to work with the
# SQLAlchemy components attached to the app
ma = Marshmallow(app)


