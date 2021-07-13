from flask import Flask
from flask_restful import Resource, Api
from models.User import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)
api = Api(app)

api.add_resource(User, '/')

if __name__ == '__main__':
    app.run(debug=True)