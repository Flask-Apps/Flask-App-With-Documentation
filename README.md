# Revisiting Flask

- Following
  - [PART 1](https://realpython.com/flask-connexion-rest-api/#adding-your-first-rest-api-endpoint)

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

## Useful things

- `localhost:8000/api/ui` to see our API documentation in action
