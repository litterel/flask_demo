from flask import Flask
<<<<<<< HEAD
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
from app import views
=======
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object('config')
from app import views,models
>>>>>>> 72d2fd806d1f0e5aad5db6ea67f5e3b66afb77d0
