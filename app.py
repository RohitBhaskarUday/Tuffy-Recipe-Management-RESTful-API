from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): #constructor for creating the database object.
  pass
db = SQLAlchemy(model_class=Base) #object created to define models and execute queries.

app = Flask(__name__) #setting the instance of the Flask App.


app.config["SQLALCHEMY_DATABASE_URI"]="mysql://root:world999$@localhost/recipedb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app) #initializing the app

#creating the database model for recipe
class Recipes(db.Model):
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  recipe_name = db.Column(db.String(500), nullable=False)
  instructions = db.Column(db.String(500))
  
#creating the db model for user
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    


#run server
if __name__ == "__main__":
  app.run(debug=True)
  