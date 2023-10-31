# Tuffy-Recipe-Managment-RESTful-API
#### Project Team Members : Pavana Manjunath(CWID : 885154195), Rohit Bhaskar Uday (CWID : 884451915 )
# Project Description
####  We  created a Flask framework for building a Recipe Management RESTful-API. This API allows users to perform various CRUD operations, including robust error handling, strong JWT (JSON Web Token) authentication for secure user access, and secure file handling with validations on file types and sizes.This Readme file includes a detailed instructions for easy setup and deployment of python based template for creating Flask APIs.       
### Drive Link For the Project Demonstration and Screenshots


# Features
- View a list of available recipes.
- Add new recipes with names and instructions.
- Update recipe instructions.
- Delete recipes.
- User registration and authentication.
- Protected endpoints for authenticated users.
- File upload for recipes with validation (file type and size).
- Serving and downloading uploaded recipe files.
# Getting Started
- Clone or download this repository to your local machine.
- Create a MySQL database named recipedb (you can modify the database URI in the code).
- Configure the UPLOAD_FOLDER to specify the folder where uploaded files will be stored.
- The API should be running on http://localhost:5000/.
# Error Handlers
 Define error handlers for HTTP status codes 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 500 (Internal Server Error), and 409 (Conflict Error). These handlers return appropriate error messages.You can access different routes to test these error responses, such as: Failed to upload the file(400), File uploaded successfully(200),No recipes found (404), Invalid credentials (401).
# Authentication
- User Registration: Users can register with a unique username and password.
- User Login: Users can log in with their credentials to obtain a JWT access token.
- JWT Protection: Certain endpoints are protected and require a valid JWT access token for access.
# Endpoints
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
# File Handling
- It Configures the file upload settings, such as the allowed file types(txt, docx, pdf, jpg etc..) and maximum file size. Also, It is stored in a specific folder where its uploaded.This endpoint will accept POST requests with file data.
- /fileupload endpoint that accepts file uploads and performs file type and size validation. The uploaded files are stored in the "recipies_files" folder within our project's directory. 
# Public Route
- The public route is defined with the @api.route decorator and set to respond to GET requests.
- Inside the /recipies function, it define a list of public recipies. 
- The jsonify function is used to convert the list of public items into a JSON response.
- When users access the /recipies route, they will receive a JSON response containing the list of public recipies. No authentication is required to access this endpoint.
# Web Services: CRUD operations
- View all recipes: GET /recipes
- Add a new recipe: POST /recipes
- Update a recipe: PUT /recipes/<recipe_name>
- Delete a recipe: DELETE /recipes/<recipe_name>






