# Revisiting Flask

- Following
  - [PART 1](https://realpython.com/flask-connexion-rest-api/#adding-your-first-rest-api-endpoint)
  - [PART 2](https://realpython.com/flask-connexion-rest-api-part-2/)

## Connexion module

- allows a python program to use the OpenAPI specification with Swagger.
- The OpenAPI specification is an API description format for REST APIs and provides a lot of functionality including:
  - Validation of i/p and o/p data to and from our API
  - Configuration of the API URL endpoints and the expected parameters
- When we use OpenAPI with Swagger, we can create a user interface to explore the API.
- All of this can happen when we create a configuration file that our flask application can access `swagger.yaml`

### Add connexion to the App

- There are 2 steps to adding a REST API URL endpoint to our Flask application with Connexion:

  - Add an API configuration file to our project (swagger.yaml)
  - Connect our Flask app with the configuration file

    - we'll use connexion to create the application instance rather than Flask

    ```py
    import connexion
    app = connexion.App(__name__, specification_dir="./")
    app.add_api("swagger.yaml")
    ```

## Flask-Marshmallow

- This extends the Marshmallow library and provides additional features when we work with Flask
- Marshmallow is a serializer that converts complex data types to and from python data types
  - we can then use this functionality to serialize and deserialize Python objects as they flow in and out of our REST API, which is based on JSON
  - Marshmallow converts Python class instances to objects that can be converted to JSON
- `flask-marshmallow[sqlalchemy]` using the sqlalchemy option we can aslo install packages that helps our flask app leverage the powers of SQLAlchemy
  - Because SQLAlchemy returns data as Python class instances, Connexion can't serialize these class instances to JSON-formatted data
    - Here, serializing means converting python objects, which can contain other Python objects and complex data types, into simpler data structures that can be parsed into JSON data types
    - our Person class contains a timestamp, which is a Python DateTime Class. There's no DateTime definition in JSON, so the timestamp has to be converted to a string in order to exist in JSON structure
- Marshmallow helps us to create a PersonSchema class, which is like the SQLAlchemy Person class that we created.
  - The PersonSchema class defines how the attributes of a class will be converted into JSON-friendly format
  - Marshmallow also makes sure that all attributes are present and contain the expected data type

## Useful things

- `localhost:8000/api/ui` to see our API documentation in action

### SQLite database

- run the `sqlite_setup.py` script
- check if the table is setup properly run `sqlite_check.py` script
- to view the data:

  - ```py

    ```
