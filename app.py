from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from routes.ImagesRoutes import ImagesUpload
from routes.adminRoutes import AdminMethods, AdminMethodsPa
from routes.citizensRoutes import CitizenMethods, CitizenMethodsPa
# from flask_mail import Mail

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)

# DataBase Configuration
app.config['UPLOAD_FOLDER'] = 'static/images'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
# mail = Mail(app)

api.add_resource(ImagesUpload, '/uploader')
api.add_resource(AdminMethods, '/admin')
api.add_resource(AdminMethodsPa, '/admin/<string:id>')
api.add_resource(CitizenMethods, '/citizen')
api.add_resource(CitizenMethodsPa, '/citizen/<string:id>')


if __name__ == '__main__':
    app.run(debug=True)