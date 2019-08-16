from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# config database
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants_v1.db'

# here DB is made
db = SQLAlchemy(app)

db.create_all()

class ExampleTable(db.Model):


@app.route('/')
def main():

  return 'Hello World!'


if __name__ == '__main__':
  app.config['DEBUG'] = True
  app.run(debug=True)

  db.init_app(app)



# good tut https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
# with good git https://github.com/sixhobbits/flask-crud-app/blob/master/bookmanager.py
