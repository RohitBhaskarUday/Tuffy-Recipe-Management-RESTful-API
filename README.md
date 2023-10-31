# Tuffy-Recipe-Managment-RESTful-API
#### Project Team Members : Pavana Manjunath(CWID : 885154195), Rohit Bhaskar Uday (CWID : )
# Project Description
####  We  created a Flask framework for building a Recipe Management RESTful-API. This API allows users to perform various CRUD operations, including robust error handling, strong JWT (JSON Web Token) authentication for secure user access, and secure file handling with validations on file types and sizes.This Readme file includes a detailed instructions for easy setup and deployment of python based template for creating Flask APIs.       
### Drive Link For the Project Demonstration and Screenshots
# Prerequisites
- Before you begin, ensure that you have the following prerequisites:

- Python (3.6 or higher) installed on your system.
Create a Python virtual environment to isolate the application's dependencies:
      python -m venv venv
  Activate the virtual environment:
       .\venv\Scripts\activate.bat
- Install the required packages using pip:

  Like pip install Flask flask_sqlalchemy pymysql

  Configure the SQLAlchemy database to connect to a MySQL database named "recipedb."
- Running the Application
1) In the terminal, navigate to the project directory where app.py is located.
2) To start the Flask application, use the following command:
flask run The application will be accessible at http://localhost:5000 in your web browser.

Accessing the Application Once the application is running, you can access it by opening your web browser and navigating to http://localhost:5000.
# Routes and Endpoints
- '/': This is the root route, which simply displays a welcome message.
- /recipes:
     - GET: Fetches a list of all recipe names.
     - POST: Adds a new recipe with a name and instructions.
- /recipes/<recipe_name>:
    - PUT: Updates the instructions for a specific recipe.
  -  DELETE: Deletes a specific recipe.
- /register: Allows users to register by providing a username and password.
- /login: Enables users to log in with their credentials and receive a JWT access token.
- /protected: A protected endpoint to check the current user's identity using the JWT access token.
- /protected/recipes (protected): Allows authorized users to access all recipes, including their instructions.
# Error Handlers
 Define error handlers for HTTP status codes 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Internal Server Error), and 409 (Conflict Error). These handlers return appropriate error messages.You can access different routes to test these error responses, such as: • /unauthorized to simulate a 401 error (Unauthorized) • /check_age to check if a provided age is valid (with potential 400 error) • /trigger_error to simulate a 500 error (Internal Server Error) • The application responds with appropriate error messages based on the route you access.

