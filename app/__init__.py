from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] ='fd8ab5bd9d7f18715270fa3dd0005b645c7d7baae0967d0dbcd3d170caf70593'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abnas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

from app import models
from app import routes